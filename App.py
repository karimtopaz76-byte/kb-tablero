import streamlit as st
import requests
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="KB VINUELA - ORO TOTAL 57", page_icon="🔥", layout="wide")

# --- TELEGRAM ---
def enviar_telegram(mensaje):
    try:
        token = st.secrets["TELEGRAM_TOKEN"]
        chat_id = st.secrets["TELEGRAM_CHAT_ID"]
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": mensaje, "parse_mode": "HTML"}
        r = requests.post(url, data=data, timeout=15)
        return r.status_code == 200
    except:
        return False

# --- DATOS REALES ---
def get_precio_real():
    try:
        import yfinance as yf
        gc = yf.Ticker("GC=F").history(period="5d")
        dx = yf.Ticker("DX-Y.NYB").history(period="5d")
        eu = yf.Ticker("EURUSD=X").history(period="5d")
        tnx = yf.Ticker("^TNX").history(period="5d")
        
        oro_p = float(gc["Close"].iloc[-1])
        oro_v = float((gc["Close"].iloc[-1] - gc["Close"].iloc[-2]) / gc["Close"].iloc[-2] * 100)
        dxy_v = float((dx["Close"].iloc[-1] - dx["Close"].iloc[-2]) / dx["Close"].iloc[-2] * 100) if not dx.empty else -0.3
        eur_v = float((eu["Close"].iloc[-1] - eu["Close"].iloc[-2]) / eu["Close"].iloc[-2] * 100) if not eu.empty else 0.3
        bono_v = float((tnx["Close"].iloc[-1] - tnx["Close"].iloc[-2]) / tnx["Close"].iloc[-2] * 100) if not tnx.empty else -0.5
        return oro_p, oro_v, dxy_v, eur_v, bono_v, True
    except:
        return 2685.50, 0.85, -0.45, 0.38, -0.80, False

oro_p, oro_v, dxy_v, eur_v, bono_v, real = get_precio_real()

# --- UI ---
st.title("🔥 KB VINUELA - ORO TOTAL 57")
st.caption(f"{'DATOS REALES' if real else 'MODO MANUAL'} | Madrid {datetime.now().strftime('%d/%m/%Y %H:%M')} | @Orototal57_bot")
st.divider()

# Si no hay datos reales, permite slider manual
if not real:
    oro_v = st.slider("Ajuste manual Fuerza ORO % (Yahoo caído)", -2.0, 2.0, oro_v, 0.05)

c1, c2, c3, c4 = st.columns(4)
c1.metric("XAU/USD", f"${oro_p:.2f}", f"{oro_v:.2f}%")
c2.metric("DXY", f"{dxy_v:.2f}%", "Débil=BUENO Oro")
c3.metric("EUR/USD", f"{eur_v:.2f}%")
c4.metric("Bonos 10Y", f"{bono_v:.2f}%", "Bajando=BUENO Oro")

# SCORE 5/5
score = 0
if oro_v > 0.5: score+=1
if dxy_v < -0.1: score+=1
if eur_v > 0.1: score+=1
if bono_v < 0: score+=1
if 8 <= datetime.now().hour <= 21: score+=1

st.divider()
if score >= 4:
    st.success(f"🔥 SETUP {score}/5 PERFECTO - ORO FUERTE {oro_v:.2f}% - BUSCA LONGS")
    senal = "LONG"
elif score <= 1:
    st.error(f"🔻 SETUP {score}/5 DÉBIL - ORO DÉBIL {oro_v:.2f}% - BUSCA SHORTS")
    senal = "SHORT"
else:
    st.warning(f"⏳ SETUP {score}/5 MEDIO - ESPERA")
    senal = "ESPERA"

# TABLA COMPLETA
st.subheader("🌍 Fuerza Total")
df = pd.DataFrame({
    "Activo": ["XAU/USD", "DXY", "EUR/USD", "GBP/USD", "US10Y"],
    "Var %": [f"{oro_v:.2f}%", f"{dxy_v:.2f}%", f"{eur_v:.2f}%", "+0.20%", f"{bono_v:.2f}%"],
    "Para Oro": ["🔥 FUERTE" if oro_v>0.5 else "Débil", "✅ Alcista Oro" if dxy_v<0 else "❌ Bajista", "✅ Alcista", "➖ Neutro", "✅ Alcista" if bono_v<0 else "❌ Bajista"],
})
st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()
col1, col2 = st.columns(2)
with col1:
    if st.button(f"🚀 ENVIAR SEÑAL {senal} A TELEGRAM", type="primary", use_container_width=True):
        msg = f"🏆 <b>ORO TOTAL 57 - {senal} {score}/5</b>\n\n💰 XAU: ${oro_p:.2f} ({oro_v:.2f}%)\n📉 DXY: {dxy_v:.2f}%\n📈 EUR: {eur_v:.2f}%\n📊 Bonos: {bono_v:.2f}%\n⏰ {datetime.now().strftime('%H:%M')} Madrid\n\n🎯 {senal}"
        if enviar_telegram(msg):
            st.balloons()
            st.success("Enviado!")
with col2:
    if st.button("🧪 PROBAR TELEGRAM", use_container_width=True):
        enviar_telegram(f"🧪 TEST ORO TOTAL 57\n${oro_p:.2f} | {oro_v:.2f}% | Score {score}/5")
        st.success("Test enviado")
