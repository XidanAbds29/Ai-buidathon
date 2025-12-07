from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import UserData, CreditScoreResponse, ExplanationResponse
from ai_engine import engine

app = FastAPI(title="FinTech AI Credit Platform")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FinTech AI Build-a-thon API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/score", response_model=CreditScoreResponse)
def get_credit_score(user: UserData):
    try:
        return engine.calculate_score(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/explain", response_model=ExplanationResponse)
def get_explanation(user: UserData):
    # In a real app, we might just pass the ID, but here we pass the full user object for the stateless mock
    try:
        score_response = engine.calculate_score(user)
        return engine.generate_explanation(user, score_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
