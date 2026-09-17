import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide")

c1,c2=st.columns([1,4])
with c1:
    try: st.image("logo.png", width=150)
    except: st.write("KB")
with c2: st.markdown("<h1>KB VINUELA TRADING</h1>", unsafe_allow_html=True)

colA,colB=st.columns([2,1])
with colA:
    st.markdown("### BLOQUE A - SOLO US 3 ESTRELLAS")
    noticias=st.selectbox("Hoy?", ["No - Verde", "Si - Rojo NO TRADE"])
    components.html('<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"light","isTransparent":false,"width":"100%","height":"550","locale":"es","importanceFilter":"1","countryFilter":"us"}</script></div>', height=580)
with colB:
    st.markdown("### BLOQUE B")
    s1=st.checkbox("1. Zona"); s2=st.checkbox("2. Rechazo"); s3=st.checkbox("3. BOS"); s4=st.checkbox("4. FVG"); s5=st.checkbox("5. Conf")
    score=s1+s2+s3+s4+s5
    st.write(f"{score}/5")

components.html('<div id="tv_xau" style="height:800px;width:100%"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","container_id":"tv_xau"});</script>', height=820)
