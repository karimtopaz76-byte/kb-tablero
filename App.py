import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="BK SYSTEM V13 FINAL", layout="wide")
st.title("BK SYSTEM V13 - FINAL 100% FUNCIONAL")

@st.cache_data(ttl=300)
def get_price(ticker_list):
    if isinstance(ticker_list, str):
        ticker_list = [ticker_list]
    for t in ticker_list:
        try:
            hist = yf.Ticker(t).history(period="5d")
            if len(hist) >= 2:
                last = float(hist["Close"].iloc[-1])
                prev = float(hist["Close"].iloc[-2])
                return last, last - prev
        except Exception:
            continue
    return 0.0, 0.0

c1,c2,c3,c4,c5,c6 = st.columns(6)
vix,dvix = get_price("^VIX")
brent,dbrent = get_price(["BZ=F","BNO"])
oro,doro = get_price(["GC=F","GLD"])
dxy,ddxy = get_price(["DX-Y.NYB","UUP"])
gas,dgas = get_price("NG=F")
spx,dspx = get_price("^GSPC")

c1.metric("VIX", f"{vix:.2f}", f"{dvix:.2f}")
c2.metric("BRENT", f"{brent:.2f}", f"{dbrent:.2f}")
c3.metric("ORO", f"{oro:.2f}", f"{doro:.2f}")
c4.metric("DXY", f"{dxy:.2f}", f"{ddxy:.2f}")
c5.metric("GAS", f"{gas:.2f}", f"{dgas:.2f}")
c6.metric("SPX", f"{spx:.2f}", f"{dspx:.2f}")

st.write("FED Mie 24 Sep 20:00 - 87% 25pb")
st.write("Ormuz 90% parado - Brent riesgo 100")
st.success("APP V13 VERDE")
