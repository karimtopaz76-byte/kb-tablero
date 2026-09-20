import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="BK SYSTEM", layout="wide")
st.title("BK SYSTEM - V7.4 REAL")

def get_price(ticker):
    try:
        data = yf.Ticker(ticker).history(period="2d")
        last = float(data.Close.iloc[-1])
        prev = float(data.Close.iloc[-2])
        return last, last-prev
    except:
        return 0.0, 0.0

# 1 y 2
st.info("1. ANALISIS FUNDAMENTAL HOY: Fed 90% subida 25pb miercoles | CPI 3.1% | NFP viernes | VIX 17.5")
st.error("2. GEOPOLITICA 20 SEP: USA-Iran Ormuz Brent 99.56 | Rusia-Ucrania 450 drones Moscu Kapotnia en llamas | UE 90.000M Ucrania")

# 3 DATOS REALES
st.subheader("3. DATOS TIEMPO REAL")
c1,c2,c3,c4 = st.columns(4)
vix, dvix = get_price("^VIX")
brent, dbrent = get_price("BZ=F")
dxy, ddxy = get_price("DX-Y.NYB")
gold, dgold = get_price("GC=F")

c1.metric("VIX", f"{vix:.2f}", f"{dvix:+.2f}")
c2.metric("Brent", f"{brent:.2f}", f"{dbrent:+.2f}")
c3.metric("DXY", f"{dxy:.2f}", f"{ddxy:+.2f}")
c4.metric("ORO", f"{gold:.2f}", f"{dgold:+.2f}")

st.success("4. CALENDARIO 3 ESTRELLAS: Mie 24 Sep FED 20:00 | Jue 25 PIB 14:30 | Vie 26 NFP + PCE 14:30")

# 5 TECNICO
st.subheader("5. ANALISIS TECNICO")
col1, col2 = st.columns(2)
with col1:
    st.write("XAUUSD")
    x1 = st.checkbox("Nivel D1 S1 N1", key="x1")
    x2 = st.checkbox("Rechazo H4", key="x2")
    x3 = st.checkbox("BOS H1", key="x3")
    x4 = st.checkbox("Retro FVG 15m", key="x4")
    x5 = st.checkbox("BOS 5m", key="x5")
    if all([x1,x2,x3,x4,x5]): st.success("XAUUSD READY")
    else: st.warning(f"{sum([x1,x2,x3,x4,x5])}/5")

with col2:
    st.write("US02Y")
    u1 = st.checkbox("Nivel D1 S1 N1 2", key="u1")
    u2 = st.checkbox("Rechazo H4 2", key="u2")
    u3 = st.checkbox("BOS H1 2", key="u3")
    u4 = st.checkbox("Retro FVG 15m 2", key="u4")
    u5 = st.checkbox("BOS 5m 2", key="u5")
    if all([u1,u2,u3,u4,u5]): st.success("US02Y READY")
    else: st.warning(f"{sum([u1,u2,u3,u4,u5])}/5")

# 6 DIARIO
st.subheader("6. DIARIO TRADING")
df = pd.DataFrame(columns=["Fecha","Instrumento","Lote","Entrada","Salida","TP","SL"])
edited = st.data_editor(df, num_rows="dynamic", use_container_width=True)
st.download_button("Descargar Excel", edited.to_csv(index=False), "diario_bk.csv", "text/csv")
