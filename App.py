import streamlit as st
from datetime import datetime
import pytz
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    h1 { color: #000000 !important; font-weight: 900 !important; text-align: center; margin-bottom: 0px; }
    .regla-oro { background-color: #000000; color: #FFD60A !important; padding: 12px; border-radius: 8px; text-align: center; font-weight: 900; font-size: 18px; margin: 15px 0px; }
    .bloque { color: #000000 !important; font-size: 20px; font-weight: 900; margin-top: 20px; border-left: 6px solid #000000; padding-left: 10px; }
    .reloj { background-color: #F0F0F0; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #DDD; font-weight: bold; }
    .caja-ok { background-color: #D4EDDA; color: #000000; padding: 15px; border-radius: 8px; font-weight: bold; border: 2px solid #28A745; text-align: center; margin-top: 15px; font-size: 18px; }
    .caja-espera { background-color: #FFF3CD; color: #000000; padding: 15px; border-radius: 8px; font-weight: bold; border: 2px solid #FFC107; text-align: center; margin-top: 15px; }
    .caja-no { background-color: #F8D7DA; color: #000000; padding: 15px; border-radius: 8px; font-weight: bold; border: 2px solid #DC3545; text-align: center; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

if 'bitacora' not in st.session_state:
    st.session_state.bitacora = []

# --- LOGO + TITULO ---
col_logo, col_titulo = st.columns([1,4])
with col_logo:
    # Si subes un archivo logo.png a GitHub, lo mostrará. Si no, muestra KB
    try:
        st.image("logo.png", width=100)
    except:
        st.markdown("<h1 style='font-size:50px; margin:0px;'>KB</h1>", unsafe_allow_html=True)
with col_titulo:
    st.markdown("<h1>KB VINUELA TRADING</h1>", unsafe_allow_html=True)

# --- RELOJES ---
sevilla_tz = pytz.timezone('Europe/Madrid')
ny_tz = pytz.timezone('America/New_York')
ahora_sev = datetime.now(sevilla_tz)
ahora_ny = datetime.now(ny_tz)

c1, c2, c3 = st.columns([2,2,1])
with c1:
    st.markdown(f"<div class='reloj'>Sevilla: {ahora_sev.strftime('%H:%M:%S')}</div>", unsafe_allow_html=True)
with c2:
    ny_text = "NY: " + ahora_ny.strftime('%H:%M:%S')
    if 10 <= ahora_ny.hour < 13:
        ny_text += " 🟢 EN VIVO"
    st.markdown(f"<div class='reloj'>{ny_text}</div>", unsafe_allow_html=True)
with c3:
    if st.button("🔄 RESET"):
        st.session_state.clear()
        st.rerun()

st.markdown("<div class='regla-oro'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)

# --- BLOQUES ---
colA, colB = st.columns(2)
with colA:
    st.markdown('<div class="bloque">BLOQUE A</div>', unsafe_allow_html=True)
    noticias = st.selectbox("Noticias rojas?", ["No - Verde", "Si - Hay rojas, no operar", "Precaucion"])
    par = st.selectbox("Par", ["XAUUSD - ORO", "DXY", "EURUSD", "GBPUSD"])
with colB:
    st.markdown('<div class="bloque">BLOQUE B - 5 pasos KB</div>', unsafe_allow_html=True)
    b1 = st.checkbox("1. Zona de interes D1/S1/M1")
    b2 = st.checkbox("2. Rechazo vela 4H con cierre bajo zona interes")
    b3 = st.checkbox("3. BOS H1")
    b4 = st.checkbox("4. Retraso al FVG 15m")
    b5 = st.checkbox("5. Confirmacion entrada en 5m")

checks = sum([b1,b2,b3,b4,b5])

if noticias != "No - Verde":
    st.markdown('<div class="caja-no">⛔ NO OPERAR - Noticias rojas</div>', unsafe_allow_html=True)
elif checks == 5:
    st.markdown('<div class="caja-ok">✅ SETUP VALIDO 5/5 - PUEDES ENTRAR</div>', unsafe_allow_html=True)
    st.balloons()
else:
    st.markdown(f'<div class="caja-espera">Esperando setup ({checks}/5)</div>', unsafe_allow_html=True)

# --- GRAFICOS TRADINGVIEW ---
st.markdown("---")
st.markdown('<div class="bloque">GRAFICOS EN VIVO - TRADING…
