import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="BK SYSTEM PRO", layout="wide", page_icon="📊")

st.markdown("""
<style>
.stApp {background:#0a0a0a;}
.card {background:#151515; border:1px solid #2a2a2a; padding:18px; border-radius:12px; margin-bottom:14px;}
.card-title {color:#ff8c00; font-weight:800; font-size:12px; letter-spacing:1.5px; margin-bottom:12px;}
.big-number {color:#fff; font-size:22px; font-weight:700;}
.small-label {color:#888; font-size:11px;}
.metric-pos {color:#00ff88;}
.metric-neg {color:#ff4444;}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_price(tickers):
    if isinstance(tickers, str):
        tickers = [tickers]
    for tk in tickers:
        try:
            d = yf.Ticker(tk).history(period="5d")
            if len(d) >= 2:
                return float(d.Close.iloc[-1]), float(d.Close.iloc[-1]-d.Close.iloc[-2])
        except:
            continue
    return 0.0, 0.0

# HEADER
st.markdown('<p class="card-title" style="font-size:20px; color:white;">BK TRADING SYSTEM - PROFESSIONAL TERMINAL</p>', unsafe_allow_html=True)

# 1 Y 2
cA,cB = st.columns(2)
with cA:
    st.markdown('<div class="card"><div class="card-title">1. ANALISIS FUNDAMENTAL HOY</div><span style="color:#ddd">FED Miercoles 20:00 - 87% subida 25pb a 3.75%<br>CPI 3.1% YoY - Hawkish<br>PCE Viernes 14:30 clave - 2.9% esperado<br>TIPS Yield alto presiona oro<br>VIX 14.81 - Complacencia</span></div>', unsafe_allow_html=True)
with cB:
    st.markdown('<div class="card"><div class="card-title">2. GEOPOLITICA LIVE - 20 SEP 2025</div><span style="color:#ddd">ORMUZ: Cierre 90% - Brent riesgo 100$<br>RUSIA: 450 drones Moscu, Kapotnia arde<br>Novorossiisk suspende 700k bd<br>ISRAEL-IRAN: 4 ataques USA, Iran ataca bases<br>UE: 90.000M ayuda Ucrania</span></div>', unsafe_allow_html=True)

# 3 - METRICS PRO COMO FOTO
st.markdown('<div class="card"><div class="card-title">3. DATOS TIEMPO REAL - LIVE MARKET</div></div>', unsafe_allow_html=True)
k1,k2,k3,k4,k5,k6 = st.columns(6)
vix,dvix = get_price("^VIX")
brent,dbrent = get_price(["BZ=F","LCO=F","BNO"])
oro,doro = get_price(["GC=F","GLD"])
dxy,ddxy = get_price(["DX-Y.NYB","UUP"])
gas,dgas = get_price(["NG=F","UNG"])
spx,dspx = get_price("^GSPC")

# Usamos texto simple para no romper sintaxis
k1.metric("VIX", round(vix,2), round(dvix,2))
k2.metric("BRENT", round(brent,2), round(dbrent,2))
k3.metric("ORO", round(oro,2), round(doro,2))
k4.metric("DXY", round(dxy,2), round(ddxy,2))
k5.metric("GAS", round(gas,2), round(dgas,2))
k6.metric("SPX", round(spx,2), round(dspx,2))

# 4
st.markdown('<div class="card"><div class="card-title">4. CALENDARIO 3 ESTRELLAS USA - SEMANA 22-26 SEP</div></div>', unsafe_allow_html=True)
df = pd.DataFrame({
" DIA ": ["Lun 22", "Mar 23", "Mie 24", "Jue 25", "Vie 26"],
" HORA CET ": ["18:00", "14:45", "20:00", "14:30", "14:30"],
" EVENTO ": ["Lagarde + Goolsbee", "PMI Flash USA/UE", "FED + Powell - CLAVE", "PIB + Jobless + SNB", "PCE + Michigan"],
" IMPACTO ": ["***", "***", "***", "***", "***"]
})
st.dataframe(df, use_container_width=True, hide_index=True)

# 5
st.markdown('<div class="card"><div class="card-title">5. ANALISIS TECNICO PROFESIONAL</div></div>', unsafe_allow_html=True)
ta1,ta2 = st.columns(2)
with ta1:
    st.write("XAUUSD")
    a1=st.checkbox("Nivel D1 S1 N1",key="a1")
    a2=st.checkbox("Rechazo H4",key="a2")
    a3=st.checkbox("BOS H1",key="a3")
    a4=st.checkbox("FVG 15m",key="a4")
    a5=st.checkbox("BOS 5m",key="a5")
    st.progress(sum([a1,a2,a3,a4,a5])/5)
    if sum([a1,a2,a3,a4,a5])==5:
        st.success("XAUUSD READY - EJECUTAR")
    else:
        st.warning("Esperando setup")
with ta2:
    st.write("US02Y")
    b1=st.checkbox("Nivel D1 S1 N1 2",key="b1")
    b2=st.checkbox("Rechazo H4 2",key="b2")
    b3=st.checkbox("BOS H1 2",key="b3")
    b4=st.checkbox("FVG 15m 2",key="b4")
    b5=st.checkbox("BOS 5m 2",key="b5")
    st.progress(sum([b1,b2,b3,b4,b5])/5)
    if sum([b1,b2,b3,b4,b5])==5:
        st.success("US02Y READY")
    else:
        st.warning("Esperando setup")

# 6
st.markdown('<div class="card"><div class="card-title">6. DIARIO TRADING PROFESIONAL</div></div>', unsafe_allow_html=True)
if "diario" not in st.session_state:
    st.session_state.diario = pd.DataFrame(columns=["Fecha","Instrumento","Lote","Entrada","Salida","TP","SL","Resultado"])
edit = st.data_editor(st.session_state.diario, num_rows="dynamic", use_container_width=True)
st.session_state.diario = edit
st.download_button("DESCARGAR EXCEL PRO", edit.to_csv(index=False), "diario_bk_pro.csv", "text/csv")
