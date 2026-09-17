import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide", page_icon="logo.png")

# --- ESTILO ---
st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    .gold-bar { background: #111; color: #FFD60A; text-align: center; padding: 12px; font-weight: bold; border-radius: 8px; margin: 10px 0px; }
    .block-title { font-size: 22px; font-weight: 900; border-left: 6px solid #111; padding-left: 10px; margin-top: 15px;}
</style>
""", unsafe_allow_html=True)

# --- HEADER CON LOGO ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    try:
        st.image("logo.png", width=140)
    except:
        st.write("KB")
with col_title:
    st.markdown("<h1 style='margin-top:25px; font-weight:900; letter-spacing: -1px;'>KB VINUELA TRADING</h1>", unsafe_allow_html=True)

# --- RELOJES ---
tz_sevilla = pytz.timezone('Europe/Madrid')
tz_ny = pytz.timezone('America/New_York')
now_sevilla = datetime.now(tz_sevilla).strftime("%H:%M:%S")
now_ny = datetime.now(tz_ny).strftime("%H:%M:%S")

c1, c2 = st.columns(2)
c1.info(f"*Sevilla: {now_sevilla}*")
c2.info(f"*NY: {now_ny}*")

st.markdown('<div class="gold-bar">REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>', unsafe_allow_html=True)

# --- BLOQUES ---
colA, colB = st.columns(2)
with colA:
    st.markdown('<div class="block-title">BLOQUE A</div>', unsafe_allow_html=True)
    noticias = st.selectbox("Noticias rojas?", ["No - Verde", "Si - Rojo, NO TRADE"])
    par = st.selectbox("Par", ["XAUUSD - ORO", "EURUSD", "GBPUSD"])

with colB:
    st.markdown('<div class="block-title">BLOQUE B</div>', unsafe_allow_html=True)
    s1 = st.checkbox("1. Zona de interes D1/S1/M1")
    s2 = st.checkbox("2. Rechazo vela 4H")
    s3 = st.checkbox("3. BOS H1")
    s4 = st.checkbox("4. Retraso al FVG 15m")
    s5 = st.checkbox("5. Confirmacion 5m")
    score = sum([s1,s2,s3,s4,s5])
    if score == 5 and noticias == "No - Verde":
        st.success(f"SETUP PERFECTO ({score}/5) - PUEDES ENTRAR")
    else:
        st.warning(f"Esperando setup ({score}/5)")

st.divider()

# --- GRAFICOS GIGANTES ---
st.markdown('<div class="block-title">GRAFICO XAUUSD - VELAS GRANDES</div>', unsafe_allow_html=True)

# XAUUSD 800px alto
tradingview_xau = """
<div class="tradingview-widget-container" style="height:100%;width:100%">
  <div id="tradingview_xau" style="height:800px;width:100%"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": true,
  "symbol": "OANDA:XAUUSD",
  "interval": "60",
  "timezone": "Europe/Madrid",
  "theme": "light",
  "style": "1",
  "locale": "es",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "hide_side_toolbar": false,
  "save_image": true,
  "studies": ["STD;Supertrend"],
  "container_id": "tradingview_xau"
}
  );
  </script>
</div>
"""
components.html(tradingview_xau, height=820)

st.markdown('<div class="block-title">DXY - CONFIRMACION DOLAR</div>', unsafe_allow_html=True)

tradingview_dxy = """
<div class="tradingview-widget-container" style="height:100%;width:100%">
  <div id="tradingview_dxy" style="height:600px;width:100%"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": true,
  "symbol": "TVC:DXY",
  "interval": "60",
  "timezone": "Europe/Madrid",
  "theme": "light",
  "style": "1",
  "locale": "es",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_dxy"
}
  );
  </script>
</div>
"""
components.html(tradingview_dxy, height=620)
