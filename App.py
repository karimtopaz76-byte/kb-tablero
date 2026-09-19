import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="KB VINUELA - Oro Total", page_icon="🔥", layout="wide")

# --- FUNCION TELEGRAM ---
def enviar_telegram(mensaje):
    try:
        token = st.secrets["TELEGRAM_TOKEN"]
        chat_id = st.secrets["TELEGRAM_CHAT_ID"]
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": mensaje, "parse_mode": "HTML"}
        requests.post(url, data=data, timeout=10)
        return True
    except Exception as e:
        st.error(f"Error Telegram: {e}")
        return False

# --- ESTILO ---
st.markdown("""
<style>
.caja-ok {background:#00ff88; color:black; padding:15px; border-radius:10px; font-weight:bold; text-align:center; font-size:18px;}
.caja-warn {background:#ffaa00; color:black; padding:15px; border-radius:10px; font-weight:bold; text-align:center;}
</style>
""", unsafe_allow_html=True)

st.title("🔥 KB VINUELA - ORO TOTAL 57")
st.write(f"Conectado a tu bot: @Orototal57_bot - {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# --- AQUI VA TU LOGICA DE ORO ---
# Simulamos por ahora, luego conectamos tu API real
xau_fuerza = st.slider("Fuerza del ORO vs USD (simulación, luego va automático)", 0.0, 1.5, 0.85, step=0.05)

if xau_fuerza >= 0.80:
    st.markdown(f'<div class="caja-ok">🔥 ORO MUY FUERTE +{xau_fuerza}% vs USD - BUSCA LONGS</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("📲 ENVIAR ALERTA A TELEGRAM", use_container_width=True):
        mensaje = f"""🔥 <b>KB VINUELA - ORO TOTAL</b>

💰 XAU/USD: <b>+{xau_fuerza}%</b> vs USD
📊 Estado: <b>MUY FUERTE</b>
✅ Acción: <b>BUSCAR LONGS - Setup 5/5</b>
⏰ {datetime.now().strftime('%d/%m %H:%M')}h

Bot: @Orototal57_bot"""
        
        if enviar_telegram(mensaje):
            st.success("✅ Alerta enviada a Telegram! Revisa tu móvil.")
            st.balloons()
        else:
            st.error("Revisa Secrets en Streamlit")

elif xau_fuerza <= -0.80:
    st.markdown(f'<div class="caja-warn">⚠️ ORO MUY DEBIL {xau_fuerza}% - BUSCA SHORTS</div>', unsafe_allow_html=True)
else:
    st.info(f"Oro neutro: {xau_fuerza}% - Esperando setup")

st.divider()
st.write("---")
if st.button("🧪 PROBAR TELEGRAM (test)"):
    if enviar_telegram("🧪 TEST KB VINUELA - Si ves esto, Telegram funciona al 100% 🔥"):
        st.success("Mensaje de prueba enviado! Mira Telegram")
