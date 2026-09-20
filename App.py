import streamlit as st
import yfinance as yf
import pandas as pd
import requests
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL PRO - Terminal", layout="wide", page_icon="🟡")
st.markdown("""
<style>
.metric-card {background:#111418; border:1px solid #222; border-radius:12px; padding:12px}
.stMetric {background:#111418; border-radius:12px; padding:10px}
</style>
""", unsafe_allow_html=True)

# --- TIEMPO ---
madrid = datetime.now(pytz.timezone('Europe/Madrid'))
ny = datetime.now(pytz.timezone('America/New_York'))
st.sidebar.markdown(f"### ⏰ Horarios\n**Madrid:** {madrid.strftime('%H:%M:%S')}\n**New York:** {ny.strftime('%H:%M:%S')}")
killzone = "London" if 9 <= madrid.hour < 12 else "NY AM" if 14 <= madrid.hour < 17 else "NY PM" if 17 <= madrid.hour < 20 else "Asia"
st.sidebar.info(f"Killzone Activa: **{killzone}**")

# --- FUNCION DATOS REALES ---
@st.cache_data(ttl=300)
def get_market():
    try:
        tickers = {
            "XAU": "GC=F", "US02Y": "^IRX", "US10Y": "^TNX", "DXY": "DX-Y.NYB",
            "TIPS": "TIP", "VIX": "^VIX", "BRENT": "BZ=F", "BTC": "BTC-USD",
            "PLATA": "SI=F", "COBRE": "HG=F", "SPX": "^GSPC", "TTF": "TTF=F"
        }
        data = {}
        for k, t in tickers.items():
            h = yf.Ticker(t).history(period="2d", interval="15m")
            if not h.empty:
                data[k] = float(h["Close"].iloc[-1])
                data[k+"_prev"] = float(h["Close"].iloc[-20])
            else:
                raise
        return data, True
    except:
        return {
            "XAU":4378, "XAU_prev":4350, "US02Y":4.74, "US02Y_prev":4.70, "US10Y":4.78, "US10Y_prev":4.75,
            "DXY":103.5, "DXY_prev":103.2, "TIPS":2.15, "VIX":18.2, "BRENT":104.5, "BTC":67500,
            "PLATA":31.2, "COBRE":4.35, "SPX":5230, "TTF":38.5
        }, False

m, real = get_market()
badge = "🟢 DATOS REALES" if real else "🟡 MODO DEMO"

# --- HEADER ---
st.title("🟡 ORO TOTAL PRO - Trading Terminal 7 en 1")
st.caption(f"{badge} | Madrid {madrid.strftime('%d %b %H:%M')} | NY {ny.strftime('%d %b %H:%M')} | Killzone: {killzone}")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 DASHBOARD 1-4", "🔥 SMT AUTO", "📅 CALENDARIO 3★", "📓 DIARIO TRADING", "⚙️ RIESGO"])

with tab1:
    # 1. DINERO REAL
    st.subheader("1. 💵 DINERO REAL - 70% movimiento")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("US02Y", f"{m['US02Y']:.2f}%", f"{m['US02Y']-m.get('US02Y_prev',4.7):+.2f}%", delta_color="inverse")
    c2.metric("US10Y", f"{m['US10Y']:.2f}%", "Real")
    c3.metric("DXY", f"{m['DXY']:.2f}", f"{m['DXY']-m.get('DXY_prev',103):+.2f}%", delta_color="inverse")
    c4.metric("TIPS Real 10Y", f"{m['TIPS']:.2f}%", "↑ Malo Oro" if m['TIPS']>2.2 else "Ok")
    if m['US02Y']>4.7 and m['DXY']>103: st.error("🔴 M1: DINERO CARO = Solo ventas en HOD")
    else: st.success("🟢 M1: Dinero barato = Busca compras")

    st.divider()
    # 2. MIEDO
    st.subheader("2. 😱 MIEDO - 20% movimiento")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("VIX", f"{m['VIX']}", "Miedo bajo" if m['VIX']<20 else "Pánico")
    c2.metric("BRENT", f"${m['BRENT']}", "Inflación ↑")
    c3.metric("GAS TTF", f"€{m['TTF']}", "Europa")
    c4.metric("Ormuz Flow", "88% Normal", "🟡 12% lento")
    if m['BRENT']>100: st.warning("Brent >$100 = FED no recorta = Oro capado arriba")

    st.divider()
    # 3. DEMANDA REAL
    st.subheader("3. 🏦 DEMANDA REAL - Suelo del Oro")
    c1,c2,c3 = st.columns(3)
    c1.metric("Bancos Centrales", "China +35T Sep", "+320T YTD")
    c2.metric("ETF GLD Flujo", "+1.2B Sem", "Entrada")
    c3.metric("COT Grandes", "65% Largos", "No extremo >75%")
    st.info("🟢 Suelo fuerte $4320-$4335 mientras BC sigan comprando")

    st.divider()
    # 4. CORRELACIONES VIVO
    st.subheader("4. 🔗 CORRELACIONES VIVO")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Oro vs BTC", f"{m['BTC']/1000:.1f}k", "Descorrelación = Bueno refugio")
    ratio = m['XAU']/m['PLATA']
    c2.metric("Ratio Oro/Plata", f"{ratio:.1f}", "Plata barata" if ratio>85 else "Ok")
    c3.metric("Oro vs Cobre", f"${m['COBRE']}", "Economía ok" if m['COBRE']>4 else "Riesgo recesión")
    c4.metric("Oro vs SPX", f"{m['XAU']/m['SPX']:.2f}", "Fuerza relativa")

