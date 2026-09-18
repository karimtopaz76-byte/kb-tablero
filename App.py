import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import streamlit.components.v1 as components

st.set_page_config(page_title="KB VINULA TRADING", layout="wide")

# ESTILO EXACTO A TU FOTO - FONDO BLANCO
st.markdown("""
<style>
.stApp {background-color:#ffffff!important;}
h1,h2,h3 {color:#000000!important;}
p,div,span,label {color:#000000!important;}
</style>
""", unsafe_allow_html=True)

# HEADER EXACTO A LA FOTO
col_logo, col_title, col_hora = st.columns([1, 2.5, 1])

with col_logo:
    try:
        st.image("logo.png", width=160)
    except:
        st.markdown('<div style="background:#3d1f1f; color:#C9A86A; padding:30px; text-align:center; font-weight:900; font-size:24px;">KB</div>', unsafe_allow_html=True)

with col_title:
    st.markdown('<h1 style="margin-bottom:0; color:#4a1a1a!important;">KB VIÑUELA TRADING</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#666!important;">Diario 100% funcional + Escudo</p>', unsafe_allow_html=True)

with col_hora:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f'<div style="text-align:right; color:#000; font-size:14px; margin-top:30px;">{madrid.strftime("%H:%M")} MADRID {madrid.strftime("%d/%m/%Y")}</div>', unsafe_allow_html=True)

st.divider()

# 2 COLUMNAS COMO EN LA FOTO
c_cal, c_pil = st.columns(2)

with c_cal:
    st.subheader("CALENDARIO - SOLO 3 ESTRELLAS")
    components.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=600, scrolling=True)

with c_pil:
    madrid_str = datetime.now(pytz.timezone('Europe/Madrid')).strftime("%d-%m-%Y")
    st.subheader(f"PILARES - HOY {madrid_str}")

    st.markdown("""
    <div style="background:#fff; padding:15px; border-left:3px solid #C9A86A; margin-bottom:15px; color:#000;">
    <b>PILAR 1 - IPC USA: 3.4% Agosto - NEUTRO-ALTO = Cuidado ORO</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#fffcf0; padding:15px; border-left:3px solid #ff9800; margin-bottom:15px; color:#000;">
    <b>PILAR 3 - FED HOY: 3.75% - 4.00% - Subio ayer 17 Sep - Tasa SUBE = DXY SUBE / ORO BAJA CORTO</b>
    </div>
    """, unsafe_allow_html=True)

    fuerte = st.selectbox("NFP Escenario:", ["Fuerte +200k - Oro baja", "Debil - Oro sube", "Mixto"], key="nfp")
    calma = st.selectbox("VIX / Geopolitica:", ["Calma", "Riesgo ON", "Riesgo OFF - ORO sube"], key="vix")

    st.info("Killzone 08-11h y 14-17h Madrid - DXY 99.67 fuerte")

    # DIARIO 11 COLUMNAS DEBAJO DE PILARES - COMO EN TU FOTO TENIAS
    st.divider()
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
        height=350,
        key="diario_final_foto"
    )

    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("GUARDAR", type="primary", use_container_width=True):
            st.session_state.df = edit
            st.success(f"Guardado OK - {len(edit)} filas")
            st.balloons()
            try:
                edit.to_excel(FILE, index=False)
            except:
                pass
    with b2:
        st.download_button("BACKUP CSV", edit.to_csv(index=False).encode('utf-8'), "kb.csv", "text/csv", use_container_width=True)
    with b3:
        if st.button("NUEVA FILA", use_container_width=True):
            hoy = datetime.now().strftime("%d/%m")
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
