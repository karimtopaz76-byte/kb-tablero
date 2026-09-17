import streamlit as st
from datetime import datetime
import pytz
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    h1 { color: #000000 !important; font-weight: 900 !important; text-align: center; }
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

col_logo, col_titulo = st.columns([1,4])
with col_logo:
    try:
        st.image("logo.png", width=110)
    except:
        st.markdown("<h1 style='font-size:45px;margin:0px;'>KB</h1>", unsafe_allow_html=True)
with col_titulo:
    st.markdown("<h1>KB VINUELA TRADING</h1>", unsafe_allow_html=True)

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
        ny_text += " EN VIVO"
    st.markdown(f"<div class='reloj'>{ny_text}</div>", unsafe_allow_html=True)
with c3:
    if st.button("RESET"):
        st.session_state.clear()
        st.rerun()

st.markdown("<div class='regla-oro'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)

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
    st.markdown('<div class="caja-no">NO OPERAR - Noticias rojas</div>', unsafe_allow_html=True)
elif checks == 5:
    st.markdown('<div class="caja-ok">SETUP VALIDO 5/5 - PUEDES ENTRAR</div>', unsafe_allow_html=True)
    st.balloons()
else:
    st.markdown(f'<div class="caja-espera">Esperando setup ({checks}/5)</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div class="bloque">GRAFICOS EN VIVO</div>', unsafe_allow_html=True)

col_g1, col_g2 = st.columns(2)
with col_g1:
    st.write("XAUUSD - ORO")
    components.html("""
    <div id="tv1"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
        "autosize": true, "height": 400,
        "symbol": "OANDA:XAUUSD", "interval": "15",
        "timezone": "Etc/UTC", "theme": "light", "style": "1",
        "locale": "es", "container_id": "tv1"
      });
    </script>
    """, height=420)
with col_g2:
    st.write("DXY - INDICE DOLAR")
    components.html("""
    <div id="tv2"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
        "autosize": true, "height": 400,
        "symbol": "TVC:DXY", "interval": "60",
        "timezone": "Etc/UTC", "theme": "light", "style": "1",
        "locale": "es", "container_id": "tv2"
      });
    </script>
    """, height=420)

st.markdown("---")
st.markdown('<div class="bloque">BITACORA KB</div>', unsafe_allow_html=True)
r1, r2, r3, r4 = st.columns(4)
with r1: resultado = st.selectbox("Resultado", ["Pendiente", "WIN", "LOSS", "BE"])
with r2: entrada = st.text_input("Entrada")
with r3: sl = st.text_input("SL")
with r4: notas = st.text_input("Notas")

if st.button("Guardar Trade"):
    nuevo = {"Fecha": ahora_sev.strftime("%d/%m %H:%M"), "Par": par, "Resultado": resultado, "Entrada": entrada, "SL": sl, "Checks": f"{checks}/5", "Notas": notas}
    st.session_state.bitacora.append(nuevo)
    st.success("Guardado!")

if st.session_state.bitacora:
    st.dataframe(pd.DataFrame(st.session_state.bitacora), use_container_width=True)
