import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide", page_icon="logo.png")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    .gold-bar { background: #111; color: #FFD60A; text-align: center; padding: 12px; font-weight: bold; border-radius: 8px; margin: 10px 0px; letter-spacing: 1px; }
    .block-title { font-size: 22px; font-weight: 900; border-left: 6px solid #111; padding-left: 10px; margin-top: 20px;}
    .phrase-card { background: #f9f9f9; border-left: 4px solid #FFD60A; padding: 10px 15px; margin: 8px 0px; border-radius: 6px; font-style: italic; }
    .pillar-box { background: #111; color: white; padding: 15px; border-radius: 8px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
c_logo, c_title = st.columns([1, 3])
with c_logo:
    st.image("logo.png", width=180)
with c_title:
    st.markdown("<h1 style='margin-top:30px; font-weight:900;'>KB VINUELA<br>TRADING</h1>", unsafe_allow_html=True)

# --- FRASES DE AYER - EN LA PARTE BLANCA ---
st.markdown('<div class="block-title">MENTALIDAD KB - 6 REGLAS</div>', unsafe_allow_html=True)

st.markdown('<div class="phrase-card"><b>1. Paciencia:</b> Aprender a cultivar la paciencia. El mercado premia al que sabe esperar.</div>', unsafe_allow_html=True)
st.markdown('<div class="phrase-card"><b>2. Enemigos:</b> El mayor enemigo es el aburrimiento, la esperanza y el miedo.</div>', unsafe_allow_html=True)
st.markdown('<div class="phrase-card"><b>3. Proceso:</b> Enfocarse en el proceso, no en los resultados. El dinero viene solo.</div>', unsafe_allow_html=True)
st.markdown('<div class="phrase-card"><b>4. Afirmación:</b> Soy más paciente, más centrado, más disciplinado que antes.</div>', unsafe_allow_html=True)
st.markdown('<div class="phrase-card"><b>5. Mentalidad:</b> Lo que te hará rico es cómo piensas cuando operas.</div>', unsafe_allow_html=True)
st.markdown('<div class="phrase-card"><b>6. Ejecución:</b> Actuar sin temor a las consecuencias. Operar con plan.</div>', unsafe_allow_html=True)

# --- 3 PILARES ---
st.markdown('<div class="block-title">3 PILARES ESENCIALES</div>', unsafe_allow_html=True)
p1, p2, p3 = st.columns(3)
p1.markdown('<div class="pillar-box"><b>FUNDAMENTAL</b><br>El POR QUÉ se mueve</div>', unsafe_allow_html=True)
p2.markdown('<div class="pillar-box"><b>TÉCNICO</b><br>El CÓMO y CUÁNDO</div>', unsafe_allow_html=True)
p3.markdown('<div class="pillar-box"><b>PSICOLOGÍA</b><br>El QUIÉN eres tú</div>', unsafe_allow_html=True)

# --- RELOJES ---
tz_sevilla = pytz.timezone('Europe/Madrid')
tz_ny = pytz.timezone('America/New_York')
now_sevilla = datetime.now(tz_sevilla).strftime("%H:%M:%S")
now_ny = datetime.now(tz_ny).strftime("%H:%M:%S")
c1, c2 = st.columns(2)
c1.info(f"*Sevilla: {now_sevilla}*")
c2.info(f"*NY: {now_ny}*")

st.markdown('<div class="gold-bar">REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>', unsafe_allow_html=True)

# --- BLOQUE A y B (tu checklist) ---
colA, colB = st.columns(2)
with colA:
    st.markdown('<div class="block-title">BLOQUE A</div>', unsafe_allow_html=True)
    noticias = st.selectbox("Noticias rojas?", ["No - Verde", "Si - Rojo, NO TRADE"])
with colB:
    st.markdown('<div class="block-title">BLOQUE B - 5/5</div>', unsafe_allow_html=True)
    s1 = st.checkbox("1. Zona de interes D1/S1/M1")
    s2 = st.checkbox("2. Rechazo vela 4H")
    s3 = st.checkbox("3. BOS H1")
    s4 = st.checkbox("4. Retraso al FVG 15m")
    s5 = st.checkbox("5. Confirmacion 5m")
    score = sum([s1,s2,s3,s4,s5])
    if score == 5 and noticias == "No - Verde":
        st.success(f"SETUP PERFECTO ({score}/5)")
    else:
        st.warning(f"Esperando ({score}/5)")
