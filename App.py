import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide", page_icon="logo.png")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    .gold-bar { background: #111; color: #FFD60A; text-align: center; padding: 14px; font-weight: bold; border-radius: 8px; margin: 15px 0px; font-size:18px; letter-spacing:1px;}
    .block-title { font-size: 22px; font-weight: 900; border-left: 6px solid #111; padding-left: 10px; margin-top: 25px; margin-bottom:10px;}
    .phrase-card { background: #f9f9f9; border-left: 4px solid #FFD60A; padding: 10px 15px; margin: 8px 0px; border-radius: 6px; font-style: italic; font-size:14px;}
    .pillar-box { background: #111; color: white; padding: 12px; border-radius: 8px; text-align: center; font-size: 13px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# --- HEADER CON LOGO ---
c_logo, c_title = st.columns([1, 4])
with c_logo:
    try:
        st.image("logo.png", width=180)
    except:
        st.markdown("## KB")
with c_title:
    st.markdown("<h1 style='margin-top:35px; font-weight:900; line-height:0.9;'>KB VINUELA<br>TRADING</h1>", unsafe_allow_html=True)

# --- MENTALIDAD - FRASES DE AYER ---
st.markdown('<div class="block-title">MENTALIDAD KB - 6 REGLAS DE AYER</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="phrase-card"><b>1. Paciencia:</b> Aprender a cultivar la paciencia. El mercado premia al que sabe esperar.</div>', unsafe_allow_html=True)
    st.markdown('<div class="phrase-card"><b>2. Enemigos:</b> El mayor enemigo es el aburrimiento, la esperanza y el miedo.</div>', unsafe_allow_html=True)
    st.markdown('<div class="phrase-card"><b>3. Proceso:</b> Enfocarse en el proceso, no en los resultados.</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="phrase-card"><b>4. Afirmación:</b> Soy más paciente, más centrado, más disciplinado que antes.</div>', unsafe_allow_html=True)
    st.markdown('<div class="phrase-card"><b>5. Mentalidad:</b> Lo que te hará rico es cómo piensas cuando operas.</div>', unsafe_allow_html=True)
    st.markdown('<div class="phrase-card"><b>6. Ejecución:</b> Actuar sin temor a las consecuencias.</div>', unsafe_allow_html=True)

st.markdown('<div class="block-title">LOS 3 PILARES</div>', unsafe_allow_html=True)
p1, p2, p3 = st.columns(3)
p1.markdown('<div class="pillar-box">ANALISIS<br>FUNDAMENTAL<br>El POR QUÉ</div>', unsafe_allow_html=True)
p2.markdown('<div class="pillar-box">ANALISIS<br>TECNICO<br>El CÓMO y CUÁNDO</div>', unsafe_allow_html=True)
p3.markdown('<div class="pillar-box">PSICOLOGIA<br>TRADING<br>El QUIÉN</div>', unsafe_allow_html=True)

# --- RELOJES ---
tz_sevilla = pytz.timezone('Europe/Madrid')
tz_ny = pytz.timezone('America/New_York')
now_sevilla = datetime.now(tz_sevilla).strftime("%H:%M:%S")
now_ny = datetime.now(tz_ny).strftime("%H:%M:%S")
r1, r2 = st.columns(2)
r1.info(f"*SEVILLA: {now_sevilla}*")
r2.info(f"*NUEVA YORK: {now_ny}*")

st.markdown('<div class="gold-bar">REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>', unsafe_allow_html=True)

# --- CHECKLIST ---
colA, colB = st.columns(2)
with colA:
    st.markdown('<div class="block-title">BLOQUE A - CONTEXTO</div>', unsafe_allow_html=True)
    noticias = st.selectbox("¿Hay noticias rojas en 1h?", ["No - Verde, se puede operar", "Si - Rojo, NO TRADE"])
    par = st.selectbox("Par", ["XAUUSD - ORO (Principal)", "EURUSD", "GBPUSD"])

with colB:
    st.markdown('<div class="block-title">BLOQUE B - CHECK
