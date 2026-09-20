import streamlit as st
import yfinance as yf
import pandas as pd
import os
from datetime import datetime
import pytz

st.set_page_config(page_title="BK TRADING SYSTEM", layout="wide")

FILE = "/tmp/diario_bk.csv"

if os.path.exists(FILE):
    df_init = pd.read_csv(FILE)
else:
    df_init = pd.DataFrame(columns=["Fecha","Instrumento","Lot size","Precio entrada","Precio salida","TP","SL"])

if "diario" not in st.session_state:
    st.session_state.diario = df_init

st.markdown("<style>.card{background:#fff;border:1px solid #e5e7eb;padding:14px;border-radius:8px;margin-bottom:10px}.card-title{font-weight:800;font-size:13px;margin-bottom:8px}</style>", unsafe_allow_html=True)

st.markdown("## BK SYSTEM — V7 FIX")

def get_price(ticker):
    try:
        h = yf.Ticker(ticker).history(period="2d")
        return float(h.Close.iloc[-1]), float(h.Close.iloc[-2])
    except:
        return 0.0, 0.0

col1, col2 = st.columns([1,1])
with col1:
    st.markdown('<div class="card" style="border-left:4px solid #ff3b30"><div class="card-title">1. ANALISIS FUNDAMENTAL</div>Fed 90% subida 25pb miercoles<br>CPI 3.1% | NFP viernes<br>VIX 17.5</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card" style="border-left:4px solid #000"><div class="card-title">2. GEOPOLITICA HOY</div>USA-Iran Ormuz $99.56<br>Rusia-Ucrania 450 drones Moscu<br>Duma vota hoy</div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="card-title">3. DATOS TIEMPO REAL</div></div>', unsafe_allow_html=True)
c1,c2,c3,c4,c5,c6 = st.columns(6)
tickers = {"VIX":"^VIX","Brent":"BZ=F","Nat Gas":"NG=F","TIPS":"^TNX","US02Y":"^IRX","DXY":"DX-Y.NYB"}
cols = [c1,c2,c3,c4,c5,c6]
for (name, tick), col in zip(tickers.items(), cols):
    p, pp = get_price(tick)
    col.metric(name, f"{p:.2f}", f"{p-pp:+.2f}")

st.markdown('<div class="card" style="border-left:4px solid #ffcc00"><div class="card-title">4. CALENDARIO 3 ESTRELLAS USA</div>Mie 24 Sep 20:00 FED<br>Jue 25 Sep 14:30 PIB USA<br>Vie 26 Sep 14:30 NFP + PCE</div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="card-title">5. ANALISIS TECNICO</div></div>', unsafe_allow_html=True)
cc1, cc2 = st.columns(2)
with cc1:
    st.markdown("**CHECKLIST XAUUSD**")
    x1 = st.checkbox("Nivel D1,S1,N1", key="x1")
    x2 = st.checkbox("Rechazo H4", key="x2")
    x3 = st.checkbox("BOS H1", key="x3")
    x4 = st.checkbox("Retraso a FVG 15m", key="x4")
    x5 = st.checkbox("BOS 5m", key="x5")
    if all([x1,x2,x3,x4,x5]):
        st.success("XAUUSD READY")
    else:
        st.warning(f"{sum([x1,x2,x3,x4,x5])}/5")

with cc2:
    st.markdown("**CHECKLIST US02Y**")
    u1 = st.checkbox("Nivel D1,S1,N1 ", key="u1")
    u2 = st.checkbox("Rechazo H4 ", key="u2")
    u3 = st.checkbox("BOS H1 ", key="u3")
    u4 = st.checkbox("Retras
