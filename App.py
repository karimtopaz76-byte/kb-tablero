import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINULA TRADING", layout="wide")

c1,c2,c3 = st.columns([1,2,1])
with c1:
    st.markdown("## KB VINULA")
with c2:
    st.markdown("<h1 style='text-align:center'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
with c3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.info(madrid.strftime("%d/%m/%Y %H:%M") + " MADRID")

st.divider()

col_cal, col_pilar = st.columns([1.15, 1])
with col_cal:
    st.markdown("#### CALENDARIO - SOLO 3 ESTRELLAS")
    with st.container(border=True):
        components.html('<iframe src="https://sslecal2.forexprostools.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=55&lang=12&importance=3" width="100%" height="650" frameborder="0"></iframe>', height=670)

with col_pilar:
    st.markdown("#### PILARES - HOY")
    with st.container(border=True):
        st.error("PILAR 1 - IPC USA: 3.4% Agosto - NEUTRO-ALTO")
        st.warning("PILAR 3 - FED HOY: 3.75% - 4.00% - Subio 17 Sep - Tasa SUBE = ORO BAJA")
        st.info("Killzone 08-11h y 14-17h - DXY 99.67")

st.divider()
st.markdown("### DIARIO TRADING SMC - 11 COLUMNAS")
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

edit = st.data_editor(st.session_state.df_smc, num_rows="dynamic", use_container_width=True, height=450, key="ed_v54")

col1,col2 = st.columns(2)
with col1:
    if st.button("GUARDAR DIARIO", type="primary", use_container_width=True):
        st.session_state.df_smc = edit
        try:
            edit.to_excel(FILE, index=False, engine='openpyxl')
            st.success("Guardado OK!")
            st.balloons()
        except:
            st.success("Guardado en memoria!")
with col2:
    csv = edit.to_csv(index=False).encode('utf-8')
    st.download_button("DESCARGAR BACKUP CSV", csv, "kb_smc.csv", "text/csv", use_container_width=True)
