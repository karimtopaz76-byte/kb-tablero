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

# LOGO + TITULO
h1,h2,h3 = st.columns([1,2,1])
with h1:
    try: st.image("logo.png", width=140)
    except: st.markdown("<h2 class='gold'>KB VINULA</h2>", unsafe_allow_html=True)
with h2:
    st.markdown("<h1 style='text-align:center; margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
with h3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>{madrid.strftime('%H:%M')}</b><br><span class='gold'>MADRID</span></div>", unsafe_allow_html=True)

st.divider()

# 3 COLUMNAS - NADA VACIO
col_cal, col_pilar, col_tv = st.columns([1.2, 0.8, 1])

with col_cal:
    st.markdown("#### 📅 CALENDARIO")
    with st.container(border=True):
        components.html('<iframe src="https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=5,17,29,25,54,32,6&calType=week&timeZone=23&lang=3" width="100%" height="380" frameborder="0"></iframe>', height=400)

with col_pilar:
    st.markdown("#### 🏛️ PILARES")
    with st.container(border=True):
        st.metric("DXY", "103.2", "-0.3%")
        st.metric("VIX", "18.5")
        st.markdown("---")
        st.markdown("*GEOPOLITICA*")
        geo = st.selectbox("geo", ["Tension media - Oro soporte","Guerra - Oro sube","Calma"], label_visibility="collapsed")
        st.warning("Oro con soporte")
        st.markdown("Killzone: 08-11h y 14-17h")

with col_tv:
    st.markdown("#### 📺 CANAL TV INFORMATIVO")
    with st.container(border=True):
        st.markdown("""
        <div style="background:#000; border:1px solid #FFD60A; border-radius:8px; padding:10px; height:380px">
        <p style="color:#FFD60A; font-weight:bold">🔴 EN VIVO ORO</p>
        <p style="font-size:13px; color:#fff">• 08:00 - Apertura Londres</p>
        <p style="font-size:13px; color:#fff">• DXY 103.2 cae -0.3% -> Oro sube</p>
        <p style="font-size:13px; color:#fff">• Oro 4.342 en soporte diario</p>
        <p style="font-size:13px; color:#fff">• VIX 18.5 miedo medio</p>
        <p style="font-size:13px; color:#fff">• IPC USA miercoles - ATENTO</p>
        <p style="font-size:13px; color:#fff">• Killzone activa 14-17h</p>
        <hr>
        <p style="color:#FFD60A">📢 TV: Bloomberg Oro</p>
        </div>
        """, unsafe_allow_html=True)

# GRAFICOS - FIX APPLE INC
st.divider()
st.markdown("### 📈 GRAFICOS")
g1,g2 = st.columns(2)

with g1:
    st.markdown("*XAUUSD - ORO*")
    components.html("""
    <div id="xau_final_36" style="height:500px"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
      "container_id": "xau_final_36",
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
    st.markdown("*DXY - DOLAR - FIX APPLE*")
    components.html("""
    <div id="dxy_final_36" style="height:500px"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
      "container_id": "dxy_final_36",
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
    t1=st.checkbox("1. Tendencia")
    t2=st.checkbox("2. Zona D1 S1 M1")
    t3=st.checkbox("3. Rechazo H4")
    t4=st.checkbox("4. BoS H1")
    t5=st.checkbox("5. FVG 15m")
    t6=st.checkbox("6. BoS 5m")
    t7=st.checkbox("7. Entrada")
    total=sum([t1,t2,t3,t4,t5,t6,t7])
    st.progress(total/7, text=f"{total}/7")
    st.success("EJECUTA" if total==7 else "ESPERA")

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
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=400, key="ed_v36")
st.session_state.df=edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("Guardado!")
    st.balloons()