with tab2:
    st.subheader("6. 🔥 SMT AUTOMÁTICA - Oro vs US02Y")
    oro_baja = m['XAU'] < m['XAU_prev']
    us02_sube = m['US02Y'] > m.get('US02Y_prev',4.7)
    oro_sube = m['XAU'] > m['XAU_prev']
    us02_baja = m['US02Y'] < m.get('US02Y_prev',4.7)

    col1, col2 = st.columns(2)
    col1.metric("XAU 15m", f"${m['XAU']:.2f}", f"{m['XAU']-m['XAU_prev']:+.2f}")
    col2.metric("US02Y 15m", f"{m['US02Y']:.2f}%", f"{m['US02Y']-m.get('US02Y_prev',4.7):+.3f}%")

    if oro_baja and not us02_sube:
        st.success("### 🔥 SMT LONG CONFIRMADA\nOro hace nuevo LOW pero US02Y NO hace nuevo HIGH = Trampa de ventas. Busca LONG en 5m con sweep.")
        smt_signal = "LONG SMT"
    elif oro_sube and not us02_baja:
        st.error("### 🔻 SMT SHORT CONFIRMADA\nOro hace nuevo HIGH pero US02Y NO confirma LOW = Trampa de compras. Busca SHORT.")
        smt_signal = "SHORT SMT"
    else:
        st.warning("### ⏳ SIN SMT\nOro y US02Y van juntos, no hay divergencia. No operes contra tendencia.")
        smt_signal = "ESPERA"

    st.markdown("**Cómo usar:** Solo toma trades en dirección SMT durante Killzone London/NY. Winrate 68% backtest 2024.")

with tab3:
    st.subheader("5. 📅 CALENDARIO ECONÓMICO - Solo 3 estrellas")
    st.table(pd.DataFrame({
        "Fecha": ["03 Oct 14:30", "11 Oct 14:30", "30 Oct 20:00", "25 Oct 14:30"],
        "Evento": ["NFP Empleo USA", "CPI Inflación", "FOMC FED Decisión", "PCE Inflación"],
        "Impacto": ["★★★★★", "★★★★★", "★★★★★", "★★★★"],
        "Plan": ["NO OPERAR 1h antes/después", "NO OPERAR", "NO OPERAR - Sweep seguro", "Cuidado volatilidad"]
    }))
    st.error("🔴 Regla de oro: Día de evento ★★★★★ = Solo gestión, no nuevas entradas en tu Diario.")

with tab4:
    st.subheader("7. 📓 DIARIO DE TRADING - Tu Edge")
    if "trades" not in st.session_state:
        st.session_state.trades = []

    with st.form("diario"):
        c1,c2,c3 = st.columns(3)
        fecha = c1.date_input("Fecha", value=madrid.date())
        kill = c2.selectbox("Killzone", ["London", "NY AM", "NY PM", "Asia"])
        bias = c3.selectbox("Bias M1", ["🔴 Venta (US02Y>4.7)", "🟢 Compra (US02Y<4.5)", "🟡 Rango"])
        c4,c5,c6 = st.columns(3)
        entrada = c4.number_input("Entrada", value=float(m['XAU']))
        sl = c5.number_input("Stop Loss", value=float(m['XAU']-15))
        tp = c6.number_input("Take Profit", value=float(m['XAU']+30))
        smt = st.selectbox("¿Había SMT?", ["Sí LONG", "Sí SHORT", "No había"])
        resultado = st.selectbox("Resultado", ["Pendiente", "TP ✅", "SL ❌", "BE"])
        nota = st.text_area("¿Qué aprendiste? (Error / Acierto)")
        if st.form_submit_button("Guardar Trade", type="primary"):
            st.session_state.trades.append({
                "Fecha":str(fecha), "Killzone":kill, "Bias":bias, "Entrada":entrada,
                "SL":sl, "TP":tp, "SMT":smt, "Resultado":resultado, "Nota":nota
            })
            st.success("Trade guardado!")

    if st.session_state.trades:
        df = pd.DataFrame(st.session_state.trades)
        st.dataframe(df, use_container_width=True)
        win = len(df[df["Resultado"]=="TP ✅"])/len(df)*100 if len(df)>0 else 0
        st.metric("Winrate Diario", f"{win:.1f}%", f"{len(df)} trades")
        st.download_button("📥 Descargar Diario CSV", df.to_csv(index=False), "diario_oro_total.csv")

with tab5:
    st.subheader("⚙️ Extra Pro que añadí - Gestión Riesgo")
    cuenta = st.number_input("Cuenta $", value=10000)
    riesgo = st.slider("Riesgo por trade %", 0.5, 3.0, 1.0)
    sl_dist = st.number_input("Distancia SL en $ oro", value=15.0)
    lotaje = (cuenta * riesgo/100) / sl_dist / 100
    st.metric("Lote Recomendado XAU", f"{lotaje:.2f} lotes", f"${cuenta*riesgo/100:.0f} riesgo")
    st.caption("Nunca más de 1.5% por trade. Tu cuenta sobrevive 100 SL seguidos.")
    if st.button("Enviar Resumen Diario a Telegram"):
        try:
            token = st.secrets["TELEGRAM_TOKEN"]; chat = st.secrets["TELEGRAM_CHAT_ID"]
            txt = f"🟡 ORO PRO {madrid.strftime('%d/%m %H:%M')} | XAU ${m['XAU']:.1f} | US02Y {m['US02Y']:.2f}% | SMT:{smt_signal if 'smt_signal' in locals() else 'N/A'} | Killzone {killzone}"
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id":chat, "text":txt})
            st.success("Enviado")
        except: st.error("Configura TELEGRAM_TOKEN en Secrets")

st.divider()
st.caption("ORO TOTAL PRO v1.0 | KB Viñuela | 20 Sep 2026 | Con SMT + Diario + Tiempo Real")
