import streamlit as st
from datetime import datetime, timedelta
import pytz
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide", page_icon="📈")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    h1 { color: #000000 !important; font-weight: 900 !important; text-align: center; font-size: 38px !important; }
    .regla-oro { background-color: #000000; color: #FFD60A !important; padding: 12px; border-radius: 8px; text-align: center; font-weight: 900; font-size: 18px; margin: 15px 0px; }
    .bloque { color: #000000 !important; font-size: 24px; font-weight: 900; margin-top: 25px; border-left: 6px solid #000000; padding-left: 12px; }
    label, p { color: #000000 !important; }
    .caja-espera { background-color: #FFF3CD; color: #000000; padding: 16px; border-radius: 8px; font-weight: bold; border: 2px solid #FFC107; text-align: center; margin-top: 15px; }
    .caja-ok { background-color: #D4EDDA; color: #000000; padding: 16px; border-radius: 8px; font-weight: bold; border: 2px solid #28A745; text-align: center; margin-top: 15px; font-size: 19px; }
    .caja-no { background-color: #F8D7DA; color: #000000; padding: 16px; border-radius: 8px; font-weight: bold; border: 2px solid #DC3545; text-align: center; margin-top: 15px; }
    .reloj { background-color: #F0F0F0; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #DDD; }
</style>
""", unsafe_allow_html=True)

if 'c1' not in st.session_state: st.session_state.c1 = False
if 'c2' not in st.session_state: st.session_state.c2 = False
if 'c3' not in st.session_state: st.session_state.c3 = False
if 'c4' not in st.session_state: st.session_state.c4 = False
if 'c5' not in st.session_state: st.session_state.c5 = False
if 'bitacora' not in st.session_state: st.session_state.bitacora = []

try:
    st.image("logo.png", width=150)
except:
    pass

st.markdown("<h1>KB VINUELA TRADING</h1>", unsafe_allow_html=True)

sevilla_tz = pytz.timezone('Europe/Madrid')
ny_tz = pytz.timezone('America/New_York')
ahora_sev = datetime.now(sevilla_tz)
ahora_ny = datetime.now(ny_tz)
ny_inicio = ahora_ny.replace(hour=10, minute=0, second=0, microsecond=0)
ny_fin = ahora_ny.replace(hour=13, minute=0, second=0, microsecond=0)

if ahora_ny < ny_inicio:
    diff = ny_inicio - ahora_ny
    estado_ny = f"⏳ NY abre en {diff.seconds//3600}h {(diff.seconds%3600)//60}m"
elif ahora_ny > ny_fin:
    estado_ny = "🔴 Sesion NY cerrada"
else:
    diff = ny_fin - ahora_ny
    estado_ny = f"🟢 NY EN VIVO - Cierra en {diff.seconds//3600}h {(diff.seconds%3600)//60}m"

col_h1, col_h2, col_h3 = st.columns([2,2,1])
with col_h1:
    st.markdown(f"<div class='reloj'>Sevilla {ahora_sev.strftime('%H:%M:%S')}</div>", unsafe_allow_html=True)
with col_h2:
    st.markdown(f"<div class='reloj'>{estado_ny}</div>", unsafe_allow_html=True)
with col_h3:
    if st.button("🔄 RESET", use_container_width=True):
        st.session_state.c1 = False
        st.session_state.c2 = False
        st.session_state.c3 = False
        st.session_state.c4 = False
        st.session_state.c5 = False
        st.rerun()
