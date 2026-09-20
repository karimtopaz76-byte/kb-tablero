import streamlit as st
import yfinance as yf
import pandas as pd
import os
from datetime import datetime
import pytz

st.set_page_config(page_title="BK SYSTEM", layout="wide")

FILE = "/tmp/diario_bk.csv"
if os.path.exists(FILE):
    df_init = pd.read_csv(FILE)
else:
    df_init = pd.DataFrame(columns=["Fecha","Instrumento","Lote","Entrada","Salida","TP","SL"])

if "diario" not in st.session_state:
    st.session_state.diario = df_init

st.title("BK SYSTEM - V7.1 FIX")

def get_price(ticker):
    try:
        h = yf.Ticker(ticker).history(period="2d")
        return float(h.Close.iloc[-1]), float(h.Close.iloc[-2])
    except:
        return 0.0, 0.0

# DATOS
c1,c2,c3,c4,c5,c6 = st.columns(6)
tickers = {"VIX":"^VIX","Brent":"BZ=F","Gas":"NG=F","TNX":"^TNX","US02Y":"^IRX","DXY":"DX-Y.NYB"}
for (name,tick),col in zip(tickers.items(), [c1,c2,c3,c4,c5,c6]):
    p,pp = get_price(tick)
    col.metric(name, f"{p:.2f}", f"{p-pp:+.2f}")

# CHECKLIST
colA, colB = st.columns(2)
with colA:
    st.subheader("XAUUSD")
    x1 = st.checkbox("Nivel D1 S1 N1", key="x1")
    x2 = st.checkbox("Rechazo H4", key="x2")
    x3 = st.checkbox("BOS H1", key="x3")
    x4 = st.checkbox("Retro FVG 15m", key="x4")
    x5 = st.checkbox("BOS 5m", key="x5")
    if all([x1,x2,x3,x4,x5]):
        st.success("XAUUSD READY")
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

# DIARIO
st.subheader("Diario Trading")
edited = st.data_editor(st.session_state.diario, num_rows="dynamic", use_container_width=True)
st.session_state.diario = edited
edited.to_csv(FILE, index=False)
st.download_button("Descargar CSV", edited.to_csv(index=False), "diario.csv", "text/csv")

st.caption(f"OK {datetime.now(pytz.timezone('Europe/Madrid')).strftime('%H:%M:%S')}")
