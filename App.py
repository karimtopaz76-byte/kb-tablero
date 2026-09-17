import streamlit as st
from datetime import datetime
import pytz

# --- KB VINUELA - VERSION FONDO BLANCO LECTURA FACIL ---
st.set_page_config(page_title="KB VINUELA TRADING", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    h1 { color: #000000 !important; font-weight: 900 !important; text-align: center; font-size: 42px !important; }
    .subtitulo { color: #555555; text-align: center; font-size: 16px; margin-bottom: 30px; }
    .bloque { 
        color: #000000 !important; 
        font-size: 26px; 
        font-weight: 900; 
        margin-top: 30px; 
        border-left: 6px solid #000000;
        padding-left: 12px;
    }
    label, p, .stCheckbox label { color: #000000 !important; font-size: 16px !important; }
    .caja-espera { background-color: #FFF3CD; color: #000000; padding: 18px; border-radius: 8px; font-weight: bold; border: 2px solid #FFC107; text-align: center; margin-top: 20px; }
    .caja-ok { background-color: #D4EDDA; color: #000000; padding: 18px; border-radius: 8px; font-weight: bold; border: 2px solid #28A745; text-align: center; margin-top: 20px; }
    .caja-no { background-color: #F8D7DA; color: #000000; padding: 18px; border-radius: 8px; font-weight: bold; border: 2px solid #DC3545; text-align: center; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

try:
    sevilla_tz = pytz.timezone('Europe/Madrid')
    ahora_sev = datetime.now(sevilla_tz).strftime("%H:%M")
except:
    ahora_sev = datetime.now().strftime("%H:%M")

st.markdown("<h1>KB VINUELA TRADING</h1>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitulo'>Sevilla {ahora_sev} | NY 10:00-13:00</div>", unsafe_allow_html=True)

st.markdown('<div class="bloque">BLOQUE A</div>', unsafe_allow_html=True)
noticias = st.selectbox("Noticias rojas?", ["No - Verde", "Si - Hay rojas, no operar", "Precaucion"])

st.markdown('<div class="bloque">BLOQUE B - 5 pasos</div>', unsafe_allow_html=True)
c1 = st.checkbox("1. Zona azul 6m tocada")
c2 = st.checkbox("2. Rechazo H4")
c3 = st.checkbox("3. BOS H1")
c4 = st.checkbox("4. FVG 15m")
c5 = st.checkbox("5. SL puesto")

checks = sum([c1,c2,c3,c4,c5])

if noticias != "No - Verde":
    st.markdown('<div class="caja-no">⛔ NO OPERAR - Noticias rojas</div>', unsafe_allow_html=True)
elif checks == 5:
    st.markdown('<div class="caja-ok">✅ SETUP VALIDO - PUEDES ENTRAR</div>', unsafe_allow_html=True)
    st.balloons()
else:
    st.markdown(f'<div class="caja-espera">Esperando setup ({checks}/5)</div>', unsafe_allow_html=True)
