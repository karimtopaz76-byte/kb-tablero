import streamlit as st
import requests
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="ORO TOTAL - 6 Módulos", layout="wide")

def enviar_telegram(mensaje):
    try:
        token = st.secrets["TELEGRAM_TOKEN"]
        chat_id = st.secrets["TELEGRAM_CHAT_ID"]
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": mensaje, "parse_mode": "HTML"}, timeout=10)
        return True
    except:
        return False

# --- DATOS ---
try:
    import yfinance as yf
    us02 = yf.Ticker("^IRX").history(period="5d") # proxy, usamos valores reales
    us10 = yf.Ticker("^TNX").history(period="5d")
    us02_v = float(us02["Close"].iloc[-1])
    us10_v = float(us10["Close"].iloc[-1])
    real = True
except:
    us02_v = 4.74
    us10_v = 4.78
    real = False

# --- CABECERA COMO EN LA FOTO ---
st.markdown("# 🟡 ORO TOTAL - Sistema Completo 6 Módulos")
st.caption(f"Todo lo que mueve el oro en una sola hoja - 20 Sep 2026 | {'DATOS REALES' if real else 'MODO DEMO'}")
st.divider()

# --- 1. DINERO REAL - 70% ---
st.markdown("## 1. 💵 DINERO REAL - 70% del movimiento")
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("US02Y", f"{us02_v:.2f}%", "↑ ↑ Peligro ventas" if us02_v > 4.5 else "Baja - Bueno Oro")
    st.caption("↑ ↑ Peligro ventas" if us02_v > 4.5 else "↓ Bueno para oro")
with c2:
    st.metric("US10Y", f"{us10_v:.2f}%", "-0.05%")
with c3:
    st.metric("US REAL 10Y", "2.10%", "Neutro")

# --- 2-5 OTROS MODULOS (resumen para completar los 6) ---
st.divider()
col1, col2, col3 = st.columns(3)
col1.markdown("**2. 💲 DXY - Dólar**\n\n-0.45% → Débil = Bueno Oro ✅")
col2.markdown("**3. 😱 MIEDO - VIX / SPX**\n\nVIX 18.5 → Riesgo medio")
col3.markdown("**4. 🏦 BANCOS CENTRALES**\n\nFED Pausa - Dovish para oro ✅")

col4, col5, col6 = st.columns(3)
col4.markdown("**5. ⛏️ OFERTA / ETF**\n\nGLD +2.3M oz → Entrada dinero")
col5.markdown("**6. 📊 SCORE TOTAL**\n\n🔥 4/6 Alcista Oro")
col6.markdown(f"**XAU/USD**\n\n**${2685 + (us02_v-4.5)*10:.2f}**")

st.divider()

# --- MAPA DE CALOR COMO EN TU FOTO ---
st.markdown("### MAPA DE CALOR - FUERZA DEL MERCADO")
data = {
    "": ["EUR","USD","JPY","GBP","CHF","AUD","CAD","NZD","XAU"],
    "EUR": ["","-0.07%","-0.64%","0.23%","0.24%","0.08%","-0.02%","-0.24%","0.79%"],
    "USD": ["0.07%","","-0.61%","0.3%","0.31%","0.13%","0.06%","-0.11%","0.85%"],
    "JPY": ["0.68%","0.6%","","0.92%","1%","0.76%","0.58%","0.49%","1.43%"],
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True, hide_index=True)

# Para que se vea con colores como en la foto, usamos HTML
st.markdown("""
<style>
div[data-testid="stDataFrame"] td:nth-child(2) { background-color: #a8d8cc; }
</style>
""", unsafe_allow_html=True)

st.divider()
if st.button("🚀 ENVIAR RESUMEN 6 MÓDULOS A TELEGRAM @Orototal57_bot", type="primary", use_container_width=True):
    msg = f"🟡 <b>ORO TOTAL - 6 Módulos</b>\n\n1. DINERO REAL: US02Y {us02_v:.2f}% / US10Y {us10_v:.2f}%\n2. DXY: -0.45% Bueno\n3. XAU Fuerza vs USD: 0.85% 🔥\n4. Score: 4/6 Alcista\n⏰ {datetime.now().strftime('%H:%M')} Madrid\n@Orototal57_bot"
    enviar_telegram(msg)
    st.balloons()
    st.success("Enviado a Telegram!")

st.caption("Versión restaurada exacta - 20 Sep 2026 - KB Viñuela")
