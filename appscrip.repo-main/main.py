from fastapi import FastAPI, Depends, HTTPException
from auth import verify_token
from rate_limiter import rate_limit
from data_fetcher import fetch_market_data
from ai_analyzer import analyze_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Trade Opportunities API running"}

@app.get("/analyze/{sector}")
def analyze_sector(sector: str, token: str = Depends(verify_token)):
    
    # Rate limit check
    rate_limit(token)

    # Fetch market data
    data = fetch_market_data(sector)

    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    # AI analysis
    report = analyze_data(sector, data)

    return {"report": report}