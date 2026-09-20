import streamlit as st
import pandas as pd

st.set_page_config(page_title="BK SYSTEM", layout="wide")

st.title("BK SYSTEM - V7.3 VERDE")

# 1. FUNDAMENTAL
st.info("1. ANALISIS FUNDAMENTAL HOY: Fed 90% subida 25pb miercoles | CPI 3.1% | NFP viernes | VIX 17.5")

# 2. GEOPOLITICA
st.error("2. SITUACION GEOPOLITICA HOY 20 SEP: USA-Iran Ormuz Brent 99.56 | Rusia-Ucrania 450 drones Moscu refineria Kapotnia en llamas | UE 90.000M a Ucrania")

# 3. DATOS
st.warning("3. DATOS TIEMPO REAL: VIX 17.5 | Brent 99.56 | Gas 3.2 | DXY 103.5 (luego conectamos real)")

# 4. CALENDARIO
st.success("4. CALENDARIO 3 ESTRELLAS: Mie 24 Sep FED | Jue 25 PIB | Vie 26 NFP + PCE")

# 5. TECNICO
st.subheader("5. ANALISIS TECNICO")
c1, c2 = st.columns(2)
with c1:
    st.write("XAUUSD")
    x1 = st.checkbox("Nivel D1 S1 N1", key="x1")
    x2 = st.checkbox("Rechazo H4", key="x2")
    x3 = st.checkbox("BOS H1", key="x3")
    x4 = st.checkbox("Retro FVG 15m", key="x4")
    x5 = st.checkbox("BOS 5m", key="x5")
    st.write(f"{sum([x1,x2,x3,x4,x5])}/5")
    if all([x1,x2,x3,x4,x5]):
        st.success("XAUUSD READY")

with c2:
    st.write("US02Y")
    u1 = st.checkbox("Nivel D1 S1 N1 2", key="u1")
    u2 = st.checkbox("Rechazo H4 2", key="u2")
    u3 = st.checkbox("BOS H1 2", key="u3")
    u4 = st.checkbox("Retro FVG 15m 2", key="u4")
    u5 = st.checkbox("BOS 5m 2", key="u5")
    st.write(f"{sum([u1,u2,u3,u4,u5])}/5")
    if all([u1,u2,u3,u4,u5]):
        st.success("US02Y READY")

# 6. DIARIO
st.subheader("6. DIARIO TRADING")
df = pd.DataFrame(columns=["Fecha","Instrumento","Lote","Entrada","Salida"])
st.data_editor(df, num_rows="dynamic", use_container_width=True)
