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
    df_init = pd.DataFrame(columns=["Fecha","Instrumento","Lote","Entrada","Salida","TP","SL"])

if "diario" not in st.session_state:
    st.session_state.diario = df_init

st.title("BK SYSTEM - V7.2 COMPLETO")
st.markdown("<style>.card{background:#fff;border:1px solid #e5e7eb;padding:14px;border-radius:8px;margin-bottom:10px}.card-title{font-weight:800;font-size:13px;margin-bottom:8px}</style>", unsafe_allow_html=True)

def get_price(ticker):
    try:
        h = yf.Ticker(ticker).history(period="2d")
        return float(h.Close.iloc[-1]), float(h.Close.iloc[-2])
    except:
        return 0.0, 0.0

# 1. FUNDAMENTAL + 2. GEOPOLITICA
cA, cB = st.columns(2)
with cA:
    st.markdown('<div class="card" style="border-left:4px solid #ff3b30"><div class="card-title">1. ANALISIS FUNDAMENTAL HOY</div>Fed: 90% prob subida 25pb miercoles<br>CPI: 3.1% vs objetivo 2%<br>NFP: viernes 26 Sep clave<br>VIX: 17.5 riesgo controlado<br>TIPS: Real Yield alto -> oro presionado</div>', unsafe_allow_html=True)

with cB:
    st.markdown('<div class="card" style="border-left:4px solid #000"><div class="card-title">2. SITUACION GEOPOLITICA HOY - 20 SEP</div>USA-Iran: Tension Ormuz, Brent 99.56<br>Rusia-Ucrania: 450 drones sobre Moscu, refineria Kapotnia en llamas, Duma vota hoy<br>UE: Von der Leyen 90.000M a Ucrania, invierno critico<br>ONU: 130 lideres martes, riesgo escalada</div>', unsafe_allow_html=True)

# 3. DATOS TIEMPO REAL
st.markdown('<div class="card"><div class="card-title">3. DATOS A TIEMPO REAL</div></div>', unsafe_allow_html=True)
c1,c2,c3,c4,c5,c6 = st.columns(6)
tickers = {"VIX":"^VIX","Brent":"BZ=F","Gas":"NG=F","TNX":"^TNX","US02Y":"^IRX","DXY":"DX-Y.NYB"}
for (name,tick),col in zip(tickers.items(), [c1,c2,c3,c4,c5,c6]):
    p,pp = get_price(tick)
    col.metric(name, f"{p:.2f}", f"{p-pp:+.2f}")

# 4. CALENDARIO
st.markdown('<div class="card" style="border-left:4px solid #ffcc00"><div class="card-title">4. CALENDARIO 3 ESTRELLAS USA</div>Mie 24 Sep 20:00 FED decision tipos ***<br>Jue 25 Sep 14:30 PIB USA Q2 ***<br>Vie 26 Sep 14:30 NFP + PCE ***<br>Vie 26: Vencimiento opciones oro 4.5B</div>', unsafe_allow_html=True)

# 5. TECNICO
st.markdown('<div class="card"><div class="card-title">5. ANALISIS TECNICO - CHECKLIST</div></div>', unsafe_allow_html=True)
colA, colB = st.columns(2)
with colA:
    st.subheader("XAUUSD")
    x1 = st.checkbox("Nivel D1 S1 N1", key="x1")
    x2 = st.checkbox("Rechazo H4", key="x2")
    x3 = st.checkbox("BOS H1", key="x3")
    x4 = st.checkbox("Retro FVG 15m", key="x4")
    x5 = st.checkbox("BOS 5m", key="x5")
    if all([x1,x2,x3,x4,x5]):
        st.success("XAUUSD READY - EJECUTAR")
    else:
        st.warning(f"{sum([x1,x2,x3,x4,x5])}/5")

with colB:
    st.subheader("US02Y")
    u1 = st.checkbox("Nivel D1 S1 N1 2", key="u1")
    u2 = st.checkbox("Rechazo H4 2", key="u2")
    u3 = st.checkbox("BOS H1 2", key="u3")
    u4 = st.checkbox("Retro FVG 15m 2", key="u4")
    u5 = st.checkbox("BOS 5m 2", key="u5")
    if all([u1,u2,u3,u4,u5]):
        st.success("US02Y READY")
    else:
        st.warning(f"{sum([u1,u2,u3,u4,u5])}/5")

# 6. DIARIO
st.markdown('<div class="card" style="border-left:4px solid #00a86b"><div class="card-title">6. DIARIO TRADING</div></div>', unsafe_allow_html=True)
edited
