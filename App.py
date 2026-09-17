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
    except: st.markdown("<div class='card' style='height:130px;display:flex;align-items:center;justify-content:center'><h2 class='gold'>KB</h2></div>", unsafe_allow_html=True)
with h2:
    st.markdown("<h1 style='margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        madrid = datetime.now(pytz.timezone('Europe/Madrid'))
        st.markdown(f"<div class='card' style='text-align:center'><b>MADRID</b><br><h2 style='margin:0'>{madrid.strftime('%H:%M:%S')}</h2><span class='gold'>MERCADO ABIERTO</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card' style='text-align:center'><b>XAUUSD</b>", unsafe_allow_html=True)
        components.html("""<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><script src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>{"symbol":"OANDA:XAUUSD","width":"100%","height":80,"locale":"es","colorTheme":"dark","isTransparent":true}</script></div>""", height=85)
        st.markdown("</div>", unsafe_allow_html=True)
with h3:
    st.markdown("<div class='card'><b class='gold'>REGLA DE ORO</b><br>Sin 7/7 no hay trade</div>", unsafe_allow_html=True)

st.divider()

# CALENDARIO + PILARES
f1,f2 = st.columns([1.2,1])
with f1:
    st.markdown("*📅 CALENDARIO ECONOMICO*")
    with st.container(border=True):
        components.html("""<div style="height:320px"><script src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme":"dark","isTransparent":true,"width":"100%","height":"320","importanceFilter":"-1,0,1","currencyFilter":"USD"}</script></div>""", height=330)
with f2:
    st.markdown("*🏛️ PILARES FUNDAMENTAL*")
    with st.container(border=True):
        st.progress(70, text="IPC")
        st.progress(45, text="NFP")
        a,b = st.columns(2)
        a.metric("DXY","103.2","-0.3%")
        b.metric("VIX","18.5")

# GRAFICOS
st.divider()
g1,g2 = st.columns(2)
with g1:
    st.markdown("*📈 XAUUSD*")
    components.html("""<div id="kb_xau_fix" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","theme":"dark","container_id":"kb_xau_fix"})</script>""", height=520)
with g2:
    st.markdown("*📉 DXY*")
    components.html("""<div id="kb_dxy_fix" style="height:500px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"TVC:DXY","interval":"60","theme":"dark","container_id":"kb_dxy_fix"})</script>""", height=520)

# CHECKLIST
st.divider()
st.markdown("### 🎯 CHECKLIST FRANCOTIRADOR")
with st.container(border=True):
    t1 = st.checkbox("1. Tendencia Diaria")
    t2 = st.checkbox("2. Zona D1,S1,M1")
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

# DIARIO - FIX DE TU FOTO
st.divider()
st.markdown("### 📂 DIARIO DE TRADING")
st.info("👇 Toca cualquier casilla y escribe. + abajo para nueva fila.")

FILE = "trading.xlsx"

def cargar_excel_limpio():
    try:
        tmp = pd.read_excel(FILE, header=None)
        fila_header = 0
        for i in range(len(tmp)):
            texto = " ".join([str(x) for x in tmp.iloc[i].values])
            if "Fecha" in texto:
                fila_header = i
                break
        df = pd.read_excel(FILE, header=fila_header)
        df = df.loc[:, ~df.columns.astype(str).str.contains('Unnamed', na=False)]
        df = df.dropna(how='all')
        df = df.fillna("")
        # ARREGLO DE FECHA SIN TRY ANIDADO
        if "Fecha" in df.columns:
            df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce')
            df["Fecha"] = df["Fecha"].dt.strftime("%d/%m/%Y")
            df["Fecha"] = df["Fecha"].fillna("").replace("NaT", "")
        df = df.replace([0, 0.0, "0.0"], "")
        
            
    
        return df
    except:
        return pd.DataFrame({
            "Fecha": [datetime.now().strftime("%d/%m/%Y")],
            "Activo": ["MGC"],
            "Calendario Economico": [""],
            "Killzone 08h": [""],
            "killzone 13h": [""],
            "tamaño": [0.25],
            "Resultado": [""],
            "Comentario": [""]
        })

if "df_kb_final" not in st.session_state:
    st.session_state.df_kb_final = cargar_excel_limpio()

editado = st.data_editor(
    st.session_state.df_kb_final,
    num_rows="dynamic",
    use_container_width=True,
    height=500,
    key="editor_final_completo"
)

st.session_state.df_kb_final = editado

b1,b2 = st.columns(2)
with b1:
    if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
        editado.to_excel(FILE, index=False)
        st.success("Guardado!")
        st.balloons()
with b2:
    st.download_button("⬇️ DESCARGAR", editado.to_csv(index=False).encode('utf-8'), "diario_KB.csv", "text/csv", use_container_width=True)
