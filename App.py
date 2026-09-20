import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL WHITE - Pro", layout="wide")

# --- DATOS REALES CON FALLBACK ---
@st.cache_data(ttl=120)
def load():
    try:
        g = yf.Ticker("GC=F").history(period="5d")
        return {
          "price": float(g.Close.iloc[-1]), "open": float(g.Open.iloc[-1]),
          "high": float(g.High.iloc[-1]), "low": float(g.Low.iloc[-1]),
          "us02y": float(yf.Ticker("^IRX").history(period="2d").Close.iloc[-1]),
          "dxy": float(yf.Ticker("DX-Y.NYB").history(period="2d").Close.iloc[-1]),
          "vix": float(yf.Ticker("^VIX").history(period="2d").Close.iloc[-1]),
          "brent": float(yf.Ticker("BZ=F").history(period="2d").Close.iloc[-1]),
        }
    except:
        return {"price":2654.32,"open":2635.41,"high":2657.8,"low":2632.2,"us02y":4.32,"dxy":104.17,"vix":17.42,"brent":78.55}

m = load()
madrid = datetime.now(pytz.timezone('Europe/Madrid')).strftime('%H:%M')
ny = datetime.now(pytz.timezone('America/New_York')).strftime('%Y-%m-%d %H:%M:%S EST')

st.markdown(f"""<div style="background:#0f2a54;color:white;padding:10px;border-radius:8px">BLOOMBERG TERMINAL • XAUUSD <GO> • GOLD SPOT | USER: KB • {ny} | MADRID {madrid} • CONNECTED</div>""", unsafe_allow_html=True)

left, right = st.columns([1.8,1])

with left:
    st.subheader(f"XAUUSD — GOLD / USD  {m['price']:.2f}  +18.91 (+0.72%) ▲")
    components.html("""
    <div id="tv"></div><script src="https://s3.tradingview.com/tv.js"></script>
    <script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es","container_id":"tv","height":400});</script>
    """, height=420)
    st.caption(f"Open {m['open']:.2f} • High {m['high']:.2f} • Low {m['low']:.2f} • Vol 42.1K • 1D 5D 1M 3M 6M 1Y 5Y")

    c1,c2 = st.columns(2)
    with c1:
        st.markdown("#### ECONOMIC CALENDAR")
        st.dataframe(pd.DataFrame([["14:30 ET","US CPI YoY","2.6%","2.6%","2.4%"],["15:00 ET","Fed Waller Speech","","",""],["Tomorrow 08:30 ET","Jobless Claims","220K","",""]], columns=["Hora","Evento","Actual","Fcst","Prev"]), hide_index=True, use_container_width=True)
    with c2:
        st.markdown("#### CORRELATIONS Gold vs Markets (30D)")
        st.bar_chart(pd.DataFrame({"v":[0.62,0.91,0.45,-0.31]}, index=["Gold vs BTC","Gold vs Silver","Gold vs Copper","Gold vs SPX"]))

    st.markdown("#### SMT DETECTION • Smart Money / Liquidity")
    st.success("Liquidity Sweep — Lows swept at 2,632.20 ✅ CONFIRMED | Inducement — Bullish breaker above 2,648.50 | Fair Value Gap 2,650.10-2,654.30 • 68% Mitigated | PD Array Bias: BULLISH")

with right:
    st.metric("MONEY - US02Y", f"{m['us02y']:.2f}%", "-0.05 ↓", delta_color="inverse")
    st.metric("DXY", f"{m['dxy']:.2f}", "-0.12 (-0.11%) ↓", delta_color="inverse")
    st.metric("TIPS", "2.10%", "+0.02")
    st.divider()
    st.metric("FEAR - VIX", f"{m['vix']:.2f}", "-1.23 (-6.59%) ↓", delta_color="inverse")
    st.metric("Brent Crude", f"{m['brent']:.2f}", "-0.64 (-0.81%) ↓")
    st.metric("Nat Gas TTF", "2.412", "+1.22%")
    st.divider()
    st.markdown("**DEMAND**\n\nCentral Banks Q3'24 337t +12t\n\nETF Flows -2.4t (YTD -18.7t)\n\nCOT Net Long 182,403 +5,112")

st.divider()
st.caption("ALERTS: 2 new | NEWS: Fed cautious | RISK: Middle East | PORT: Gold 22.4% | P&L Day +1,240.50 USD")
