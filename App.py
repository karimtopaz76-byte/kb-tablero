import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="BK SYSTEM PRO", layout="wide", page_icon="📊")

st.markdown("""
<style>
.card {background:#111; border:1px solid #333; padding:16px; border-radius:10px; margin-bottom:12px;}
.card-title {color:#f59e0b; font-weight:800; font-size:13px; margin-bottom:10px; letter-spacing:1px;}
body {background:#0e0e0e;}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_price_safe(tickers):
    if isinstance(tickers, str):
        tickers = [tickers]
    for t in tickers:
        try:
            d = yf.Ticker(t).history(period="5d")
            if len(d) >= 2:
                return float(d.Close.iloc[-1]), float(d.Close.iloc[-1]-d.Close.iloc[-2]), t
        except:
            continue
    return 0.0, 0.0, "N/A"

st.title("BK SYSTEM V9 PRO")
st.caption("Fundamental + Geopolitica + Real Time + Tecnico + Diario")

c1,c2 = st.columns(2)
with c1:
    st.markdown('<div class="card"><div class="card-title">1. ANALISIS FUNDAMENTAL HOY</div><span style="color:#fff">FED Miercoles 24 Sep 20:00 - 87% subida 25pb<br>CPI 3.1% vs 2% objetivo<br>PCE / NFP Viernes 26 Sep 14:30 clave<br>VIX 14.81 riesgo controlado</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><div class="card-title">2. GEOPOLITICA LIVE - 20 SEP 2025</div><span style="color:#fff">ORMUZ: 90% parado, Brent riesgo 100$<br>RUSIA: 450 drones Moscu, Kapotnia en llamas<br>Novorossiisk para 700k barriles<br>ISRAEL-IRAN: 4 rondas ataques, bases USA atacadas</span></div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="card-title">3. DATOS TIEMPO REAL - LIVE</div></div>', unsafe_allow_html=True)
k1,k2,k3,k4,k5,k6 = st.columns(6)
vix,dvix,_ = get_price_safe("^VIX")
brent,dbrent,tb = get_price_safe(["BZ=F","LCO=F","BNO"])
oro,doro,to = get_price_safe(["GC=F","GLD"])
dxy,ddxy,td = get_price_safe(["DX-Y.NYB","UUP"])
gas,dgas,_ = get_price_safe(["NG=F","UNG"])
spx,dspx,_ = get_price_safe("^GSPC")

k1.metric("VIX", f"{vix:.2f}", f"{dvix:+.2f}")
k2.metric(f"BRENT {tb}", f"{brent:.2f}", f"{dbrent:+.2f}")
k3.metric(f"ORO {to}", f"{oro:.2f}", f"{doro:+.2f}")
k4.metric(f"DXY {td}", f"{dxy:.2f}",
