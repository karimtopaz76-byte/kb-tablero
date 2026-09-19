import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINULA TRADING", layout="wide")

# ESTILO DORADO
st.markdown("""
<style>
.gold {color:#C9A86A!important; font-weight:900; text-align:center; letter-spacing:2px;}
.logo-box {background:#1a0f0f; border:2px solid #C9A86A; padding:10px; text-align:center; border-radius:8px;}
</style>
""", unsafe_allow_html=True)

# CABECERA CON LOGO + DORADO
c1,c2,c3 = st.columns([1,2,1])
with c1:
    try:
        st.image("logo.png", width=150)
    except:
        st.markdown('<div class="logo-box"><div style="color:#C9A86A; font-size:32px; font-weight:900;">KB</div><div style="color:#C9A86A; font-size:10px;">VIÑUELA TRADING</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown("<h1 class='gold'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#C9A86A;'>FRANCOTIRADOR ORO / DXY</p>", unsafe_allow_html=True)

with c3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    fecha_txt = str(madrid.day) + "/" + str(madrid.month) + "/" + str(madrid.year) + " " + str(madrid.hour) + ":" + str(madrid.minute)
    st.info(fecha_txt + " MADRID")

st.divider()

# CALENDARIO + PILARES
col_cal, col_pilar = st.columns([1.15, 1])

with col_cal:
    st.markdown("#### CALENDARIO - SOLO 3 ESTRELLAS")
    with st.container(border=True):
        components.html('<iframe src="https://sslecal2.forexprostools.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=55&lang=12&importance=3" width="100%" height="650" frameborder="0"></iframe>', height=670)

with col_pilar:
    st.markdown("#### fundamental - HOY 18-09-2026")
    with st.container(border=True):
        st.error("1 - IPC USA: 3.4% Agosto - NEUTRO-ALTO = Cuidado ORO")
        st.warning("3 - FED HOY: 3.75% - 4.00% - Subio ayer 17 Sep - Tasa SUBE = DXY SUBE / ORO BAJA CORTO")
        st.selectbox("NFP", ["Fuerte +200k - Oro baja","Medio","Debil <100k - Oro sube"], label_visibility="collapsed")
        st.selectbox("GEO", ["Calma","Tension media","Guerra - Oro sube"], label_visibility="collapsed")
        st.info("Killzone 08-11h y 14-17h Madrid - DXY 99.67 fuerte")

st.divider()

# DXY + NOTICIAS
st.markdown("#### NOTICIAS + DXY")
components.html('<div style="background:#000; border:2px solid #FFD60A; border-radius:8px; padding:10px; color:#FFD60A; font-family:monospace"><marquee scrollamount="7">FED 3.75-4.00% | IPC 3.4% | DXY 99.67 FUERTE = ORO PRESIONADO | KILLZONE 14-17h</marquee></div>', height=60)

col_tv, col_dxy = st.columns([1,1])
with col_tv:
    with st.container(border=True):
        st.link_button("IPC USA DETALLE", "https://www.investing.com/economic-calendar/cpi-733", use_container_width=True)
        st.link_button("FED RATE DECISION", "https://www.investing.com/economic-calendar/interest-rate-decision-168", use_container_width=True)
        st.link_button("FOREX NEWS", "https://www.investing.com/news/forex-news", use_container_width=True)
with col_dxy:
    components.html('<div id="dxy" style="height:450px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"container_id":"dxy","width":"100%","height":450,"symbol":"TVC:DXY","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es"});</script>', height=470)

st.divider()
st.markdown("#### XAUUSD")
components.html('<div id="xau" style="height:550px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"container_id":"xau","width":"100%","height":550,"symbol":"OANDA:XAUUSD","interval":"15","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es"});</script>', height=570)

st.divider()
st.markdown("### CHECKLIST 7/7")
with st.container(border=True):
    chk1 = st.checkbox("1. Calendario econòmico y eventos mundiales")
    chk2 = st.checkbox("2. DXY analizado")
    chk3 = st.checkbox("3. zonas de interes D1 S1 M1 Tocado")
    chk4 = st.checkbox("4. Rechazo de vila de H4 cierre con mecha ")
    chk5 = st.checkbox("5. BOS H1 cierre con cuerpo")
    chk6 = st.checkbox("6. Retrazo a FVG 15M")
    chk7 = st.checkbox("7. Psicologia OK")
    total = sum([chk1,chk2,chk3,chk4,chk5,chk6,chk7])
    st.progress(total/7, text=str(total)+"/7")
    if total == 7:
        st.success("EJECUTA ORDEN")
        st.balloons()

# DIARIO 11 COLUMNAS - TODO JUNTO
st.divider()
st.markdown("### DIARIO TRADING ")
FILE="trading.xlsx"

def cargar():
    try:
        df = pd.read_excel(FILE)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed', na=False)]
        df = df.dropna(how='all')
        if df.empty:
            raise ValueError("vacio")
        cols = ["Fecha","Activo","Calendario economico","Nivel de interes","Rechazo H4","BOS H1","FVG 15m","FVG 5m","Tamano operacion","TP","SL"]
        for c in cols:
            if c not in df.columns:
                df[c] = ""
        return df[cols].fillna("")
    except:
        return pd.DataFrame({
            "Fecha":["18/09/2026"],
            "Activo":["XAUUSD"],
            "Calendario economico":["IPC 3.4% / FED 4%"],
            "Nivel de interes":["3.75%-4.00%"],
            "Rechazo H4":["Si - Mecha larga"],
            "BOS H1":["Si alcista"],
            "FVG 15m":["2650-2652"],
            "FVG 5m":["Si entrada"],
            "Tamano operacion":["0.01"],
            "TP":["2660"],
            "SL":["2645"]
        })

if "df_smc" not in st.session_state:
    st.session_state.df_smc = cargar()

edit = st.data_editor(st.session_state.df_smc, num_rows="dynamic", use_container_width=True, height=450, key="ed_final")

col1,col2,col3 = st.columns(3)
with col1:
    if st.button("GUARDAR DIARIO", type="primary", use_container_width=True):
        st.session_state.df_smc = edit
        try:
            edit.to_excel(FILE, index=False, engine='openpyxl')
            st.success("Guardado OK")
            st.balloons()
        except:
            st.success("Guardado en memoria")
with col2:
    csv = edit.to_csv(index=False).encode('utf-8')
    st.download_button("BACKUP CSV", csv, "kb_smc.csv", "text/csv", use_container_width=True)
with col3:
    if st.button("NUEVA FILA", use_container_width=True):
        ahora = datetime.now()
        fecha_nueva = str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year)
        nueva = pd.DataFrame({
            "Fecha":[fecha_nueva],
            "Activo":["XAUUSD"],
            "Calendario economico":[""],
            "Zona de interes":["3.75%-4.00%"],
            "Rechazo H4":[""],
            "BOS H1":[""],
            "FVG 15m":[""],
            "FVG 5m":[""],
            "Tamano operacion":["0.01"],
            "TP":[""],
            "SL":[""]
        })
        st.session_state.df_smc = pd.concat([edit, nueva], ignore_index=True)
        st.rerun()
