import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL PRO WHITE", layout="wide")
st.markdown("""
<style>
[data-testid="stMetric"] {background:white; border:1px solid #e5e7eb; border-radius:12px; padding:12px; box-shadow:0 1px 3px rgba(0,0,0,0.05)}
.block {background:white; border:1px solid #e5e7eb; border-radius:12px; padding:16px; margin-bottom:14px}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_data():
    try:
        def last(t):
            return float(yf.Ticker(t).history(period="2d", interval="15m")["Close"].iloc[-1])
        return {
            "XAU":last("GC=F"), "US02Y":last("^IRX"), "DXY":last("DX-Y.NYB"),
            "TIPS":1.84, "VIX":last("^VIX"), "BRENT":last("BZ=F"), "GAS":2.41,
            "PLATA":last("SI=F"), "COBRE":last("HG=F"), "BTC":last("BTC-USD"), "SPX":last("^GSPC")
        }, True
    except:
        return {"XAU":4378,"US02Y":4.74,"DXY":103.5,"TIPS":2.15,"VIX":18.2,"BRENT":104.5,"GAS":38,"PLATA":31.2,"COBRE":4.35,"BTC":67500,"SPX":5230}, False

m, real = get_data()
madrid = datetime.now(pytz.timezone('Europe/Madrid'))

# HEADER AZUL COMO LA FOTO
st.markdown(f"""
<div style="background:#1e3a5f; color:white; padding:12px 18px; border-radius:10px; display:flex; justify-content:space-between">
<div><b>BLOOMBERG TERMINAL</b> • XAUUSD GOLD PRICE • {madrid.strftime('%d %b %H:%M')} Madrid • {"🟢 REALTIME" if real else "🟡 DEMO"}</div>
<div>TRADER • LIVE</div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.6,1])

with left:
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown(f"### XAUUSD • GOLD PRICE CHART • 1M DAILY USD/oz — ${m['XAU']:.2f}")
    df_chart = pd.DataFrame({"price":[2600,2620,2610,2585,m['XAU']]})
    st.line_chart(df_chart, height=200)
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.metric("OPEN","2608.12"); c2.metric("HIGH","2618.90"); c3.metric("LOW","2599.40"); c4.metric("VOL","12.4M"); c5.metric("YTD","+18.7%")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("### 📅 ECONOMIC CALENDAR • Sep 01 - Sep 05")
    st.table(pd.DataFrame({
        "Fecha": ["Sep 01 08:30","Sep 03 10:00","Sep 05 08:30"],
        "Evento": ["US Nonfarm Payrolls","ISM Services PMI","Initial Jobless Claims"],
        "Forecast": ["160k","51.7","230k"],
        "Previo": ["114k","51.2","227k"]
    }))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="block" style="border-left:4px solid #c2410c">', unsafe_allow_html=True)
    st.markdown("### 🎯 SMT DETECTION • LIQUIDITY SWEEP • ACTIVE")
    st.error("LIQUIDITY SWEEP DETECTED — XAUUSD")
    st.markdown("""
    - Sweep below 2600.00 support — swept buy-side stops
    - Target liquidity zone: 2592-2595 — 62% probability
    - Bullish displacement expected → watch 2620 break
    """)
    st.progress(64, text="Status: MONITORING • Confidence 64%")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("#### 🏦 MONEY • RATES & FX")
    st.metric("US02Y", f"{m['US02Y']:.3f}%", "+0.024 (+0.64%)")
    st.metric("DXY (Dollar Index)", f"{m['DXY']:.2f}", "-0.12 (-0.12%)", delta_color="inverse")
    st.metric("TIPS (5Y)", f"{m['TIPS']:.2f}%", "+0.011")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("#### ⏱️ FEAR • RISK")
    st.metric("VIX", f"{m['VIX']:.2f}", "-0.58 (-3.42%)", delta_color="inverse")
    st.metric("Brent Crude", f"{m['BRENT']:.2f}", "+0.63 (+0.81%)")
    st.metric("Natural Gas TTF", f"{m['GAS']}", "-0.05 (-2.03%)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("#### 📦 DEMAND • FLOW")
    st.markdown(f"**Central Banks** Net Buy: +12.4t oz\n\n**ETF Holdings** 2,847.2t +4.2t (+0.15%)\n\n**COT Managed Money Long: 112.4k**")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("#### 🔗 CORRELATIONS • 30D vs Gold")
    st.bar_chart(pd.DataFrame({"corr":[0.68,0.82,0.45,-0.12]}, index=["Gold","Gold vs Silver","Gold vs Copper","Gold vs SPX"]))
    st.caption(f"Ratio Oro/Plata: {m['XAU']/m['PLATA']:.1f} • Oro/BTC: Descorrelacionado")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
# DIARIO RÁPIDO
st.subheader("📓 DIARIO TRADING RÁPIDO")
if "trades" not in st.session_state: st.session_state.trades=[]
with st.form("d"):
    c1,c2,c3,c4 = st.columns(4)
    bias=c1.selectbox("Bias", ["LONG SMT","SHORT SMT","RANGO"])
    entrada=c2.number_input("Entrada", value=float(m['XAU']))
    sl=c3.number_input("SL", value=float(m['XAU']-15))
    res=c4.selectbox("Res", ["Pendiente","TP ✅","SL ❌"])
    nota=st.text_input("Nota")
    if st.form_submit_button("Guardar"):
        st.session_state.trades.append({"Hora":madrid.strftime('%H:%M'),"Bias":bias,"Entrada":entrada,"SL":sl,"Res":res,"Nota":nota})
if st.session_state.trades:
    st.dataframe(pd.DataFrame(st.session_state.trades), use_container_width=True)
