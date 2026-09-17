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

# === HEADER CON LOGO ===
h1,h2,h3 = st.columns([0.9,2.2,1])
with h1:
    try: st.image("logo.png", width=140)
    except: st.markdown("<h2 class='gold'>KB VINULA</h2>", unsafe_allow_html=True)
with h2:
    st.markdown("<h1 style='text-align:center; margin:0'>KB VINULA TRADING</h1><p style='text-align:center; color:#FFD60A; margin:0'>Sistema Francotirador Oro</p>", unsafe_allow_html=True)
with h3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>MADRID</b><br><h2 style='margin:0'>{madrid.strftime('%H:%M:%S')}</h2></div>", unsafe_allow_html=True)

st.divider()

# === CALENDARIO + PILARES FUNDAMENTALES ===
col_cal, col_pilar = st.columns([1.2, 1])

with col_cal:
    st.markdown("#### 📅 CALENDARIO ECONOMICO USD")
    with st.container(border=True):
        components.html("""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
          {"colorTheme":"dark","isTransparent":true,"width":"100%","height":"650","locale":"es","importanceFilter":"-1,0,1","currencyFilter":"USD,EUR"}
          </script>
        </div>
        """, height=670)

with col_pilar:
    st.markdown("#### 🏛️ PILARES FUNDAMENTALES")
    with st.container(border=True):
        # 1 IPC
        st.markdown("*1. IPC USA*")
        ipc = st.slider("ipc", 0.0, 8.0, 3.2, 0.1, label_visibility="collapsed")
        if ipc > 4: st.error(f"IPC {ipc}% Alto = Oro baja")
        elif ipc < 2.5: st.success(f"IPC {ipc}% Bajo = Oro sube")
        else: st.warning(f"IPC {ipc}% Medio")

        # 2 NFP
        st.markdown("*2. NFP EMPLEO*")
        nfp = st.selectbox("nfp", ["Fuerte +200k - Oro baja","Medio 100-200k","Débil <100k - Oro sube"], label_visibility="collapsed")
        st.caption(nfp)

        # 3 FED
        st.markdown("*3. TASAS FED*")
        fed = st.selectbox("fed", ["Suben tasas - Oro baja","Mantienen - Oro soporte","Bajan tasas - Oro sube"], label_visibility="collapsed")
        if "Bajan" in fed: st.success("🚀 DXY baja = Oro sube")
        elif "Suben" in fed: st.error("DXY sube = Oro baja")
        else: st.warning("Oro con soporte")

        st.divider()
        c1,c2 = st.columns(2)
        c1.metric("DXY", "103.2", "-0.3%")
        c2.metric("VIX", "18.5", "Miedo medio")

        # 4 GEOPOLITICA
        st.markdown("*4. 🌍 GEOPOLITICA*")
        geo = st.selectbox("geo", ["Tensión media - Oro soporte","Guerra activa - Oro sube","Calma - Lateral"], label_visibility="collapsed")
        if "Guerra" in geo: st.error("🚀 Refugio")
        else: st.warning("⚠️ Soporte")

        # 5 SESION
        st.markdown("*5. 📍 SESION HOY*")
        st.info("Killzone: 08-11h y 14-17h Madrid")

# === CANAL TV INFORMATIVO - QUE SI FUNCIONA ===
st.divider()
st.markdown("#### 📺 CANAL TV INFORMATIVO - TIEMPO REAL ORO")
with st.container(border=True):
    tv1, tv2 = st.columns(2)
    with tv1:
        st.markdown("*Noticias Oro en Vivo*")
        components.html("""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
          {"feedMode":"market","market":"forex","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":350,"locale":"es"}
          </script>
        </div>
        """, height=370)
    with tv2:
        st.markdown("*Oro / DXY / VIX - Tiempo Real*")
        components.html("""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
          {"colorTheme":"dark","dateRange":"1D","showChart":true,"locale":"es","width":"100%","height":350,"isTransparent":true,"tabs":[{"title":"Oro & Dólar","symbols":[{"s":"OANDA:XAUUSD","d":"Oro"},{"s":"TVC:DXY","d":"DXY"},{"s":"TVC:VIX","d":"VIX"}]}]}
          </script>
        </div>
        """, height=370)

# === GRAFICOS - SIN BUG APPLE ===
st.divider()
st.markdown("### 📈 GRAFICOS")
g1,g2 = st.columns(2)
with g1:
    st.markdown("*XAUUSD - ORO*")
    components.html('<div id="kb_xau_final" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"container_id":"kb_xau_final","autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"dark","style":"1","locale":"es"})</script>', height=520)
with g2:
    st.markdown("*DXY - DOLAR*")
    components.html('<div id="kb_dxy_final" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"container_id":"kb_dxy_final","autosize":true,"symbol":"TVC:DXY","interval":"60","timezone":"Europe/Madrid","theme":"dark","style":"1","locale":"es"})</script>', height=520)

# === CHECKLIST ===
st.divider()
st.markdown("### 🎯 CHECKLIST 7/7")
with st.container(border=True):
    c1,c2 = st.columns(2)
    with c1:
        t1=st.checkbox("1. Tendencia Diaria")
        t2=st.checkbox("2. Zona D1 S1 M1")
        t3=st.checkbox("3. Rechazo H4")
        t4=st.checkbox("4. BoS H1")
    with c2:
        t5=st.checkbox("5. FVG 15m")
        t6=st.checkbox("6. BoS 5m")
        t7=st.checkbox("7. Entrada 1m")
    total=sum([t1,t2,t3,t4,t5,t6,t7])
    st.progress(total/7, text=f"{total}/7")
    if total==7:
        st.success("✅ 7/7 EJECUTA - FRANCOTIRADOR LISTO")
        st.balloons()
    else:
        st.error(f"⏳ {total}/7 ESPERA")

# === DIARIO ===
st.divider()
st.markdown("### 📂 DIARIO TRADING")
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
        return pd.DataFrame({"Fecha":[datetime.now().strftime("%d/%m/%Y")],"Activo":["MGC"],"Resultado":[""],"Comentario":[""]})

if "df" not in st.session_state: st.session_state.df=cargar()
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=400, key="final_v43")
st.session_state.df=edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("✅ Guardado!")
