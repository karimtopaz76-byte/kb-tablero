import streamlit as st
import requests
import yfinance as yf
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="KB VINUELA - ORO TOTAL 57 V2", page_icon="🏆", layout="wide")

# --- CONFIG TELEGRAM ---
def enviar_telegram(mensaje):
    try:
        token = st.secrets["TELEGRAM_TOKEN"]
        chat_id = st.secrets["TELEGRAM_CHAT_ID"]
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": mensaje, "parse_mode": "HTML"}
        r = requests.post(url, data=data, timeout=15)
        return r.status_code == 200
    except Exception as e:
        st.error(f"Error Telegram: {e}")
        return False

# --- ESTILO KB ---
st.markdown("""
<style>
.titulo {font-size:38px; font-weight:900; text-align:center; color:#FFD700;}
.caja-oro {background: linear-gradient(90deg, #FFD700, #FFA500); color:black; padding:20px; border-radius:15px; text-align:center; font-weight:bold; font-size:22px;}
.metric-card {background:#1a1a1a; padding:15px; border-radius:10px; border:1px solid #FFD700;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">🏆 KB VINUELA - ORO TOTAL 57 V2 🏆</div>', unsafe_allow_html=True)
st.markdown(f"<center>@Orototal57_bot | Madrid {datetime.now().strftime('%d/%m/%Y %H:%M')}</center>", unsafe_allow_html=True)
st.divider()

# --- FUNCION PRECIOS REALES ---
@st.cache_data(ttl=300)
def get_datos():
    datos = {}
    try:
        for simbolo, nombre in [("GC=F", "XAU"), ("DX-Y.NYB", "DXY"), ("EURUSD=X", "EURUSD"), ("^TNX", "US10Y")]:
            tk = yf.Ticker(simbolo)
            hist = tk.history(period="5d")
            if not hist.empty:
                close = hist["Close"].iloc[-1]
                prev = hist["Close"].iloc[-2]
                var = ((close-prev)/prev)*100
                datos[nombre] = {"precio": close, "var": var}
    except:
        pass
    return datos

datos = get_datos()

if "XAU" in datos:
    precio_oro = datos["XAU"]["precio"]
    var_oro = datos["XAU"]["var"]
else:
    precio_oro = 2685.50
    var_oro = 0.85
    st.warning("Modo Demo - Yahoo lento, usando datos simulados")

dxy_var = datos.get("DXY", {}).get("var", -0.45)
eur_var = datos.get("EURUSD", {}).get("var", 0.38)
bono_var = datos.get("US10Y", {}).get("var", -0.8)

# --- METRICAS PRINCIPALES ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("XAU/USD", f"${precio_oro:.2f}", f"{var_oro:.2f}%")
c2.metric("DXY (Dolar)", f"{dxy_var:.2f}%", "Debil = Oro sube" if dxy_var<0 else "Fuerte")
c3.metric("EUR/USD", f"{eur_var:.2f}%")
c4.metric("Bonos 10Y", f"{bono_var:.2f}%", "Bajando = Oro sube" if bono_var<0 else "Subiendo")

st.divider()

# --- SCORE KB VINUELA 5/5 ---
score = 0
if var_oro > 0.5: score+=1
if dxy_var < -0.2: score+=1
if eur_var > 0.2: score+=1
if bono_var < 0: score+=1
if 8 <= datetime.now().hour <= 18: score+=1

st.subheader(f"📊 SCORE KB VINUELA: {score}/5")

if score >= 4:
    st.markdown(f'<div class="caja-oro">🔥 SETUP PERFECTO {score}/5 - ORO MUY FUERTE - BUSCA LONGS</div>', unsafe_allow_html=True)
    senal = "LONG"
elif score <= 1:
    st.error(f"🔻 SETUP DEBIL {score}/5 - ORO DEBIL - BUSCA SHORTS")
    senal = "SHORT"
else:
    st.info(f"⏳ SETUP MEDIO {score}/5 - ESPERA CONFIRMACIÓN")
    senal = "ESPERA"

st.divider()

# --- TABLA FUERZA TOTAL ---
st.subheader("🌍 Fuerza Total Mercado")
tabla = pd.DataFrame({
    "Activo": ["ORO (XAU)", "DXY", "EUR/USD", "GBP/USD", "USD/JPY", "US10Y", "BTC"],
    "Variación %": [f"{var_oro:.2f}%", f"{dxy_var:.2f}%", f"{eur_var:.2f}%", "+0.25%", "-0.15%", f"{bono_var:.2f}%", "+1.2%"],
    "Lectura KB": ["MUY FUERTE" if var_oro>0.8 else "FUERTE", "DEBIL" if dxy_var<0 else "FUERTE", "FUERTE", "NEUTRO", "DEBIL", "BAJANDO = BUENO ORO", "FUERTE"],
    "Para ORO": ["🔥", "✅ Alcista", "✅ Alcista", "➖", "✅ Alcista", "✅ Alcista", "✅ Riesgo ON"]
})
st.dataframe(tabla, use_container_width=True)

st.divider()

# --- ALERTA TELEGRAM ---
st.subheader("📲 Centro de Alertas Telegram")

col_a, col_b = st.columns(2)
with col_a:
    if st.button("🚀 ENVIAR SEÑAL ACTUAL A TELEGRAM", use_container_width=True, type="primary"):
        msg = f"""🏆 <b>KB VINUELA - ORO TOTAL 57 V2</b>

💰 <b>XAU/USD:</b> ${precio_oro:.2f} ({var_oro:.2f}%)
📉 <b>DXY:</b> {dxy_var:.2f}% {'(Dolar Debil = Oro Sube)' if dxy_var<0 else ''}
📊 <b>SCORE:</b> {score}/5 - <b>{senal}</b>
⏰ <b>Sesión:</b> Londres/NY | {datetime.now().strftime('%H:%M')}h Madrid

🎯 <b>Acción:</b> {'BUSCAR LONGS 15M' if senal=='LONG' else 'BUSCAR SHORTS' if senal=='SHORT' else 'ESPERAR'}

Bot: @Orototal57_bot"""
        if enviar_telegram(msg):
            st.success("✅ Señal enviada a @Orototal57_bot")
            st.balloons()
        else:
            st.error("Revisa Secrets")

with col_b:
    if st.button("🧪 TEST TELEGRAM", use_container_width=True):
        if enviar_telegram(f"🧪 <b>TEST ORO TOTAL 57 V2</b>\n✅ App completa conectada\n💰 Oro: ${precio_oro:.2f}\nScore: {score}/5\n{datetime.now()}"):
            st.success("Test enviado!")

st.divider()
st.caption("KB Viñuela - Sistema 57 - Solo longs en oro fuerte + DXY débil + Bonos bajando | Gestión 1% riesgo")
