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

# HEADER CON LOGO - IGUAL QUE ANTES
h_logo, h_title, h_clock = st.columns([0.9, 2.2, 1])
with h_logo:
    try:
        st.image("logo.png", width=150)
    except:
        st.markdown("<h2 class='gold'>KB VINULA</h2>", unsafe_allow_html=True)
with h_title:
    st.markdown("<h1 style='margin:0; text-align:center'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
with h_clock:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>MADRID</b><br><h2 style='margin:0'>{madrid.strftime('%H:%M:%S')}</h2></div>", unsafe_allow_html=True)

st.divider()

# ZONA 1 - CALENDARIO ORIGINAL + PILARES ORIGINAL - COMO TU FOTO
col_cal, col_pilar = st.columns([1.4, 0.8])

with col_cal:
    st.markdown("#### 📅 CALENDARIO ECONOMICO USD")
    with st.container(border=True):
        components.html("""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
          {
            "colorTheme": "dark",
            "isTransparent": true,
            "width": "100%",
            "height": "450",
            "locale": "es",
            "importanceFilter": "-1,0,1",
            "currencyFilter": "USD,EUR",
            "isTransparent": true
          }
          </script>
        </div>
        """, height=470)

with col_pilar:
    st.markdown("#### 🏛️ PILARES FUNDAMENTALES")
    with st.container(border=True):
        st.markdown("*DXY*")
        st.markdown("<h2 style='margin:0'>103.2</h2><p style='color:#ff4b4b'>↓ -0.3%</p>", unsafe_allow_html=True)
        st.divider()
        st.markdown("*🌍 GEOPOLITICA*")
        geo = st.selectbox("geo", ["Tension media - Oro soporte","Guerra activa - Oro sube","Calma - Lateral"], label_visibility="collapsed")
        if "Guerra" in geo:
            st.error("🚀 Oro con soporte fuerte")
        else:
            st.warning("⚠️ Oro con soporte")
        st.divider()
        st.markdown("*📍 SESION HOY*")
        st.markdown("*Killzone: 08-11h y 14-17h Madrid*")
        st.info("Sesión Londres + NY")

# ZONA 2 - CANAL TV INFORMATIVO - DONDE TENIAS EL NEGRO VACIO - AHORA SI FUNCIONA
st.divider()
st.markdown("#### 📺 CANAL TV INFORMATIVO - TIEMPO REAL ORO")
with st.container(border=True):
    tv1, tv2 = st.columns([1.2, 1])
    with tv1:
        # TV QUE SI FUNCIONA EN TABLET - YOUTUBE BLOOMBERG LIVE
        components.html("""
        <iframe width="100%" height="300" src="https://www.youtube.com/embed/1W1r6NwI5Yw?autoplay=0&mute=1" title="Bloomberg TV Live" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """, height=320)
        st.caption("Bloomberg Markets Live - Oro / DXY / Fed")
    with tv2:
        # NOTICIAS EN VIVO QUE NO SE BLOQUEA
        components.html("""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
          {
            "feedMode": "market",
            "market": "forex",
            "colorTheme": "dark",
            "isTransparent": true,
            "displayMode": "regular",
            "width": "100%",
            "height": 300,
            "locale": "es"
          }
          </script>
        </div>
        """, height=320)

# ZONA 3 - GRAFICOS - FIX APPLE INC
st.divider()
g1,g2 = st.columns(2)
with g1:
    st.markdown("*📈 XAUUSD - ORO*")
    components.html("""
    <div id="kb_xau_v37" style="height:500px"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
      "container_id": "kb_xau_v37",
      "autosize": true,
      "symbol": "OANDA:XAUUSD",
      "interval": "60",
      "timezone": "Europe/Madrid",
      "theme": "dark",
      "style": "1",
      "locale": "es"
    });
    </script>
    """, height=520)

with g2:
    st.markdown("*📉 DXY - DOLAR - YA NO APPLE*")
    components.html("""
    <div id="kb_dxy_v37" style="height:500px"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
      "container_id": "kb_dxy_v37",
      "autosize": true,
      "symbol": "TVC:DXY",
      "interval": "60",
      "timezone": "Europe/Madrid",
      "theme": "dark",
      "style": "1",
      "locale": "es"
    });
    </script>
    """, height=520)

# CHECKLIST
st.divider()
st.markdown("### 🎯 CHECKLIST 7/7")
with st.container(border=True):
    t1=st.checkbox("1. Tendencia Diaria")
    t2=st.checkbox("2. Zona D1 S1 M1")
    t3=st.checkbox("3. Rechazo H4")
    t4=st.checkbox("4. BoS H1")
    t5=st.checkbox("5. FVG 15m")
    t6=st.checkbox("6. BoS 5m")
    t7=st.checkbox("7. Entrada")
    total=sum([t1,t2,t3,t4,t5,t6,t7])
    st.progress(total/7, text=f"{total}/7")
    if total==7: st.success("7/7 - EJECUTA"); st.balloons()
    else: st.error(f"{total}/7 - ESPERA")

# DIARIO
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
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=400, key="ed_v37")
st.session_state.df=edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("Guardado!")
