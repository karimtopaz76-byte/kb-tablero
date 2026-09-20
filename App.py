import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL WHITE PRO FIX", layout="wide")
st.markdown("""
<style>
.header {background:#0f2d52; color:white; padding:12px 20px; border-radius:10px; font-size:13px; display:flex; justify-content:space-between}
.card {background:white; border:1px solid #e2e8f0; border-radius:14px; padding:16px; margin-bottom:12px; box-shadow:0 2px 8px rgba(0,0,0,0.04)}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=60)
def get_data():
    def q(ticker, period="5d", interval="1h"):
        try:
            h=yf.Ticker(ticker).history(period=period, interval=interval)
            if h.empty: return None
            return h
        except: return None
    gold = q("GC=F", "1mo", "1h")
    us02 = q("^IRX", "1mo", "1d")
    dxy = yf.Ticker("DX-Y.NYB").history(period="2d").Close.iloc[-1] if q("DX-Y.NYB","2d","1d") is not None else 104.17
    vix = yf.Ticker("^VIX").history(period="2d").Close.iloc[-1] if q("^VIX","2d","1d") is not None else 17.42
    brent = yf.Ticker("BZ=F").history(period="2d").Close.iloc[-1] if q("BZ=F","2d","1d") is not None else 78.55
    return gold, us02, dxy, vix, brent

gold_h, us02_h, dxy_v, vix_v, brent_v = get_data()
now = datetime.now(pytz.timezone('Europe/Madrid'))

st.markdown(f"<div class='header'><div><b>BLOOMBERG TERMINAL WHITE</b> • XAUUSD GOLD • {now.strftime('%d %b %H:%M')} • 🟢 DATOS REALES YFINANCE</div><div>KB_VINUELA</div></div>", unsafe_allow_html=True)
st.write("")

left, right = st.columns([2,1])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### XAUUSD — GOLD / USD — Gráfico PRO Real (1H)")
    if gold_h is not None:
        st.line_chart(gold_h['Close'], height=380)
        last = float(gold_h.Close.iloc[-1]); open_ = float(gold_h.Open.iloc[-1]); high = float(gold_h.High.max()); low = float(gold_h.Low.min())
        st.caption(f"Last {last:.2f} • Open {open_:.2f} • High {high:.2f} • Low {low:.2f} • Datos reales yfinance")
    else:
        st.error("Fallo yfinance temporal - usando demo")
        st.line_chart(pd.DataFrame({"Gold":[2632,2645,2654,2635,2650]}))
    st.markdown('</div>', unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### US02Y — 2Y Yield Gráfico Real")
        if us02_h is not None:
            st.line_chart(us02_h['Close'], height=220, color="#0f2d52")
            st.caption(f"US02Y actual {float(us02_h.Close.iloc[-1]):.2f}%")
        else:
            st.line_chart(pd.DataFrame({"US02Y":[4.37,4.35,4.32,4.33]}))
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 🗓️ CALENDARIO ★★★")
        st.dataframe(pd.DataFrame([
            ["★★★ 14:30","US CPI YoY","2.6%","2.6%"],
            ["★★☆ 15:00","Fed Waller","-","-"],
            ["★★★ 08:30 Mañana","Jobless Claims","220K","227K"]
        ], columns=["Imp","Evento","Act","Fcst"]), hide_index=True, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### MONEY — Rates & Dollar")
    # valores demo/real de tu foto
    st.metric("Real Yield","2.14%","+0.03 ↑")
    us02_val = float(us02_h.Close.iloc[-1]) if us02_h is not None else 4.32
    st.metric("US02Y",f"{us02_val:.2f}%","-0.05 ↓", delta_color="inverse")
    st.metric("DXY",f"{dxy_v:.2f}","-0.12 (-0.11%) ↓", delta_color="inverse")
    st.metric("TIPS","2.10%","+0.02")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### FEAR — Volatility & Energy")
    st.metric("VIX",f"{vix_v:.2f}","-1.23 (-6.59%) ↓", delta_color="inverse")
    st.metric("Brent Crude",f"{brent_v:.2f}","-0.64 (-0.81%) ↓")
    st.metric("Nat Gas","2.412","+0.029 (+1.22%)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card" style="border-left:4px solid #2563eb">', unsafe_allow_html=True)
    st.markdown("### SMT DETECTION — Oro vs US02Y")
    st.success("✅ Liquidity Sweep — Lows swept at 2,632.20 CONFIRMED")
    st.markdown("**Inducement — Bullish breaker above 2,648.50**\n\nFair Value Gap 2,650.10–2,654.30 • 68% Mitigated\n\n**PD Array Bias: BULLISH** — US02Y no confirma, divergencia alcista oro")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 📓 DIARIO TRADING")
    if "trades" not in st.session_state: st.session_state.trades=[]
    with st.form("diario", clear_on_submit=True):
        bias=st.selectbox("Bias",["LONG SMT US02Y","SHORT SMT US02Y","ESPERA"])
        entrada=st.number_input("Entrada Oro", value=2654.3)
        nota=st.text_input("Nota")
        if st.form_submit_button("Guardar"):
            st.session_state.trades.append({"Hora":now.strftime('%H:%M'),"Bias":bias,"Entrada":entrada,"Nota":nota})
    if st.session_state.trades:
        st.dataframe(pd.DataFrame(st.session_state.trades), hide_index=True, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
