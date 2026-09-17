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
h1,h2,h3 = st.columns([1.2, 2.5, 1.5])
with h1:
    try: st.image("logo.png", width=140)
    except: st.markdown("<div class='card'><h2 class='gold'>KB</h2></div>", unsafe_allow_html=True)
with h2:
    st.markdown("<h1 style='margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    c1,c2 = st.columns(2)
    with c1:
        st.markdown(f"<div class='card' style='text-align:center'><b>MADRID</b><br><h2>{madrid.strftime('%H:%M:%S')}</h2><span class='gold'>ABIERTO</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><b>XAUUSD</b>", unsafe_allow_html=True)
        components.html("""<div class="tradingview-widget-container"><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"OANDA:XAUUSD","width":"100%","height":80,"locale":"es","colorTheme":"dark","isTransparent":true}</script></div>""", height=85)

st.divider()

# GRAFICOS
g1,g2 = st.columns(2)
with g1:
    components.html("""<div id="xau" style="height:450px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","theme":"dark","container_id":"xau"})</script>""", height=470)
with g2:
    components.html("""<div id="dxy" style="height:450px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"TVC:DXY","interval":"60","theme":"dark","container_id":"dxy"})</script>""", height=470)

# CHECKLIST
st.divider()
st.markdown("### 🎯 CHECKLIST 7/7")
with st.container(border=True):
    t1 = st.checkbox("1. Tendencia")
    t2 = st.checkbox("2. Zona D1/S1/M1")
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

# DIARIO FIX - SIN LINEAS LARGAS
st.divider()
st.markdown("### 📂 DIARIO DE TRADING")
FILE = "trading.xlsx"

def cargar_excel_limpio():
    try:
        tmp = pd.read_excel(FILE, header=None)
        fila = 0
        for i in range(len(tmp)):
            txt = str(tmp.iloc[i].values)
            if "Fecha" in txt:
                fila = i
                break
        df = pd.read_excel(FILE, header=fila)
        # Borrar Unnamed sin linea larga
        cols_ok = []
        for c in df.columns:
            if "Unnamed" not in str(c):
                cols_ok.append(c)
        df = df[cols_ok]
        df = df.dropna(how='all')
        df = df.fillna("")
        # Arreglar fecha 2026-09-03 00:00:00 -> 03/09/2026
        if "Fecha" in df.columns:
            df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce')
            df["Fecha"] = df["Fecha"].dt.strftime("%d/%m/%Y")
            df["Fecha"] = df["Fecha"].fillna("")
        # Quitar ceros feos
        df = df.replace("0.0", "")
        df = df.replace("NaT", "")
        return df
    except:
        return pd.DataFrame({
            "Fecha": [datetime.now().strftime("%d/%m/%Y")],
            "Activo": ["MGC"],
            "Calendario": ["IPC"],
            "Killzone": [""],
            "Resultado": [""],
            "Comentario": [""]
        })

if "df_final" not in st.session_state:
    st.session_state.df_final = cargar_excel_limpio()

editado = st.data_editor(
    st.session_state.df_final,
    num_rows="dynamic",
    use_container_width=True,
    height=500,
    key="editor_fix"
)

st.session_state.df_final = editado

b1,b2 = st.columns(2)
with b1:
    if st.button("💾 GUARDAR", type="primary", use_container_width=True):
        editado.to_excel(FILE, index=False)
        st.success("Guardado!")
        st.balloons()
with b2:
    st.download_button("⬇️ DESCARGAR", editado.to_csv(index=False).encode('utf-8'), "diario.csv", use_container_width=True)
