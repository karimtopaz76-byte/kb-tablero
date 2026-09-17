import streamlit as st
from datetime import datetime
import pytz, pandas as pd
st.set_page_config(page_title="KB Trading", layout="centered")
st.markdown("<style>.stApp{background:#0a0a0a;} h1,h2{color:#D4AF37 !important;}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'>KB VINUELA TRADING</h1>", unsafe_allow_html=True)
sevilla = pytz.timezone('Europe/Madrid')
ahora = datetime.now(sevilla)
st.caption(f"Sevilla {ahora.strftime('%H:%M')} | NY 10:00-13:00")
st.header("BLOQUE A")
news = st.selectbox("Noticias rojas?", ["No - Verde", "SI ROJO"])
st.header("BLOQUE B - 5 pasos")
c1 = st.checkbox("1. Zona azul 6m tocada")
c2 = st.checkbox("2. Rechazo H4")
c3 = st.checkbox("3. BOS H1")
c4 = st.checkbox("4. FVG 15m")
c5 = st.checkbox("5. SL puesto")
if "No" in news and c1 and c2 and c3 and c4 and c5:
    st.success("TODO VERDE - ENTRAR CORTO")
else:
    st.warning("Esperando setup")
if "trades" not in st.session_state:
    st.session_state.trades = []
with st.form("f"):
    e = st.number_input("Entrada", value=2580.0)
    s = st.number_input("SL", value=2590.0)
    t = st.number_input("TP", value=2550.0)
    rr = abs(t-e)/abs(e-s) if e!=s else 0
    st.metric("RR", f"1:{rr:.2f}")
    res = st.selectbox("Resultado", ["Pendiente","Ganado","Perdido"])
    nota = st.text_input("Nota", value="FVG + azul 6m")
    ok = st.form_submit_button("Guardar Trade")
    if ok:
        st.session_state.trades.append({"Fecha":ahora.strftime("%d/%m"), "E":e, "SL":s, "TP":t, "RR":f"1:{rr:.2f}", "Res":res, "Nota":nota})
        st.success("Guardado")
if st.session_state.trades:
    st.dataframe(pd.DataFrame(st.session_state.trades))
