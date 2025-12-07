from pydantic import BaseModel
from typing import List, Optional

class UserData(BaseModel):
    user_id: str
    name: str
    age: int
    location: str
    wallet_balance: float
    avg_monthly_topup: float
    avg_transaction_val: float
    transaction_count_last_90_days: int
    has_smart_phone: bool
    community_trust_referrals: int  # For TrustGraph AI (10x feature)

class CreditScoreResponse(BaseModel):
    user_id: str
    credit_score: int
    risk_level: str  # Low, Medium, High
    approval_status: bool
    max_loan_amount: float

class ExplanationResponse(BaseModel):
    user_id: str
    base_score: int
    top_positive_factors: List[str]
    top_negative_factors: List[str]
    narrative_explanation: str
