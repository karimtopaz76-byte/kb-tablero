import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import pytz

st.set_page_config(page_title="BK TRADING TERMINAL PRO", layout="wide", page_icon="📈")

st.markdown("""
<style>
.stApp {background:#080808;}
.card {background:#151515; border:1px solid #222; padding:20px; border-radius:14px; margin-bottom:14px;}
.card-title {color:#ff8c00; font-weight:800; font-size:11px; letter-spacing:2px; margin-bottom:14px; text-transform:uppercase; border-bottom:1px solid #222; padding-bottom:8px;}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_price(tickers):
    if isinstance(tickers, str):
        tickers=[tickers]
    for tk in tickers:
        try:
            d=yf.Ticker(tk).history(period="5d")
            if len(d)>=2:
                last=float(d.Close.iloc[-1])
                prev=float(d.Close.iloc[-2])
                return last, last-prev, (last-prev)/prev*100 if prev!=0 else 0
        except:
            continue
    return 0.0,0.0,0.0

st.markdown('<div style="color:#ff8c00; font-size:22px; font-weight:800;">BLOOMBERG BK</div><div style="color:#888; font-size:10px; letter-spacing:2px;">TRADING TERMINAL PRO - V10.1</div>', unsafe_allow_html=True)

r1c1,r1c2 = st.columns(2)
with r1c1:
    st.markdown('<div class="card"><div class="card-title">1. Fundamental Analysis - TODAY</div><span style="color:#ddd">FED Mie 24 Sep 20:00 - 87% +25pb<br>CPI 3.1% Hawkish<br>PCE Vie 14:30 clave<br>VIX 14.81</span></div>', unsafe_allow_html=True)
with r1c2:
    st.markdown('<div class="card" style="border-left:3px solid #ff4444;"><div class="card-title">2. Geopolitics LIVE</div><span style="color:#ddd">ORMUZ 90% parado - Brent 100$ riesgo<br>450 drones Moscu - Kapotnia arde<br>Novorossiisk 700k bd suspendido<br>4 ataques USA-Iran</span></div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="card-title">3. Real-Time Data Metrics - LIVE</div></div>', unsafe_allow_html=True)
k1,k2,k3,k4,k5,k6 = st.columns(6)
vix,dvix,pvix = get_price("^VIX")
brent,dbrent,pbrent = get_price(["BZ=F","LCO=F","BNO"])
oro,doro,poro = get_price(["GC=F","GLD"])
dxy,ddxy,pdxy = get_price(["DX-Y.NYB","UUP"])
gas,dgas,pgas = get_price("NG=F")
spx,dspx,pspx = get_price("^GSPC")
k1.metric("VIX", round(vix,2), round(dvix,2))
k2.metric("BRENT", round(brent,2), round(dbrent,2))
k3.metric("GOLD", round(oro,2), round(doro,2))
k4.metric("DXY", round(dxy,2), round(ddxy,2))
k5.metric("GAS", round(gas,2), round(dgas,2))
k6.metric("SPX
