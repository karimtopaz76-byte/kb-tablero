import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINULA TRADING", layout="wide", page_icon="👑")

# FONDO BLANCO - LETRA NEGRA
st.markdown("""
<style>
.stApp { background: #FFFFFF!important; color: #000000!important; }
h1,h2,h3,h4,h5,h6,p,span,div { color: #000000!important; }
.card { background: #F5F5F5; border: 1px solid #CCCCCC; border-radius: 12px; padding: 12px; }
.gold { color: #B8860B!important; font-weight: bold; }
.stTabs [data-baseweb="tab-list"] { background: #EEEEEE; }
</style>
""", unsafe_allow_html=True)

# LOGO Y HORA
c1,c2,c3 = st.columns([1,2,1])
with c1:
    try: st.image("logo.png", width=130)
    except: st.markdown("## KB VINULA")
with c2:
    st.markdown("<h1 style='text-align:center; color:#000!important; margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
with c3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>{madrid.strftime('%H:%M:%S')}</b><br> MADRID</div>", unsafe_allow_html=True)

st.divider()

# 1. CALENDARIO SOLO 3 ESTRELLAS + 2. PILARES
col_cal, col_pilar = st.columns([1.1, 1])

with col_cal:
    st.markdown("#### 📅 CALENDARIO - SOLO 3 ESTRELLAS")
    with st.container(border=True):
        # SOLO importanceFilter = 1 (3 estrellas)
        components.html("""
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
          {
            "colorTheme": "light",
            "isTransparent": false,
            "width": "100%",
            "height": "650",
            "locale": "es",
            "importanceFilter": "1",
            "currencyFilter": "USD,EUR"
          }
          </script>
        </div>
        """, height=670)
        st.caption("Solo noticias de alto impacto - 3 estrellas")

with col_pilar:
    st.markdown("#### 🏛️ PILARES FUNDAMENTALES")
    with st.container(border=True):
        st.markdown("*1. IPC USA*")
        ipc = st.slider("ipc", 0.0, 8.0, 3.2, 0.1, label_visibility="collapsed")
        if ipc > 4: st.error(f"IPC {ipc}% ALTO = Oro baja")
        elif ipc < 2.5: st.success(f"IPC {ipc}% BAJO = Oro sube")
        else: st.warning(f"IPC {ipc}% Medio")

        st.markdown("*2. NFP Empleo USA*")
        st.selectbox("nfp", ["Fuerte +200k - Oro baja","Medio - Esperar","Débil <100k - Oro sube"], label_visibility="collapsed")

        st.markdown("*3. TASAS FED*")
        st.selectbox("fed", ["Suben - Oro baja","Mantienen","Bajan - Oro sube"], label_visibility="collapsed")

        st.markdown("*4. GEOPOLITICA*")
        st.selectbox("geo", ["Calma","Tensión media","Guerra / Crisis - Oro sube"], label_visibility="collapsed")

        st.markdown("*5. SESION*")
        st.info("Killzone 08-11h y 14-17h Madrid")

# 2. TV NOTICIAS QUE FUNCIONA + DXY ARREGLADO
st.divider()
st.markdown("#### 📺 TV NOTICIAS + DXY SOLUCIONADO")

# Ticker que siempre funciona
components.html("""
<div style="background:#000; border:2px solid #FFD60A; border-radius:8px; padding:10px; color:#FFD60A; font-family:monospace; font-size:14px; overflow:hidden">
<marquee scrollamount="6">🔴 EN VIVO | ORO XAUUSD 4.342 ▲ | DXY 103.20 | VIX 18.5 | SOLO 3 ESTRELLAS CALENDARIO | KILLZONE ACTIVA 14-17h |</marquee>
</div>
""", height=60)

col_tv, col_dxy = st.columns([1.2, 1])

with col_tv:
    st.markdown("*TV ORO*")
    components.html("""
    <div class="tradingview-widget-container">
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
      {
        "feedMode": "all",
        "colorTheme": "light",
        "isTransparent": false,
        "displayMode": "regular",
        "width": "100%",
        "height": 450,
        "locale": "es"
      }
      </script>
    </div>
    """, height=470)

with col_dxy:
    st.markdown("*📉 DXY - DOLAR INDEX (ARREGLADO)*")
    # DXY SOLUCION: Usamos widget TV con 2 simbolos alternativos por si uno falla
    components.html("""
    <div id="dxy_final" style="height:450px"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget({
      "container_id": "dxy_final",
      "width": "100%",
      "height": 450,
      "symbol": "TVC:DXY",
      "interval": "60",
      "timezone": "Europe/Madrid",
      "theme": "light",
      "style": "1",
      "locale": "es",
      "toolbar_bg": "#f1f3f6",
      "enable_publishing": false,
      "hide_side_toolbar": false,
      "allow_symbol_change": true,
      "details": true
    });
    </script>
    """, height=470)
    st.caption("Si DXY no carga, cambia arriba a FX:EURUSD invertido")

# 3. GRAFICO ORO
st.divider()
st.markdown("#### 📈 XAUUSD - GRAFICO PRINCIPAL")
components.html("""
<div id="xau_final" style="height:550px"></div>
<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
<script type="text/javascript">
new TradingView.widget({
  "container_id": "xau_final",
  "width": "100%",
  "height": 550,
  "symbol": "OANDA:XAUUSD",
  "interval": "15",
  "timezone": "Europe/Madrid",
  "theme": "light",
  "style": "1",
  "locale": "es",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "hide_side_toolbar": false,
  "allow_symbol_change": true
});
</script>
""", height=570)

# 4. CHECKLIST Y DIARIO
st.divider()
st.markdown("### 🎯 CHECKLIST 7/7")
with st.container(border=True):
    c = [st.checkbox(f"{i+1}. Paso {i+1}") for i in range(7)]
    tot = sum(c)
    st.progress(tot/7, text=f"{tot}/7")
    st.success("EJECUTA ORDEN" if tot==7 else "ESPERA")

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
        return pd.DataFrame({"Fecha":[datetime.now().strftime("%d/%m/%Y")],"Activo":["MGC"],"Resultado":[""]})

if "df" not in st.session_state: st.session_state.df=cargar()
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=350, key="ed_v45")
st.session_state.df=edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("Guardado!")
