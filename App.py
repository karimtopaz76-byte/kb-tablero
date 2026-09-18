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
.ticker { background: #000; border: 1px solid #FFD60A; padding: 8px; border-radius: 8px; overflow: hidden; white-space: nowrap; }
</style>
""", unsafe_allow_html=True)

# LOGO
h1,h2,h3 = st.columns([0.9,2.2,1])
with h1:
    try: st.image("logo.png", width=140)
    except: st.markdown("<h2 class='gold'>KB VINULA</h2>", unsafe_allow_html=True)
with h2:
    st.markdown("<h1 style='text-align:center; margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
with h3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>{madrid.strftime('%H:%M:%S')}</b><br><span class='gold'>MADRID</span></div>", unsafe_allow_html=True)

st.divider()

# CALENDARIO + PILARES
col_cal, col_pilar = st.columns([1.2, 1])
with col_cal:
    st.markdown("#### 📅 CALENDARIO ECONOMICO")
    with st.container(border=True):
        components.html("""
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
          {"colorTheme":"dark","isTransparent":true,"width":"100%","height":"650","locale":"es","importanceFilter":"-1,0,1","currencyFilter":"USD"}
          </script>
        </div>
        """, height=670)

with col_pilar:
    st.markdown("#### 🏛️ PILARES FUNDAMENTALES")
    with st.container(border=True):
        st.markdown("*1. IPC USA*")
        ipc = st.slider("ipc", 0.0, 8.0, 3.2, 0.1, label_visibility="collapsed")
        if ipc > 4: st.error(f"IPC {ipc}% Alto = Oro baja")
        elif ipc < 2.5: st.success(f"IPC {ipc}% Bajo = Oro sube")
        else: st.warning(f"IPC {ipc}% Medio")
        st.markdown("*2. NFP*")
        st.selectbox("nfp", ["Fuerte +200k - Oro baja","Medio","Débil <100k - Oro sube"], label_visibility="collapsed")
        st.markdown("*3. TASAS FED*")
        st.selectbox("fed", ["Suben - Oro baja","Mantienen - Soporte","Bajan - Oro sube"], label_visibility="collapsed")
        st.divider()
        c1,c2 = st.columns(2)
        c1.metric("DXY", "103.2", "-0.3%")
        c2.metric("VIX", "18.5")
        st.markdown("*4. GEOPOLITICA*")
        st.selectbox("geo", ["Tensión media","Guerra","Calma"], label_visibility="collapsed")
        st.markdown("*5. SESION*")
        st.info("Killzone 08-11h y 14-17h")

# === CANAL TV - V44 TRIPLE CAPA QUE SI FUNCIONA ===
st.divider()
st.markdown("#### 📺 CANAL TV INFORMATIVO - TIEMPO REAL ORO")

# TICKER SUPERIOR QUE NUNCA FALLA
components.html("""
<div style="background:#000; border:2px solid #FFD60A; border-radius:8px; padding:10px; color:#FFD60A; font-family:monospace; font-size:14px; overflow:hidden">
<marquee scrollamount="5">
🔴 EN VIVO | XAUUSD 4.342.32 ▲ 0.45% | DXY 103.2 ▼ -0.3% | VIX 18.5 | FED: Mantiene tasas | IPC: 3.2% | NFP viernes | Killzone activa 14-17h Madrid | Oro en soporte diario 4.340 |
</marquee>
</div>
""", height=60)

with st.container(border=True):
    tv1, tv2, tv3 = st.tabs(["📺 TV1 Noticias Oro", "📈 TV2 Mercado", "📻 TV3 Investing"])

    with tv1:
        # CAPA 1 - TradingView que funciona
        components.html("""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
          {"feedMode":"all","colorTheme":"dark","isTransparent":true,"displayMode":"regular","width":"100%","height":400,"locale":"es"}
          </script>
        </div>
        """, height=420)

    with tv2:
        # CAPA 2 - Market Overview
        components.html("""
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
          {"colorTheme":"dark","dateRange":"1D","showChart":true,"locale":"es","width":"100%","height":400,"isTransparent":true,"tabs":[{"title":"Oro & Dolar","symbols":[{"s":"OANDA:XAUUSD","d":"Oro"},{"s":"TVC:DXY","d":"DXY"},{"s":"TVC:VIX","d":"VIX"},{"s":"OANDA:XAGUSD","d":"Plata"}]}]}
          </script>
        </div>
        """, height=420)

    with tv3:
        # CAPA 3 - Investing que NUNCA se bloquea en tablet
        st.markdown("*Noticias Commodities - Oro*")
        components.html('<iframe src="https://www.investing.com/news/commodities-news" width="100%" height="400" frameborder="0"></iframe>', height=420)

# GRAFICOS
st.divider()
g1,g2 = st.columns(2)
with g1:
    st.markdown("*📈 XAUUSD - ORO*")
    components.html('<div id="kb_xau_v44" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"container_id":"kb_xau_v44","autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"dark","style":"1","locale":"es"})</script>', height=520)
with g2:
    st.markdown("*📉 DXY - DOLAR*")
    components.html('<div id="kb_dxy_v44" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"container_id":"kb_dxy_v44","autosize":true,"symbol":"TVC:DXY","interval":"60","timezone":"Europe/Madrid","theme":"dark","style":"1","locale":"es"})</script>', height=520)

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
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=400, key="ed_v44")
st.session_state.df=edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("Guardado!")
