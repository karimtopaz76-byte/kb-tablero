import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="BK PRO", layout="wide")

@st.cache_data(ttl=300)
def get_price(tickers):
    if isinstance(tickers, str):
        tickers = [tickers]
    for tk in tickers:
        try:
            d = yf.Ticker(tk).history(period="5d")
            if len(d) >= 2:
                last = float(d.Close.iloc[-1])
                prev = float(d.Close.iloc[-2])
                return last, last-prev
        except:
            continue
    return 0.0, 0.0

st.title("BK SYSTEM V11 PRO - FINAL FIX")

st.info("1. FUNDAMENTAL: FED Mie 24 Sep 20:00 - 87pct subida 25pb. CPI 3.1pct.")

st.error("2. GEOPOLITICA LIVE 20 SEP: Ormuz 90pct parado. 450 drones Moscu. Kapotnia en llamas. Novorossiisk 700k.")

st.subheader("3. DATOS TIEMPO REAL")

c1,c2,c3,c4,c5,c6 = st.columns(6)

vix,dvix = get_price("^VIX")
brent,dbrent = get_price(["BZ=F","LCO=F","BNO"])
oro,doro = get_price(["GC=F","GLD"])
dxy,ddxy = get_price(["DX-Y.NYB","UUP"])
gas,dgas = get_price("NG=F")
spx,dspx = get_price("^GSPC")

# METRICS SIN COMILLAS DOBLES ANIDADAS - FIX
c1.metric("VIX", round(vix,2), round(dvix,2))
c2.metric("BRENT", round(brent,2), round(dbrent,2))
c3.metric("ORO", round(oro,2), round(doro,2))
c4.metric("DXY", round(dxy,2), round(ddxy,2))
c5.metric("GAS", round(gas,2), round(dgas,2))
c6.metric("SPX", round(spx,2), round(dspx,2))

st.subheader("4. CALENDARIO 3 ESTRELLAS")
st.write("Lun 22 - Lagarde + Goolsbee")
st.write("Mar 23 14:45 - PMI Flash - 3 estrellas")
st.write("Mie 24 20:00 - FED + Powell - 3 estrellas CLAVE")
st.write("Jue 25 14:30 - PIB + Jobless - 3 estrellas")
st.write("Vie 26 14:30 - PCE + Michigan - 3 estrellas")

st.subheader("5. TECNICO")
a,b = st.columns(2)
with a:
    x1=st.checkbox("Nivel D1",key="x1")
    x2=st.checkbox("Rechazo H4",key="x2")
    x3=st.checkbox("BOS H1",key="x3")
    x4=st.checkbox("FVG 15m",key="x4")
    x5=st.checkbox("BOS 5m",key="x5")
    if all([x1,x2,x3,x4,x5]):
        st.success("XAUUSD READY")
with b:
    u1=st.checkbox("Nivel D1 2",key="u1")
    u2=st.checkbox("Rechazo H4 2",key="u2")
    u3=st.checkbox("BOS H1 2",key="u3")
    u4=st.checkbox("FVG 15m 2",key="u4")
    u5=st.checkbox("BOS 5m 2",key="u5")
    if all([u1,u2,u3,u4,u5]):
        st.success("US02Y READY")

st.subheader("6. DIARIO")
if "diario" not in st.session_state:
    st.session_state.diario = pd.DataFrame(columns=["Fecha","Inst","Lote","Entrada","Salida"])
ed = st.data_editor(st.session_state.diario, num_rows="dynamic", use_container_width=True)
st.session_state.diario = ed
st.download_button("DESCARGAR", ed.to_csv(index=False), "diario.csv", "text/csv")
