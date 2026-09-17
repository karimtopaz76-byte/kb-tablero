import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINULA TRADING", layout="wide", page_icon="👑")

st.markdown("""
<style>
.stApp { background: #0A0A0A; color: #EAEAEA; }
.card { background: #151515; border: 1px solid #2A2A2A; border-radius: 14px; padding: 16px; }
.gold { color: #FFD60A; }
.gold-bar { background: linear-gradient(90deg,#FFD60A,#FFB700); color: #111; font-weight: 900; text-align: center; padding: 8px; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# HEADER
h1,h2,h3 = st.columns([1.2, 2.5, 1.5])
with h1:
    try: st.image("logo.png", width=140)
    except: st.markdown("<div class='card' style='height:140px;display:flex;align-items:center;justify-content:center'><h2 class='gold'>KB</h2></div>", unsafe_allow_html=True)
with h2:
    st.markdown("<h1 style='margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        madrid = datetime.now(pytz.timezone('Europe/Madrid'))
        st.markdown(f"<div class='card' style='text-align:center'><b>MADRID</b><br><h2 style='margin:0'>{madrid.strftime('%H:%M:%S')}</h2><span class='gold'>MERCADO ABIERTO</span></div>", unsafe_allow_html=True)
    with c2:
        # PRECIO ARREGLADO - YA NO SE DISTORSIONA
        st.markdown("<div class='card' style='text-align:center'><b>XAUUSD</b>", unsafe_allow_html=True)
        components.html("""<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"OANDA:XAUUSD","width":"100%","height":80,"locale":"es","colorTheme":"dark","isTransparent":true}</script></div>""", height=85)
        st.markdown("</div>", unsafe_allow_html=True)

with h3:
    st.markdown("<div class='card'><b class='gold'>REGLA DE ORO</b><br>Menos trades, más calidad</div>", unsafe_allow_html=True)

st.divider()

# CALENDARIO + PILARES
f1,f2 = st.columns([1.2,1])
with f1:
    st.markdown("*📅 CALENDARIO ECONOMICO*")
    with st.container(border=True):
        components.html("""<div style="height:320px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":"320","importanceFilter":"-1,0,1","currencyFilter":"USD"}</script></div>""", height=330)
with f2:
    st.markdown("*🏛️ PILARES FUNDAMENTAL ORO*")
    with st.container(border=True):
        st.markdown("*IPC (Inflación):* Alto = Malo para oro")
        st.progress(70)
        st.markdown("*NFP (Empleo):* Fuerte = DXY sube = Oro baja")
        st.progress(45)
        c_a,c_b = st.columns(2)
        c_a.metric("DXY", "103.2", "-0.3%")
        c_b.metric("VIX", "18.5", "Miedo medio")

# GRAFICOS
g1,g2 = st.columns(2)
with g1:
    st.markdown("*📈 GRAFICO XAUUSD*")
    components.html("""<div id="kb_xau_v21" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"dark","container_id":"kb_xau_v21"})</script>""", height=520)
with g2:
    st.markdown("*📉 GRAFICO DXY*")
    components.html("""<div id="kb_dxy_v21" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"TVC:DXY","interval":"60","timezone":"Europe/Madrid","theme":"dark","container_id":"kb_dxy_v21"})</script>""", height=520)

# CHECKLIST REAL
st.divider()
st.markdown("### 🎯 CHECKLIST FRANCOTIRADOR")
with st.container(border=True):
    t1 = st.checkbox("Tendencia Diaria")
    t2 = st.checkbox("Zona de interes D1, S1, M1")
    t3 = st.checkbox("Rechazo de vela H4 de (D1,S1,M1)")
    t4 = st.checkbox("BoS H1")
    t5 = st.checkbox("Retraso a FVG 15m")
    t6 = st.checkbox("BoS 5m")
    t7 = st.checkbox("Entrada")
    total = sum([t1,t2,t3,t4,t5,t6,t7])
    st.progress(total/7)
    if total==7:
        st.balloons()
        st.success(f"{total}/7 - ENTRADA VALIDA")
    else:
        st.error(f"{total}/7 - ESPERA")

# DIARIO
st.divider()
st.markdown("### 📂 DIARIO DE TRADING")
try:
    tmp = pd.read_excel("trading.xlsx", header=None)
    fila=0
    for i in range(len(tmp)):
        if "Fecha" in str(tmp.iloc[i].values): fila=i; break
    df = pd.read_excel("trading.xlsx", header=fila)
    df = df.dropna(how='all')
    df = df.loc[:, ~df.columns.astype(str).str.contains('Unnamed', na=False)]
    st.dataframe(df, use_container_width=True, height=400)
except Exception as e:
    st.info(f"Añade trading.xlsx - {e}")
