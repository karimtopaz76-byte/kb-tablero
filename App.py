import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import pytz

st.set_page_config(page_title="BK SYSTEM", layout="wide")
st.title("BK SYSTEM - V7.6 REAL FIX")

def get_price(ticker):
    try:
        d = yf.Ticker(ticker).history(period="2d")
        return float(d.Close.iloc[-1]), float(d.Close.iloc[-1]-d.Close.iloc[-2])
    except:
        return 0.0, 0.0

# 1
st.info("1. FUNDAMENTAL HOY: Fed Miercoles 20:00 decision tipos 87pct subida 25pb. PCE y NFP viernes clave.")

# 2
st.error("2. GEOPOLITICA LIVE 20 SEP: Ormuz cerrado, Brent sube 3pct. Rusia-Ucrania 450 drones Moscu, refineria Kapotnia en llamas, Novorossiisk para embarques. Iran ataca bases USA.")

# 3
st.subheader("3. DATOS TIEMPO REAL")
c1,c2,c3,c4 = st.columns(4)
vix,d1 = get_price("^VIX")
brent,d2 = get_price("BZ=F")
oro,d3 = get_price("GC=F")
dxy,d4 = get_price("DX-Y.NYB")
c1.metric("VIX", f"{vix:.2f}", f"{d1:+.2f}")
c2.metric("Brent", f"{brent:.2f}", f"{d2:+.2f}")
c3.metric("Oro", f"{oro:.2f}", f"{d3:+.2f}")
c4.metric("DXY", f"{dxy:.2f}", f"{d4:+.2f}")

# 4 - CALENDARIO SIN LISTAS, A PRUEBA DE WHATSAPP
st.subheader("4. CALENDARIO 3 ESTRELLAS USA - SEMANA REAL")
st.write("Lun 22 Sep - Lagarde ECB + Goolsbee Fed")
st.write("Mar 23 Sep 14:45 - PMI Flash USA UE UK - 3 estrellas")
st.write("Mie 24 Sep 20:00 - FED DECISION TIPOS + Powell 20:30 - 3 estrellas - CLAVE SEMANA")
st.write("Jue 25 Sep 14:30 - PIB USA Q2 + Jobless Claims + SNB + BoE - 3 estrellas")
st.write("Vie 26 Sep 14:30 - PCE Inflacion + Durable Goods + Michigan - 3 estrellas - Vencimiento oro 4.5B")

# 5
st.subheader("5. TECNICO")
a,b = st.columns(2)
with a:
    x1=st.checkbox("Nivel D1",key="x1")
    x2=st.checkbox("Rechazo H4",key="x2")
    x3=st.checkbox("BOS H1",key="x3")
    x4=st.checkbox("FVG 15m",key="x4")
    x5=st.checkbox("BOS 5m",key="x5")
    if all([x1,x2,x3,x4,x5]): st.success("XAUUSD READY")
    else: st.warning(f"{sum([x1,x2,x3,x4,x5])}/5")
with b:
    u1=st.checkbox("Nivel D1 2",key="u1")
    u2=st.checkbox("Rechazo H4 2",key="u2")
    u3=st.checkbox("BOS H1 2",key="u3")
    u4=st.checkbox("FVG 15m 2",key="u4")
    u5=st.checkbox("BOS 5m 2",key="u5")
    if all([u1,u2,u3,u4,u5]): st.success("US02Y READY")
    else: st.warning(f"{sum([u1,u2,u3,u4,u5])}/5")

# 6
st.subheader("6. DIARIO")
df = pd.DataFrame(columns=["Fecha","Inst","Lote","Entrada","Salida"])
st.data_editor(df, num_rows="dynamic", use_container_width=True)

st.caption("BK V7.6 FIX")
