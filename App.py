import streamlit as st
from datetime import datetime
import pytz
st.set_page_config(page_title="KB VINUELA TRADING", layout="wide")
madrid = datetime.now(pytz.timezone('Europe/Madrid'))
hora = f"{madrid.hour:02d}:{madrid.minute:02d} MADRID - {madrid.day:02d}/{madrid.month:02d}/{madrid.year}"
c1, c2, c3 = st.columns([1, 2, 1])
with c1:
    st.image("logo.png", width=140)
with c2:
    st.title("KB VINUELA TRADING")
with c3:
    st.markdown(f'<div style="background:black; color:#C9A86A; border:1.5px solid #C9A86A; border-radius:8px; padding:12px; text-align:center; font-weight:bold;">{hora}</div>', unsafe_allow_html=True)
st.divider()
st.subheader("CALENDARIO - SOLO 3 ESTRELLAS")
st.components.v1.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=650, scrolling=True)
st.subheader(f"PILARES - {hora}")
st.error("PILAR 1 IPC 3.4% - Cuidado ORO")
st.warning("PILAR 3 FED 3.75-4% - DXY 99.67 FUERTE")
st.success("PILAR 2 NFP >200k = ORO BAJA")
st.info("KILLZONE 08-11h Londres | 14-17h NY")
