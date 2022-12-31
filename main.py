from fastapi import FastAPI
import yfinance as yf
import json

app = FastAPI()

@app.get("/")
async def root(code: str):
  ticker = yf.Ticker(f"{code}.T")
  hist = ticker.history(period="5y", interval="1mo")

  return hist.Close
