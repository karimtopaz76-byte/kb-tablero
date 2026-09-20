import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="BK SYSTEM PRO", layout="wide")

st.markdown("""
<style>
.stApp{background:#0a0a0a; color:#fff;}
.card{background:#151515; border:1px solid #2a2a2a; padding:18px; border-radius:12px; margin-bottom:14px;}
.card-title{color:#ff8c00; font-weight:800; font-size:12px; letter-spacing:1.5px; margin-bottom:12px;}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_price(tickers):
    if isinstance(tickers, str):
        tickers=[tickers]
    for tk in tickers:
        try:
            d=yf.Ticker(tk).history(period="5d")
            if len(d)>=2:
                return float(d.Close.iloc[-1]), float(d.Close.iloc[-1]-d.Close.iloc[-2])
        except:
            continue
    return 0.0,0.0

st.title("BK SYSTEM - V10.1 PRO TERMINAL")

cA,cB=st.columns(2)
with cA:
    st.markdown('<div class="card"><div class="card-title">1. FUNDAMENTAL HOY</div>FED Mie 24 Sep 20:00 - 87% subida 25pb<br>CPI 3.1% - Hawkish<br>PCE Vie 26 14:30 clave</div>',unsafe_allow_html=True)
with cB:
    st.markdown('<div class="card"><div class="card-title">2. GEOPOLITICA LIVE 20 SEP</div>ORMUZ 90% parado<br>450 drones Moscu - Kapotnia arde<br>Novorossiisk para 700k<br>4 ataques USA-Iran</div>',unsafe_allow_html=True)

st.markdown('<div class="card"><div class="card-title">3. REAL TIME DATA - LIVE</div></div>',unsafe_allow_html=True)
k1,k2,k3,k4,k5,k6=st.columns(6)
vix,dvix=get_price("^VIX")
brent,dbrent=get_price(["BZ=F","LCO=F","BNO"])
oro,doro=get_price(["GC=F","GLD"])
dxy,ddxy=get_price(["DX-Y.NYB","UUP"])
gas,dgas=get_price("NG=F")
spx,dspx=get_price("^GSPC")

k1.metric("VIX", round(vix,2), round(dvix,2))
k2.metric("BRENT", round(brent,2), round(dbrent,2))
k3.metric("ORO", round(oro,2), round(doro,2))
k4.metric("DXY", round(dxy,2), round(ddxy,2))
k5.metric("GAS", round(gas,2), round(dgas,2))
k6.metric("SPX", round(spx,2), round(dspx,2))

st.markdown('<div class="card"><div class="card-title">4. CALENDARIO 3 ESTRELLAS USA</div></div>',unsafe_allow_html=True)
st.write("Lun 22 18:00 - Lagarde + Goolsbee ***")
st.write("Mar 23 14:45 - PMI Flash ***")
st.write("Mie 24 20:00 - FED + Powell *** CLAVE")
st.write("Jue 25 14:30 - PIB + Jobless + SNB ***")
st.write("Vie 26 14:30 - PCE + Michigan *** Vto Oro 4.5B")

st.markdown('<div class="card"><div class="card-title">5. TECNICO</div></div>',unsafe_allow_html=True)
ta1,ta2=st.columns(2)
with ta1:
    x1=st.checkbox("Nivel D1",key="x1"); x2=st.checkbox("Rechazo H4",key="x2"); x3=st.checkbox("BOS H1",key="x3"); x4=st.checkbox("FVG 15m",key="x4"); x5=st.checkbox("BOS 5m",key="x5")
    st.progress(sum([x1,x2,x3,x4,x5])/5)
    if all([x1,x2,x3,x4,x5]): st.success("XAUUSD READY")
with ta2:
    u1=st.checkbox("Nivel D1 2",key="u1"); u2=st.checkbox("Rechazo H4 2",key="u2"); u3=st.checkbox("BOS H1 2",key="u3"); u4=st.checkbox("FVG 15m 2",key="u4"); u5=st.checkbox("BOS 5m 2",key="u5")
    st.progress(sum([u1,u2,u3,u4,u5])/5)
    if all([u1,u2,u3,u4,u5]): st.success("US02Y READY")

st.markdown('<div class="card"><div class="card-title">6. DIARIO</div></div>',unsafe_allow_html=True)
if "diario" not in st.session_state:
    st.session_state.diario=pd.DataFrame(columns=["Fecha","Inst","Lote","Entrada","Salida"])
ed=st.data_editor(st.session_state.diario, num_rows="dynamic", use_container_width=True)
st.session_state.diario=ed
st.download_button("DESCARGAR", ed.to_csv(index=False), "diario.csv", "text/csv")
