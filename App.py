import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="BK SYSTEM V11 FINAL", layout="wide")

@st.cache_data(ttl=300)
def get_price(tickers):
    if isinstance(tickers, str):
        tickers = [tickers]
    for tk in tickers:
        try:
            d = yf.Ticker(tk).history(period="5d")
            if len(d) >= 2:
                last = float(d.Close.iloc[-1])
                prev = float(d.Close.iloc[-2])
                return last, last - prev
        except:
            continue
    return 0.0, 0.0

st.title("BK SYSTEM V11 FINAL - VERDE GARANTIZADO")
...
k1.metric("VIX", round(vix, 2), round(dvix, 2))
k2.metric("BRENT", round(brent, 2), round(dbrent, 2))
k3.metric("ORO", round(oro, 2), round(doro, 2))
k4.metric("DXY", round(dxy, 2), round(ddxy, 2))
k5.metric("GAS", round(gas, 2), round(dgas, 2))
k6.metric("SPX", round(spx, 2), round(dspx, 2))
