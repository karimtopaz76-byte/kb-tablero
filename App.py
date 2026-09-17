    import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide", page_icon="logo.png")

st.markdown("""
<style>
.stApp{background:#FFFFFF}
.gold-bar{background:#111;color:#FFD60A;text-align:center;padding:14px;font-weight:900;border-radius:8px;margin:15px 0;font-size:18px}
.block-title{font-size:22px;font-weight:900;border-left:6px solid #111;padding-left:10px;margin-top:28px;margin-bottom:10px}
.phrase-card{background:#f9f9f9;border-left:4px solid #FFD60A;padding:10px 15px;margin:8px 0;border-radius:6px;font-size:14px;font-style:italic}
.pillar-box{background:#111;color:white;padding:12px;border-radius:8px;text-align:center;font-size:13px;font-weight:bold}
</style>
""", unsafe_allow_html=True)

# HEADER
c1,c2 = st.columns([1,4])
with c1:
    try: st.image("logo.png", width=170)
    except: st.markdown("### KB")
with c2:
    st.markdown("<h1 style='margin-top:30px;font-weight:900;'>KB VINUELA<br>TRADING</h1>", unsafe_allow_html=True)

# MENTALIDAD
st.markdown("<div class='block-title'>MENTALIDAD KB - 6 REGLAS</div>", unsafe_allow_html=True)
a,b = st.columns(2)
with a:
    st.markdown("<div class='phrase-card'><b>1. Paciencia:</b> Aprender a cultivar la paciencia.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>2. Enemigos:</b> Aburrimiento, esperanza y miedo.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>3. Proceso:</b> Enfocarse en el proceso, no en resultados.</div>", unsafe_allow_html=True)
with b:
    st.markdown("<div class='phrase-card'><b>4. Afirmacion:</b> Soy mas paciente, centrado, disciplinado.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>5. Mentalidad:</b> Lo que te hara rico es como piensas.</div>", unsafe_allow_html=True)
    st.markdown("<div class='phrase-card'><b>6. Ejecucion:</b> Actuar sin temor a consecuencias.</div>", unsafe_allow_html=True)

# PILARES
st.markdown("<div class='block-title'>LOS 3 PILARES</div>", unsafe_allow_html=True)
p1,p2,p3 = st.columns(3)
p1.markdown("<div class='pillar-box'>FUNDAMENTAL<br>El POR QUE</div>", unsafe_allow_html=True)
p2.markdown("<div class='pillar-box'>TECNICO<br>El COMO</div>", unsafe_allow_html=True)
p3.markdown("<div class='pillar-box'>PSICOLOGIA<br>El QUIEN</div>", unsafe_allow_html=True)

# RELOJES
tz_mad=pytz.timezone('Europe/Madrid')
tz_ny=pytz.timezone('America/New_York')
r1,r2=st.columns(2)
r1.info(f"SEVILLA: {datetime.now(tz_mad).strftime('%H:%M:%S')}")
r2.info(f"NY: {datetime.now(tz_ny).strftime('%H:%M:%S')}")

st.markdown("<div class='gold-bar'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)

# BLOQUES A y B
colA,colB = st.columns([2,1])
with colA:
    st.markdown("<div class='block-title'>BLOQUE A - SOLO NOTICIAS ROJAS US 3 ESTRELLAS</div>", unsafe_allow_html=True)
    noticias=st.selectbox("Noticias rojas hoy?", ["No - Verde, se puede operar", "Si - Rojo, NO TRADE"], key="noticias")
    components.html('<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"light","isTransparent":false,"width":"100%","height":"550","locale":"es","importanceFilter":"1","countryFilter":"us"}</script></div>', height=580)

with colB:
    st.markdown("<div class='block-title'>BLOQUE B - CHECKLIST 5/5</div>", unsafe_allow_html=True)
    s1=st.checkbox("1. Zona D1/S1/M1")
    s2=st.checkbox("2. Rechazo 4H")
    s3=st.checkbox("3. BOS H1")
    s4=st.checkbox("4. FVG 15m")
    s5=st.checkbox("5. Confirmacion 5m")
    score=s1+s2+s3+s4+s5
    if score==5 and "No" in noticias:
        st.success(f"SETUP PERFECTO {score}/5 - EJECUTA")
        st.balloons()
    elif "Si" in noticias:
        st.error("HOY NO SE OPERA - NOTICIA ROJA 3 ESTRELLAS")
    else:
        st.warning(f"Esperando {score}/5")
st.divider()
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
<div id="tv_dxy_final" style="height:600px;width:100%"></div>
<script src="https://s3.tradingview.com/tv.js"></script>
<script>
new TradingView.widget({
  "autosize": true,
  "symbol": "CAPITALCOM:DXY",
  "interval": "60",
  "timezone": "Europe/Madrid",
  "theme": "light",
  "style": "1",
  "locale": "es",
  "container_id": "tv_dxy_final"
});
</script>
""", height=620)
