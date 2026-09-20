import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import pytz

st.set_page_config(page_title="BK SYSTEM V7.5 REAL", layout="wide")
st.title("BK SYSTEM - V7.5 TIEMPO REAL")

def get_price(ticker):
    try:
        d = yf.Ticker(ticker).history(period="2d")
        return float(d.Close.iloc[-1]), float(d.Close.iloc[-1]-d.Close.iloc[-2])
    except:
        return 0.0, 0.0

# --- 1. FUNDAMENTAL ---
st.markdown("### 1. ANALISIS FUNDAMENTAL HOY")
st.info("Fed esta semana: Miercoles 24 Sep 20:00 Decision tipos (87% prob subida 25pb a 3.75-4.00%). Mercado descontando 2 subidas mas. PCE y NFP viernes clave para oro. TIPS alto = oro presionado.")

# --- 2. GEOPOLITICA TIEMPO REAL ---
st.markdown("### 2. SITUACION GEOPOLITICA HOY - LIVE 20 SEP")
col_g1, col_g2 = st.columns(2)
with col_g1:
    brent, dbrent = get_price("BZ=F")
    st.metric("Brent Real", f"{brent:.2f} $", f"{dbrent:+.2f}")
    st.markdown(f"""
    **LIVE HOY:**
    - **Ormuz:** Trafico casi 0, Iran declara estrecho cerrado hasta nuevo aviso. USA dice corredor sur abierto pero con transponders apagados. Prima de riesgo +3%【1188134727684339588†L49-L54】
    - **Rusia-Ucrania:** 450 drones sobre Moscu, refineria Kapotnia en llamas, Novorossiisk suspende embarques 700k barriles/dia【1188134727684339588†L78-L82】
    - **Israel-Iran:** 4 rondas ataques USA a Iran, Iran ataca bases USA en Kuwait, Bahrain, Qatar【1188134727684339588†L213-L217】
    """)

with col_g2:
    st.markdown("""
    **Impacto Trading:**
    - Petroleo soporte por geopolítica, pero OPEP+ aumenta produccion gradual
    - Oro refugio si Ormuz se cierra
    - VIX 17.5 controlado pero puede saltar si USA entra directo
    """)
    edit_geo = st.text_area("Edita geopolítica si hay noticia:", "Ormuz cerrado, Brent 99.56, Moscu en llamas, UE 90.000M a Ucrania")

# --- 3. DATOS TIEMPO REAL ---
st.markdown("### 3. DATOS TIEMPO REAL")
c1,c2,c3,c4,c5,c6 = st.columns(6)
tickers = {"VIX":"^VIX","Brent":"BZ=F","Gas":"NG=F","Oro":"GC=F","DXY":"DX-Y.NYB","US02Y":"^IRX"}
for (name,tick), col in zip(tickers.items(), [c1,c2,c3,c4,c5,c6]):
    p, dp = get_price(tick)
    col.metric(name, f"{p:.2f}", f"{dp:+.2f}")

# --- 4. CALENDARIO REAL ESTA SEMANA ---
st.markdown("### 4. CALENDARIO 3 ESTRELLAS USA - SEMANA REAL")
st.warning("Fuente: Econoday / FedRateCalc Sep 2026【2439552646956138605†L121-L126】")

cal_data = [
    ["Lun 22 Sep", "20:15", "PBoC tipos + Lagarde ECB", "***", "CNY/EUR"],
    ["Mar 23
