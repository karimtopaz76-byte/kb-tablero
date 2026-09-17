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
        st.title("KB")
with c2:
    st.markdown("<h1 style='margin-top:35px; font-weight:900;'>KB VINUELA<br>TRADING</h1>", unsafe_allow_html=True)

# MENTALIDAD
st.markdown("<div class='block-title'>MENTALIDAD KB - 6 REGLAS</div>", unsafe_allow_html=True)
a, b = st.columns(2)
with a:
    st.markdown("<div class='phrase-card'><b>1. Paciencia:</b> Aprender a cultivar la paciencia.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>2. Enemigos:</b> Aburrimiento, esperanza y miedo.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>3. Proceso:</b> Enfocarse en el proceso, no en resultados.</div>", unsafe_allow_html=True)
with b:
    st.markdown("<div class='phrase-card'><b>4. Afirmacion:</b> Soy mas paciente, centrado, disciplinado.</div>", unsafe_allow_html=True)
    st
