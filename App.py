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

# HEADER
st.markdown("<h1 style='margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
c1,c2,c3 = st.columns([1,1,2])
with c1:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>MADRID</b><br><h2>{madrid.strftime('%H:%M:%S')}</h2><span class='gold'>ABIERTO</span></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='card' style='text-align:center'><b>XAUUSD</b><br><h2>4.341</h2></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='card'><b class='gold'>REGLA DE ORO</b><br>Sin 7/7 no hay trade</div>", unsafe_allow_html=True)

st.divider()

# CALENDARIO ECONOMICO + PILARES - AHORA SI
f1,f2 = st.columns([1.3, 0.9])

with f1:
    st.markdown("### 📅 CALENDARIO ECONOMICO USD")
    with st.container(border=True):
        # Widget 1 - TradingView Events - Este carga siempre
        components.html("""
        <div style="height:420px; background:#151515">
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
          {
            "colorTheme": "dark",
            "isTransparent": true,
            "width": "100%",
            "height": "420",
            "locale": "es",
            "importanceFilter": "-1,0,1",
            "currencyFilter": "USD,EUR",
            "isTransparent": true
          }
          </script>
        </div>
        </div>
        """, height=440)

with f2:
    st.markdown("### 🏛️ PILARES FUNDAMENTAL ORO")
    with st.container(border=True):
        st.markdown("*🔥 IPC (Inflacion USA)*")
        st.markdown("Alto = Malo para Oro")
        st.progress(75, text="IPC Alto")

        st.markdown("*💼 NFP (Empleo USA)*")
        st.markdown("Fuerte = DXY sube, Oro baja")
        st.progress(40, text="NFP Medio")

        st.divider()
        a,b = st.columns(2)
        a.metric("DXY", "103.2", "-0.3%", help="DXY baja = Oro sube")
        b.metric("VIX MIEDO", "18.5", "Medio")

        st.markdown("---")
        st.markdown("*🌍 GEOPOLITICA*")
        geo = st.selectbox("geo", ["Tension media - Oro soporte","Guerra activa - Oro sube fuerte","Calma - Oro lateral / baja"], label_visibility="collapsed")
        if "Guerra" in geo:
            st.error("🚀 Oro alcista fuerte")
        elif "Tension" in geo:
            st.warning("⚠️ Oro con soporte")
        else:
            st.info("😴 Oro lateral")

        st.markdown("---")
        st.markdown("*📊 SESION HOY*")
        st.markdown("Killzone: 08-11h y 14-17h Madrid")

# GRAFICOS
st.divider()
g1,g2 = st.columns(2)
with g1:
    st.markdown("*📈 XAUUSD - ORO*")
    components.html("""<div id="xau_v31" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"dark","container_id":"xau_v31"})</script>""", height=520)
with g2:
    st.markdown("*📉 DXY - DOLAR*")
    components.html("""<div id="dxy_v31" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"TVC:DXY","interval":"60","timezone":"Europe/Madrid","theme":"dark","container_id":"dxy_v31"})</script>""", height=520)

# CHECKLIST
st.divider()
st.markdown("### 🎯 CHECKLIST FRANCOTIRADOR")
with st.container(border=True):
    t1 = st.checkbox("1. Tendencia Diaria")
    t2 = st.checkbox("2. Zona D1 S1 M1")
    t3 = st.checkbox("3. Rechazo H4")
    t4 = st.checkbox("4. BoS H1")
    t5 = st.checkbox("5. FVG 15m")
    t6 = st.checkbox("6. BoS 5m")
    t7 = st.checkbox("7. Entrada")
    total = sum([t1,t2,t3,t4,t5,t6,t7])
    st.progress(total/7, text=f"{total}/7")
    if total==7:
        st.success("7/7 - EJECUTA")
        st.balloons()
    else:
        st.error(f"{total}/7 - ESPERA")

# DIARIO
st.divider()
st.markdown("### 📂 DIARIO DE TRADING")
FILE = "trading.xlsx"
def cargar():
    try:
        tmp = pd.read_excel(FILE, header=None)
        fila = 0
        for i in range(len(tmp)):
            if "Fecha" in str(tmp.iloc[i].values):
                fila = i
                break
        df = pd.read_excel(FILE, header=fila)
        cols = [c for c in df.columns if "Unnamed" not in str(c)]
        df = df[cols]
        df = df.dropna(how='all').fillna("")
        if "Fecha" in df.columns:
            df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce').dt.strftime("%d/%m/%Y")
            df["Fecha"] = df["Fecha"].fillna("").replace("NaT","")
        df = df.replace("0.0","")
        return df
    except:
        return pd.DataFrame({"Fecha":[datetime.now().strftime("%d/%m/%Y")],"Activo":["MGC"],"Resultado":[""],"Comentario":[""]})

if "df" not in st.session_state:
    st.session_state.df = cargar()

edit = st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=450, key="ed_v31")
st.session_state.df = edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("Guardado!")
    st.balloons()
