import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="BK SYSTEM V14 COMPLETA", layout="wide")
st.markdown("<style>.stApp{background:#0e1117;color:#e0e0e0}h1,h2,h3{color:#00ff88!important}div[data-testid='metric']{background:#1a1d26;border:1px solid #00ff88;border-radius:10px;padding:10px}</style>", unsafe_allow_html=True)

st.title("BK SYSTEM V14 - COMPLETA PROFESIONAL")
st.caption("FUNDAMENTAL + GEOPOLITICA + LIVE + CALENDARIO + TECNICO + DIARIO - 20 SEP 2026")

@st.cache_data(ttl=300)
def get_price(tickers):
    if isinstance(tickers, str): tickers=[tickers]
    for tk in tickers:
        try:
            d=yf.Ticker(tk).history(period="5d")
            if len(d)>=2:
                return float(d["Close"].iloc[-1]), float(d["Close"].iloc[-1]-d["Close"].iloc[-2])
        except: continue
    return 0.0,0.0

cF,cG=st.columns(2)
with cF:
    st.subheader("1. FUNDAMENTAL HOY")
    st.write("- FED Mie 24 Sep 20:00 - 87% 25pb")
    st.write("- CPI 3.1% vs 2% - Hawkish")
    st.write("- PCE Vie 26 Sep 14:30 clave")
with cG:
    st.subheader("2. GEOPOLITICA LIVE")
    st.write("- Ormuz 90% parado - Brent 100 riesgo")
    st.write("- Rusia 450 drones - Kapotnia en llamas")
    st.write("- Novorossiisk 700k parados")

st.divider()
st.subheader("3. MERCADO EN VIVO")
k1,k2,k3,k4,k5,k6=st.columns(6)
vix,dvix=get_price("^VIX")
brent,dbr=get_price(["BZ=F","BNO"])
oro,doro=get_price(["GC=F","GLD"])
dxy,ddxy=get_price(["DX-Y.NYB","UUP"])
gas,dgas=get_price("NG=F")
spx,dsp=get_price("^GSPC")
k1.metric("VIX",round(vix,2),round(dvix,2))
k2.metric("BRENT",round(brent,2),round(dbr,2))
k3.metric("ORO",round(oro,2),round(doro,2))
k4.metric("DXY",round(dxy,2),round(ddxy,2))
k5.metric("GAS",round(gas,2),round(dgas,2))
k6.metric("SPX",round(spx,2),round(dsp,2))

st.divider()
st.subheader("4. CALENDARIO 3 ESTRELLAS")
st.table(pd.DataFrame([["Lun 22 18:00","Lagarde+Goolsbee","2*"],["Mar 23 14:45","PMI Flash USA/UE/UK","3*"],["Mie 24 20:00","FED + Powell","CLAVE"],["Jue 25 14:30","PIB+Jobless+SNB+BoE","3*"],["Vie 26 14:30","PCE+Michigan","3* CLAVE ORO"]],columns=["Fecha","Evento","Impacto"]))

st.divider()
st.subheader("5. TECNICO CHECKLIST")
a,b=st.columns(2)
with a:
    st.write("XAUUSD")
    x1=st.checkbox("Nivel D1",key="x1"); x2=st.checkbox("Rechazo H4",key="x2"); x3=st.checkbox("BOS H1",key="x3"); x4=st.checkbox("FVG 15m",key="x4"); x5=st.checkbox("BOS 5m",key="x5")
    if all([x1,x2,x3,x4,x5]): st.success("XAUUSD READY 5/5")
with b:
    st.write("US02Y")
    u1=st.checkbox("Nivel D1 2",key="u1"); u2=st.checkbox("Rechazo H4 2",key="u2"); u3=st.checkbox("BOS H1 2",key="u3"); u4=st.checkbox("FVG 15m 2",key="u4"); u5=st.checkbox("BOS 5m 2",key="u5")
    if all([u1,u2,u3,u4,u5]): st.success("US02Y READY 5/5")

st.divider()
st.subheader("6. DIARIO")
if "diario" not in st.session_state: st.session_state.diario=pd.DataFrame(columns=["Fecha","Inst","Lote","Entrada","Salida","Resultado"])
ed=st.data_editor(st.session_state.diario,num_rows="dynamic",use_container_width=True)
st.session_state.diario=ed
st.download_button("DESCARGAR CSV",ed.to_csv(index=False),"diario_bk_v14.csv")
st.success("V14 COMPLETA CARGADA - VERDE GARANTIZADO")
