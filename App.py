import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide", page_icon="logo.png")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    .gold-bar { background: #111; color: #FFD60A; text-align: center; padding: 14px; font-weight: bold; border-radius: 8px; margin: 15px 0px; font-size:18px; }
    .block-title { font-size: 22px; font-weight: 900; border-left: 6px solid #111; padding-left: 10px; margin-top: 25px; margin-bottom:10px;}
    .phrase-card { background: #f9f9f9; border-left: 4px solid #FFD60A; padding: 10px 15px; margin: 8px 0px; border-radius: 6px; font-style: italic; font-size:14px;}
    .pillar-box { background: #111; color: white; padding: 12px; border-radius: 8px; text-align: center; font-size: 13px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# HEADER
c1, c2 = st.columns([1,4])
with c1:
    try:
        st.image("logo.png", width=180)
    except:
        st.write("KB")
with c2:
    st.markdown("<h1 style='margin-top:35px; font-weight:900;'>KB VINUELA<br>TRADING</h1>", unsafe_allow_html=True)

# FRASES
st.markdown("<div class='block-title'>MENTALIDAD KB - 6 REGLAS DE AYER</div>", unsafe_allow_html=True)
a, b = st.columns(2)
with a:
    st.markdown("<div class='phrase-card'><b>1. Paciencia:</b> Aprender a cultivar la paciencia.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>2. Enemigos:</b> Aburrimiento, esperanza y miedo.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>3. Proceso:</b> Enfocarse en el proceso, no en resultados.</div>", unsafe_allow_html=True)
with b:
    st.markdown("<div class='phrase-card'><b>4. Afirmacion:</b> Soy mas paciente, centrado, disciplinado.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>5. Mentalidad:</b> Lo que te hara rico es como piensas.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>6. Ejecucion:</b> Actuar sin temor a consecuencias.</div>", unsafe_allow_html=True)

st.markdown("<div class='block-title'>LOS 3 PILARES</div>", unsafe_allow_html=True)
p1, p2, p3 = st.columns(3)
p1.markdown("<div class='pillar-box'>FUNDAMENTAL<br>El POR QUE</div>", unsafe_allow_html=True)
p2.markdown("<div class='pillar-box'>TECNICO<br>El COMO</div>", unsafe_allow_html=True)
p3.markdown("<div class='pillar-box'>PSICOLOGIA<br>El QUIEN</div>", unsafe_allow_html=True)

# RELOJES
tz_sevilla = pytz.timezone('Europe/Madrid')
tz_ny = pytz.timezone('America/New_York')
hora_sev = datetime.now(tz_sevilla).strftime("%H:%M:%S")
hora_ny = datetime.now(tz_ny).strftime("%H:%M:%S")
r1, r2 = st.columns(2)
r1.info(f"SEVILLA: {hora_sev}")
r2.info(f"NY: {hora_ny}")

st.markdown("<div class='gold-bar'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)

colA, colB = st.columns(2)
with colA:
    st.markdown("<div class='block-title'>BLOQUE A - CONTEXTO</div>", unsafe_allow_html=True)
    noticias = st.selectbox("Noticias rojas?", ["No - Verde", "Si - Rojo NO TRADE"])
with colB:
    st.markdown("<div class='block-title'>BLOQUE B - CHECKLIST 5/5</div>", unsafe_allow_html=True)
    s1 = st.checkbox("1. Zona D1/S1/M1")
    s2 = st.checkbox("2. Rechazo 4H")
    s3 = st.checkbox("3. BOS H1")
    s4 = st.checkbox("4. FVG 15m")
    s5 = st.checkbox("5. Confirmacion 5m")
    score = s1+s2+s3+s4+s5
    if score==5 and "No" in noticias:
        st.success(f"SETUP PERFECTO {score}/5")
        st.balloons()
    else:
        st.warning(f"Esperando {score}/5")

st.divider()

# GRAFICOS
st.markdown("<div class='block-title'>GRAFICO XAUUSD 800PX</div>", unsafe_allow_html=True)
components.html("""
<div id="tv_xau" style="height:800px;width:100%"></div>
<script src="https://s3.tradingview.com/tv.js"></script>
<script>
new TradingView.widget({
"autosize": true,
"symbol": "OANDA:XAUUSD",
"interval": "60",
"timezone": "Europe/Madrid",
"theme": "light",
"style": "1",
"locale": "es",
"container_id": "tv_xau"
});
</script>
""", height=820)

st.markdown("<div class='block-title'>DXY 600PX</div>", unsafe_allow_html=True)
components.html("""
<div id="tv_dxy" style="height:600px;width:100%"></div>
<script src="https://s3.tradingview.com/tv.js"></script>
<script>
new TradingView.widget({
"autosize": true,
"symbol": "TVC:DXY",
"interval": "60",
"timezone": "Europe/Madrid",
"theme": "light",
"style": "1",
"locale": "es",
"container_id": "tv_dxy"
});
</script>
""", height=620)
