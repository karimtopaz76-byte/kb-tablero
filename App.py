import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="ORO TOTAL 57", page_icon="🔥", layout="centered")

def enviar_telegram(mensaje):
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": mensaje, "parse_mode": "HTML"}
    r = requests.post(url, data=data, timeout=10)
    return r.status_code == 200

st.title("🔥 KB VINUELA - ORO TOTAL 57")
st.write(f"Madrid {datetime.now().strftime('%H:%M')} | @Orototal57_bot")

fuerza = st.slider("Fuerza ORO vs USD %", -2.0, 2.0, 0.85, 0.05)

if fuerza >= 0.8:
    st.success(f"🔥 ORO FUERTE {fuerza}% - BUSCA LONG")
    tipo = "LONG"
elif fuerza <= -0.8:
    st.error(f"🔻 ORO DEBIL {fuerza}% - BUSCA SHORT")
    tipo = "SHORT"
else:
    st.info(f"⏳ RANGO {fuerza}% - ESPERA")
    tipo = "ESPERA"

if st.button(f"📲 ENVIAR ALERTA {tipo} A TELEGRAM", type="primary", use_container_width=True):
    msg = f"🏆 <b>ORO TOTAL 57 - {tipo}</b>\n💰 Fuerza: {fuerza}%\n⏰ {datetime.now().strftime('%H:%M')}h Madrid\n🎯 KB Viñuela Sistema 57"
    if enviar_telegram(msg):
        st.balloons()
        st.success("¡Enviado a Telegram!")

if st.button("🧪 PROBAR TELEGRAM"):
    enviar_telegram("🧪 TEST OK - ORO TOTAL 57 funcionando")
    st.success("Prueba enviada")

st.divider()
st.caption("Si esto te funciona, ahora le añadimos el precio real y la tabla completa")
