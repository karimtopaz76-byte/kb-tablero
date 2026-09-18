import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINULA TRADING", layout="wide")

st.title("KB VINULA TRADING")
madrid = datetime.now(pytz.timezone('Europe/Madrid'))
st.write("MADRID - " + str(madrid.day) + "/" + str(madrid.month) + "/" + str(madrid.year))

st.divider()

# PILARES ACTUALIZADOS HOY
col1, col2 = st.columns(2)
with col1:
    st.error("PILAR 1 - IPC USA: 3.4% Agosto")
    st.warning("PILAR 3 - FED HOY: 3.75% - 4.00% - Subio ayer 17 Sep")
with col2:
    st.info("Killzone 08-11h y 14-17h Madrid - DXY 99.67 fuerte - Tasa SUBE = Oro baja corto")

st.divider()

# DIARIO 11 COLUMNAS - TU PEDIDO
st.subheader("DIARIO TRADING - 11 COLUMNAS")
FILE = "trading.xlsx"

def cargar():
    try:
        df = pd.read_excel(FILE)
        if df.empty:
            raise ValueError("vacio")
        cols = ["Fecha","Activo","Calendario economico","Nivel de interes","Rechazo H4","BOS H1","FVG 15m","FVG 5m","Tamano operacion","TP","SL"]
        for c in cols:
            if c not in df.columns:
                df[c] = ""
        return df
    except:
        return pd.DataFrame({
            "Fecha": ["18/09/2026"],
            "Activo": ["XAUUSD"],
            "Calendario economico": ["IPC 3.4% / FED 4%"],
            "Nivel de interes": ["3.75%-4.00%"],
            "Rechazo H4": ["Si - Mecha larga"],
            "BOS H1": ["Si alcista"],
            "FVG 15m": ["2650-2652"],
            "FVG 5m": ["Si entrada"],
            "Tamano operacion": ["0.01"],
            "TP": ["2660"],
            "SL": ["2645"]
        })

if "df" not in st.session_state:
    st.session_state.df = cargar()

edit = st.data_editor(
    st.session_state.df,
    num_rows="dynamic",
    use_container_width=True,
    height=400,
    key="diario_final"
)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("GUARDAR", type="primary", use_container_width=True):
        st.session_state.df = edit
        st.success("Guardado OK - " + str(len(edit)) + " filas")
        st.balloons()
        try:
            edit.to_excel(FILE, index=False)
        except:
            pass

with c2:
    csv = edit.to_csv(index=False).encode('utf-8')
    st.download_button("BACKUP CSV", csv, "kb.csv", "text/csv", use_container_width=True)

with c3:
    if st.button("NUEVA FILA", use_container_width=True):
        hoy = str(datetime.now().day) + "/" + str(datetime.now().month)
        nueva = pd.DataFrame({
            "Fecha": [hoy],
            "Activo": ["XAUUSD"],
            "Calendario economico": [""],
            "Nivel de interes": ["3.75%-4.00%"],
            "Rechazo H4": [""],
            "BOS H1": [""],
            "FVG 15m": [""],
            "FVG 5m": [""],
            "Tamano operacion": ["0.01"],
            "TP": [""],
            "SL": [""]
        })
        st.session_state.df = pd.concat([edit, nueva], ignore_index=True)
        st.rerun()
