import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import shap

# 1. Generate Synthetic Data
print("Generating synthetic data...")
np.random.seed(42)
n_samples = 1000

data = {
    'wallet_balance': np.random.exponential(scale=5000, size=n_samples),
    'avg_monthly_topup': np.random.normal(loc=500, scale=200, size=n_samples),
    'transaction_count_last_90_days': np.random.poisson(lam=30, size=n_samples),
    'community_trust_referrals': np.random.choice([0, 0, 0, 1, 2, 3, 5], size=n_samples), # Zero inflated
    'has_smart_phone': np.random.choice([0, 1], size=n_samples, p=[0.3, 0.7]),
    'age': np.random.randint(18, 65, size=n_samples)
}

df = pd.DataFrame(data)

# Logic for "Target" (Probability of Repayment)
# Rule: repayment depends on stability (topup), liquidity (balance), and social trust (referrals)
df['repayment_prob'] = (
    0.3 * (df['wallet_balance'] / 10000).clip(0, 1) +
    0.2 * (df['avg_monthly_topup'] / 1000).clip(0, 1) +
    0.3 * (df['community_trust_referrals'] / 5).clip(0, 1) + 
    0.1 * (df['transaction_count_last_90_days'] / 100).clip(0, 1) +
    0.1 * df['has_smart_phone']
)
# Add some noise
df['repayment_prob'] += np.random.normal(0, 0.05, size=n_samples)
df['credit_score'] = (df['repayment_prob'] * 600 + 300).clip(300, 900).astype(int)

# 2. Train Model
print("Training Random Forest Regressor...")
X = df.drop(['repayment_prob', 'credit_score'], axis=1)
y = df['credit_score']

model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
model.fit(X, y)

# 3. Train Explainer
print("Generating SHAP explainer...")
explainer = shap.Explainer(model)
# We compute shape values for a subset to initialize if needed, but TreeExplainer is fast
# Save the model and explainer
joblib.dump(model, 'credit_model.joblib')
joblib.dump(explainer, 'shap_explainer.joblib')

# Save column names to ensure order matches during inference
joblib.dump(X.columns.tolist(), 'model_columns.joblib')

print("Model and Explainer saved successfully!")
print("Sample Prediction:", model.predict(X.iloc[:1]))
