import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINULA TRADING", layout="wide")

st.markdown("<style>.stApp{background:#0A0A0A;color:#EAEAEA}.card{background:#151515;border:1px solid #2A2A2A;border-radius:12px;padding:12px}</style>", unsafe_allow_html=True)

# HEADER CORTO
c1,c2 = st.columns([1,3])
with c1:
    try: st.image("logo.png", width=110)
    except: st.markdown("### KB")
with c2:
    st.markdown("## KB VINULA TRADING - DIARIO DE TRADING")

# --- ESTA ES LA PARTE QUE ARREGLA TU FOTO ---
FILE = "trading.xlsx"

def cargar_y_limpiar():
    try:
        # Carga tu excel tal cual lo tienes
        df = pd.read_excel(FILE)
        # Limpia TODO lo que sale como None en tu foto
        df = df.fillna("") 
        # Si la columna Fecha viene con hora, la deja solo fecha
        if "Fecha" in df.columns:
            df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce').dt.strftime("%d/%m/%Y")
            df["Fecha"] = df["Fecha"].fillna("")
        return df
    except:
        # Si no hay excel, crea uno limpio desde cero
        return pd.DataFrame({
            "Fecha": [datetime.now().strftime("%d/%m/%Y")],
            "Activo": ["XAUUSD"],
            "Calendario Economico": ["IPC 14:30"],
            "Killzone 08h-11h": [""],
            "killzone 14h-17h": [""],
            "Checklist 7/7": ["7/7"],
            "Resultado": ["TP"],
            "Comentario": [""]
        })

if "df" not in st.session_state:
    st.session_state.df = cargar_y_limpiar()

st.success("👇 Ahora toca cualquier casilla y escribe con tu teclado. Dale al + de abajo para nueva fila.")

# TABLA QUE SI DEJA ESCRIBIR EN TABLET
editado = st.data_editor(
    st.session_state.df,
    num_rows="dynamic",  # Esto activa el + para añadir filas
    use_container_width=True,
    height=500,
    key="diario_kb"
)

st.session_state.df = editado

col1, col2 = st.columns(2)
with col1:
    if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
        editado.to_excel(FILE, index=False)
        st.success("Guardado!")
        st.balloons()
with col2:
    st.download_button("⬇️ DESCARGAR COPIA", editado.to_csv(index=False).encode('utf-8'), "diario_kb.csv", use_container_width=True)

st.divider()
st.markdown("#### Añadir rápido:")
with st.form("rapido", clear_on_submit=True):
    f1,f2,f3 = st.columns(3)
    fecha = f1.text_input("Fecha", datetime.now().strftime("%d/%m/%Y"))
    activo = f2.text_input("Activo", "XAUUSD")
    cal = f3.text_input("Calendario", "Sin noticias")
    com = st.text_input("Comentario")
    if st.form_submit_button("AÑADIR"):
        nueva = pd.DataFrame([{"Fecha":fecha,"Activo":activo,"Calendario Economico":cal,"Killzone 08h-11h":"","killzone 14h-17h":"","Checklist 7/7":"7/7","Resultado":"Pendiente","Comentario":com}])
        st.session_state.df = pd.concat([st.session_state.df, nueva], ignore_index=True)
        st.rerun()
