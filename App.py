import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINULA TRADING", layout="wide", page_icon="👑")

st.markdown("""
<style>
.stApp { background: #0A0A0A; color: #EAEAEA; }
.card { background: #151515; border: 1px solid #2A2A2A; border-radius: 14px; padding: 14px; }
.gold { color: #FFD60A; }
</style>
""", unsafe_allow_html=True)

# HEADER CON LOGO
c1,c2,c3 = st.columns([0.9,2.2,1])
with c1:
    try: st.image("logo.png", width=140)
    except: st.markdown("<h2 class='gold'>KB VINULA</h2>", unsafe_allow_html=True)
with c2:
    st.markdown("<h1 style='text-align:center; margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
with c3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>{madrid.strftime('%H:%M:%S')}</b><br><span class='gold'>MADRID</span></div>", unsafe_allow_html=True)

st.divider()

# CALENDARIO + PILARES - RESTAURADO ORIGINAL
col_cal, col_pilar = st.columns([1.4, 0.8])

with col_cal:
    st.markdown("#### 📅 CALENDARIO ECONOMICO")
    with st.container(border=True):
        components.html("""
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
          {"colorTheme":"dark","isTransparent":true,"width":"100%","height":"420","locale":"es","importanceFilter":"-1,0,1","currencyFilter":"USD"}
          </script>
        </div>
        """, height=440)

with col_pilar:
    st.markdown("#### 🏛️ PILARES FUNDAMENTALES")
    with st.container(border=True):
        st.metric("DXY", "103.2", "-0.3%")
        st.metric("VIX", "18.5", "Medio")
        st.divider()
        st.markdown("*🌍 GEOPOLITICA*")
        geo = st.selectbox("geo", ["Tension media - Oro soporte","Guerra - Oro sube","Calma - Lateral"], label_visibility="collapsed")
        if "Guerra" in geo: st.error("🚀 Oro alcista")
        else: st.warning("⚠️ Oro con soporte")
        st.divider()
        st.markdown("*📍 SESION HOY*")
        st.info("Killzone: 08-11h y 14-17h Madrid")

# CANAL TV INFORMATIVO - FIX VIDÉO NON DISPONIBLE
st.divider()
st.markdown("#### 📺 CANAL TV INFORMATIVO - TIEMPO REAL ORO")
with st.container(border=True):
    t1,t2 = st.columns([1,1])
    with t1:
        st.markdown("*Noticias Mercado Oro en Vivo*")
        components.html("""
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
          {"feedMode":"symbol","symbol":"OANDA:XAUUSD","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":350,"locale":"es"}
          </script>
        </div>
        """, height=370)
    with t2:
        st.markdown("*Mercado Oro / DXY / Fed*")
        components.html("""
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
          {"colorTheme":"dark","dateRange":"1D","showChart":true,"locale":"es","width":"100%","height":350,"isTransparent":true,"showSymbolLogo":true,"showFloatingTooltip":false,"plotLineColorGrowing":"rgba(255,214,10,1)","plotLineColorFalling":"rgba(255,214,10,1)","gridLineColor":"rgba(240,243,250,0)","scaleFontColor":"rgba(120,123,134,1)","belowLineFillColorGrowing":"rgba(41,98,255,0.12)","belowLineFillColorFalling":"rgba(41,98,255,0.12)","belowLineFillColorGrowingBottom":"rgba(41,98,255,0)","belowLineFillColorFallingBottom":"rgba(41,98,255,0)","symbolActiveColor":"rgba(41,98,255,0.12)","tabs":[{"title":"Oro & Dolar","symbols":[{"s":"OANDA:XAUUSD","d":"Oro"},{"s":"TVC:DXY","d":"DXY"},{"s":"TVC:VIX","d":"VIX"}]}]}
          </script>
        </div>
        """, height=370)

# GRAFICOS - FIX DEFINITIVO
st.divider()
g1,g2 = st.columns(2)
with g1:
    st.markdown("*📈 XAUUSD - ORO*")
    components.html('<div id="kb_xau_v39" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"container_id":"kb_xau_v39","autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"dark","style":"1","locale":"es"})</script>', height=520)
with g2:
    st.markdown("*📉 DXY - DOLAR*")
    components.html('<div id="kb_dxy_v39" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"container_id":"kb_dxy_v39","autosize":true,"symbol":"TVC:DXY","interval":"60","timezone":"Europe/Madrid","theme":"dark","style":"1","locale":"es"})</script>', height=520)

# CHECKLIST + DIARIO
st.divider()
st.markdown("### 🎯 CHECKLIST 7/7")
with st.container(border=True):
    checks = [st.checkbox(f"{i+1}. Paso {i+1}") for i in range(7)]
    total = sum(checks)
    st.progress(total/7, text=f"{total}/7")
    st.success("EJECUTA" if total==7 else "ESPERA")

st.divider()
st.markdown("### 📂 DIARIO")
FILE="trading.xlsx"
def cargar():
    try:
        tmp=pd.read_excel(FILE, header=None)
        f=0
        for i in range(len(tmp)):
            if "Fecha" in str(tmp.iloc[i].values): f=i; break
        df=pd.read_excel(FILE, header=f)
        df=df[[c for c in df.columns if "Unnamed" not in str(c)]].dropna(how='all').fillna("")
        if "Fecha" in df.columns:
            df["Fecha"]=pd.to_datetime(df["Fecha"], errors='coerce').dt.strftime("%d/%m/%Y").replace("NaT","").fillna("")
        return df.replace("0.0","")
    except:
        return pd.DataFrame({"Fecha":[datetime.now().strftime("%d/%m/%Y")],"Activo":["MGC"],"Resultado":[""]})

if "df" not in st.session_state: st.session_state.df=cargar()
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=400, key="ed_v39")
st.session_state.df=edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("Guardado!")
