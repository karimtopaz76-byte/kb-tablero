import streamlit as st
import requests

st.set_page_config(page_title="ORO TOTAL v57 - Live + Alertas", layout="wide")
st.title("🟡 ORO TOTAL v57 - Live + Telegram")
st.caption("Datos en vivo + Alertas automáticas")

# === FUNCION DATOS EN VIVO QUE NO FALLA ===
def get_live(ticker):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=2d"
        r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, timeout=5).json()
        close = r['chart']['result'][0]['indicators']['quote'][0]['close']
        last = close[-1]
        prev = close[-2] if len(close)>1 and close[-2] else last
        chg = ((last-prev)/prev)*100 if prev else 0
        return round(last,2), round(chg,2)
    except:
        return None, 0

# === TRAE DATOS ===
us02y, c1 = get_live("^IRX")
us10y, c2 = get_live("^TNX")
dxy, c3 = get_live("DX-Y.NYB")
vix, c4 = get_live("^VIX")
brent, c5 = get_live("BZ=F")
oro, c6 = get_live("GC=F")
btc, c7 = get_live("BTC-USD")

# Si falla API, usa datos de respaldo de hoy
if us02y is None:
    us02y, us10y, dxy, vix, brent, oro, btc = 4.74, 4.78, 103.5, 18.2, 104.5, 4378, 67500
    st.warning("Usando datos de respaldo - API Yahoo lenta, se actualizará solo")
else:
    # Convertir yields: ^IRX y ^TNX vienen x10
    us02y = us02y/1 if us02y < 10 else us02y/10  # Ajuste según formato
    us10y = us10y/1 if us10y < 10 else us10y/10
    st.success(f"✅ Datos en vivo: Oro ${oro} - Brent ${brent}")

# === MUESTRA MÓDULOS ===
st.header("1. DINERO REAL - LIVE")
col1, col2, col3, col4 = st.columns(4)
col1.metric("US02Y", f"{us02y}%", f"{c1}%")
col2.metric("US10Y", f"{us10y}%", f"{c2}%")
col3.metric("DXY", f"{dxy}", f"{c3}%")
col4.metric("VIX", f"{vix}", f"{c4}%")

st.header("2. MATERIAS + ORO")
c1, c2, c3 = st.columns(3)
c1.metric("ORO FUTURO", f"${oro}", f"{c6}%")
c2.metric("BRENT", f"${brent}", f"{c5}%")
c3.metric("BTC", f"${btc}", f"{c7}%")

# === MODULO ALERTAS TELEGRAM ===
st.divider()
st.header("3. 🔔 ALERTAS TELEGRAM")

st.write("Configura tu bot una sola vez:")
token = st.text_input("BOT TOKEN (de @BotFather)", type="password")
chat_id = st.text_input("CHAT ID (de @userinfobot)")

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": msg}, timeout=5)
        return True
    except:
        return False

# Lógica de alerta automática
alerta = ""
if isinstance(brent, (int,float)) and brent > 110:
    alerta = f"🚨 BRENT ROMPIÓ $110 - Actual ${brent} - Oro puede ir a $4500 por miedo"
if isinstance(us02y, (int,float)) and us02y > 4.80:
    alerta = f"🚨 US02Y > 4.80% - Actual {us02y}% - PELIGRO ventas oro"

if alerta and token and chat_id:
    if st.button("Enviar alerta ahora a Telegram"):
        if send_telegram(alerta):
            st.success("Alerta enviada!")
        else:
            st.error("Error token/chat_id")
    # Auto-envío
    if 'ultima_alerta' not in st.session_state or st.session_state.ultima_alerta != alerta:
        send_telegram(alerta + f"\nOro ${oro}")
        st.session_state.ultima_alerta = alerta
        st.toast(alerta)

if alerta:
    st.error(alerta)
else:
    st.info(f"Todo en rango - Oro ${oro} - Sin alertas críticas")

st.caption("v57 - Próximo: Módulo 3,4,5,6 con datos live también")
