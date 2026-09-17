import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VIÑUELA TRADING - PRO DESK", layout="wide", page_icon="👑")

# CSS LUJO ORO NEGRO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&display=swap');
.stApp { background: #0A0A0A; color: white; }
h1,h2,h3 { font-family: 'Montserrat', sans-serif; }
.gold { color: #FFD60A; }
.card {
    background: #151515;
    border: 1px solid #2a2a2a;
    border-radius: 16px;
    padding: 18px;
}
.gold-bar {
    background: linear-gradient(90deg, #FFD60A, #FFB700);
    color: #111;
    text-align: center;
    padding: 12px;
    font-weight: 900;
    border-radius: 10px;
    letter-spacing: 1px;
    font-size: 15px;
}
.frase-box {
    background: #1A1A1A;
    border-left: 4px solid #FFD60A;
    padding: 12px 16px;
    border-radius: 8px;
    font-style: italic;
    color: #ccc;
}
</style>
""", unsafe_allow_html=True)

FRASES = [
    "El mercado te pagará por tu disciplina, no por tus ganas.",
    "Sin 5/5 no hay trade. Sin paciencia no hay cuenta.",
    "Hoy no necesitas operar, necesitas no arruinarte.",
    "Un francotirador espera horas por un solo disparo perfecto.",
    "Tu trabajo no es adivinar, es esperar y ejecutar.",
    "El oro recompensa al paciente y castiga al ansioso.",
    "Protege el capital. El beneficio es consecuencia.",
    "Menos es más. Un trade bueno al día te hace libre.",
]

if 'frase' not in st.session_state:
    st.session_state.frase = random.choice(FRASES)

# HEADER
c_logo, c_title, c_clock = st.columns([1,3,1.2])
with c_logo:
    try: st.image("logo.png", width=110)
    except: st.markdown("<h2 class='gold'>KB</h2>", unsafe_allow_html=True)
with c_title:
    st.markdown("<h1 style='margin:0;line-height:0.9'>KB VIÑUELA<br><span class='gold'>TRADING DESK</span></h1>", unsafe_allow_html=True)
    st.markdown("<div class='gold-bar'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)
with c_clock:
    hora = datetime.now(pytz.timezone('Europe/Madrid')).strftime("%H:%M:%S")
    st.markdown(f"<div class='card' style='text-align:center'><small>MADRID</small><h2 style='margin:0'>{hora}</h2><small class='gold'>MERCADO ABIERTO</small></div>", unsafe_allow_html=True)
    if st.button("🔄 Nueva frase"): 
        st.session_state.frase = random.choice(FRASES)
        st.rerun()

st.markdown(f"<div class='frase-box'>💭 <b>FRASE PRO:</b> {st.session_state.frase}</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# PRECIOS EN VIVO
p1,p2,p3 = st.columns(3)
with p1:
    st.markdown("*XAUUSD - ORO*")
    components.html("""<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"OANDA:XAUUSD","width":"100%","height":120,"locale":"es","colorTheme":"dark","isTransparent":true}</script></div>""", height=125)
with p2:
    st.markdown("*DXY - DOLAR (Enemigo del oro)*")
    components.html("""<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"TVC:DXY","width":"100%","height":120,"locale":"es","colorTheme":"dark","isTransparent":true}</script></div>""", height=125)
with p3:
    st.markdown("*US10Y - Bonos (Miedo del mercado)*")
    components.html("""<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"TVC:US10Y","width":"100%","height":120,"locale":"es","colorTheme":"dark","isTransparent":true}</script></div>""", height=125)

# TORRE DE CONTROL
st.divider()
t1,t2,t3 = st.columns([1,1.2,1])

with t1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("*🎯 SESIÓN Y TENDENCIA*")
    d1 = st.selectbox("DIARIO D1", ["ALCISTA 🟢","BAJISTA 🔴","LATERAL ⚪"], key="d1")
    h4 = st.selectbox("H4", ["ALCISTA 🟢","BAJISTA 🔴","LATERAL ⚪"], key="h4")
    sesion = st.selectbox("Sesión", ["LONDRES 🔥 (Mejor para oro)","NEW YORK 🔥🔥 (Más volatil)","ASIA 💤 (No operar)"])
    if "ALCISTA" in d1 and "ALCISTA" in h4:
        st.success("BIAS: SOLO COMPRAS")
    elif "BAJISTA" in d1 and "BAJISTA" in h4:
        st.error("BIAS: SOLO VENTAS")
    else:
        st.warning("BIAS: ESPERA - SIN ALINEACIÓN")
    st.markdown("</div>", unsafe_allow_html=True)

with t2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("*✅ CHECKLIST FRANCOTIRADOR 5/5*")
    c1 = st.checkbox("1. D1 + H4 alineados y claros")
    c2 = st.checkbox("2. Barrido de liquidez / SL cazados")
    c3 = st.checkbox("3. BOS / CHoCH en M15 confirmado")
    c4 = st.checkbox("4. Entrada en FVG / Order Block premium")
    c5 = st.checkbox("5. RR 1:2.5 mínimo + SL lógico")
    tot = sum([c1,c2,c3,c4,c5])
    st.progress(tot/5)
    if tot==5:
        st.balloons()
        st.markdown("<h3 style='color:#FFD60A;text-align:center'>🔥 5/5 - MODO FRANCOTIRADOR ACTIVADO</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<center>{tot}/5 - No toques el ratón</center>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with t3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("*💰 GESTIÓN PRO*")
    bal = st.number_input("Balance $", value=1000, step=100)
    riesgo = st.slider("Riesgo por trade %", 0.5, 3.0, 1.0)
    sl = st.number_input("SL en $ de oro", value=2.5)
    if sl>0:
        lote = (bal*riesgo/100)/(sl*100)
        st.metric("Lote XAUUSD", f"{lote:.2f}", f"${bal*riesgo/100:.0f} riesgo")
    estado = st.select_slider("Estado mental", ["TILT 😡","Ansioso 😬","Neutral 😐","Enfocado 🧠","En la zona 🔥"], value="Enfocado 🧠")
    if "TILT" in estado or "Ansioso" in estado:
        st.error("NO OPERES. Ve a caminar 10 min.")
    st.markdown("</div>", unsafe_allow_html=True)

# JOURNAL + GRAFICO
st.divider()
j1,j2 = st.columns([1.1,2])

with j1:
    st.markdown("*📂 DIARIO DE TRADING*")
    try:
        tmp = pd.read_excel("trading.xlsx", header=None)
        fila=0
        for i in range(len(tmp)):
            if "Fecha" in str(tmp.iloc[i].values): fila=i; break
        df = pd.read_excel("trading.xlsx", header=fila)
        df = df.dropna(how='all')
        df = df.loc[:, ~df.columns.astype(str).str.contains('Unnamed', na=False)]
        st.dataframe(df, use_container_width=True, height=620)
    except Exception as e:
        st.warning(f"Sube tu trading.xlsx - {e}")
        st.dataframe(pd.DataFrame({"Fecha":["HOY"],"Par":["XAUUSD"],"Nota":["Esperar 5/5"]}), use_container_width=True)

with j2:
    st.markdown("### 📈 XAUUSD - CAMPO DE BATALLA")
    components.html("""<div id="kb_xau_final_pro" style="height:640px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"15","timezone":"Europe/Madrid","theme":"dark","style":"1","container_id":"kb_xau_final_pro","hide_side_toolbar":false})</script>""", height=650)

st.markdown("### 📉 DXY - TERMÓMETRO DEL DÓLAR")
components.html("""<div id="kb_dxy_final_pro" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"TVC:DXY","interval":"60","timezone":"Europe/Madrid","theme":"dark","container_id":"kb_dxy_final_pro"})</script>""", height=520)

st.markdown("<br><center><small style='color:#555'>KB VIÑUELA TRADING © 2026 - Hecho para traders con disciplina, no con suerte.</small></center>", unsafe_allow_html=True)
