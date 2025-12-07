import joblib
import pandas as pd
import numpy as np
import shap
from models import UserData, CreditScoreResponse, ExplanationResponse

class AIEngine:
    def __init__(self):
        try:
            self.model = joblib.load('credit_model.joblib')
            self.explainer = joblib.load('shap_explainer.joblib')
            self.columns = joblib.load('model_columns.joblib')
            print("AI Engine: Real ML Model Loaded Successfully.")
        except Exception as e:
            print(f"AI Engine Warning: Could not load model ({e}). Using fallback logic.")
            self.model = None

    def calculate_score(self, user: UserData) -> CreditScoreResponse:
        if self.model:
            # Prepare input dataframe
            input_data = pd.DataFrame([{
                'wallet_balance': user.wallet_balance,
                'avg_monthly_topup': user.avg_monthly_topup,
                'transaction_count_last_90_days': user.transaction_count_last_90_days,
                'community_trust_referrals': user.community_trust_referrals,
                'has_smart_phone': 1 if user.has_smart_phone else 0,
                'age': user.age
            }])[self.columns]
            
            # Predict
            score = self.model.predict(input_data)[0]
            score = int(np.clip(score, 300, 900))
        else:
            # Fallback Logic (if training failed)
            score = 300 + min(user.avg_monthly_topup * 0.5, 300)
            score = min(900, int(score))

        # Determine risk
        if score >= 750:
            risk = "Low"
            approval = True
            loan_limit = 50000
        elif score >= 600:
            risk = "Medium"
            approval = True
            loan_limit = 20000
        else:
            risk = "High"
            approval = False
            loan_limit = 0
            
        return CreditScoreResponse(
            user_id=user.user_id,
            credit_score=score,
            risk_level=risk,
            approval_status=approval,
            max_loan_amount=loan_limit
        )

    def generate_explanation(self, user: UserData, score_response: CreditScoreResponse) -> ExplanationResponse:
        positives = []
        negatives = []
        narrative = ""

        if self.model:
             # Prepare input
            input_data = pd.DataFrame([{
                'wallet_balance': user.wallet_balance,
                'avg_monthly_topup': user.avg_monthly_topup,
                'transaction_count_last_90_days': user.transaction_count_last_90_days,
                'community_trust_referrals': user.community_trust_referrals,
                'has_smart_phone': 1 if user.has_smart_phone else 0,
                'age': user.age
            }])[self.columns]
            
            # Calculate SHAP values
            shap_values = self.explainer(input_data)
            
            # Get top features
            # shap_values.values is [1, num_features]
            values = shap_values.values[0]
            feature_names = self.columns
            
            # Sort by absolute impact
            sorted_indices = np.argsort(np.abs(values))[::-1]
            
            top_features = []
            for i in sorted_indices[:3]: # Top 3 drivers
                val = values[i]
                name = feature_names[i]
                human_name = name.replace("_", " ").title()
                
                if val > 0:
                    positives.append(f"High {human_name} impacted score positively (+{int(val)} pts)")
                else:
                    negatives.append(f"Low/Negative {human_name} impacted score negatively ({int(val)} pts)")
                    
            narrative = f"Based on the Random Forest analysis, the Credit Score of {score_response.credit_score} is primarily driven by {feature_names[sorted_indices[0]].replace('_', ' ')}." 
        else:
            narrative = "Score generated using rule-based fallback logic."

        return ExplanationResponse(
            user_id=user.user_id,
            base_score=score_response.credit_score,
            top_positive_factors=positives,
            top_negative_factors=negatives,
            narrative_explanation=narrative
        )

engine = AIEngine()
