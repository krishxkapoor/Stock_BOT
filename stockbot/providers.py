import requests
import pandas as pd

def fetch_ohlcv_yfinance(symbol, period="1mo", interval="1d"):
    import yfinance as yf
    ticker = yf.Ticker(symbol + ".NS")  # ".NS" for NSE
    df = ticker.history(period=period, interval=interval)
    if df.empty:
        return None
    df = df.reset_index()
    return df

def fetch_ohlcv(symbol, period="1mo", interval="1d"):
    return fetch_ohlcv_yfinance(symbol, period, interval)

def get_latest_price(symbol):
    df = fetch_ohlcv(symbol, period="1d", interval="1d")
    if df is not None and not df.empty:
        return df.iloc[-1]["Close"]
    return None
