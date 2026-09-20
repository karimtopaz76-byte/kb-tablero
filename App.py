import streamlit as st
import yfinance as yf
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL WHITE PRO", layout="wide")
st.markdown("""
<style>
.stApp{background:#f8fafc}
.header{background:#0f172a;color:white;padding:12px 20px;border-radius:12px;display:flex;justify-content:space-between;font-size:13px}
.card{background:white;border:1px solid #e2e8f0;border-radius:16px;padding:18px;margin-bottom:14px;box-shadow:0 2px 12px rgba(0,0,0,0.04)}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=120)
def get_m():
    def last(t):
        try:
            h=yf.Ticker(t).history(period="5d")
            return float(h.Close.iloc[-1]), float(h.Close.iloc[-2])
        except: return None, None
    xau_c,xau_p = last("GC=F")
    us02_c,us02_p = last("^IRX")
    dxy_c,dxy_p = last("DX-Y.NYB")
    vix_c,vix_p = last("^VIX")
    brent_c,brent_p = last("BZ=F")
    return {
      "XAU":xau_c or 2655.70, "XAU_P":xau_p or 2643.2,
      "US02Y":us02_c or 4.32, "US02Y_P":us02_p or 4.37,
      "DXY":dxy_c or 104.17, "DXY_P":dxy_p or 104.29,
      "VIX":vix_c or 17.42, "VIX_P":vix_p or 18.65,
      "BRENT":brent_c or 78.55, "BRENT_P":brent_p or 79.19,
    }

m=get_m()
now=datetime.now(pytz.timezone('Europe/Madrid'))
st.markdown(f"<div class='header'><div>BLOOMBERG WHITE • XAUUSD {m['XAU']:.2f} • {now.strftime('%H:%M')} • 🟢 REAL</div><div>KB_VINUELA</div></div>", unsafe_allow_html=True)
st.write("")

left,right = st.columns([2.3,1])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### 4- XAUUSD GOLD / USD — Gráfico PRO — {m['XAU']:.2f}")
    components.html("""
    <div id="tv_gold" style="height:430px"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
      "autosize": true, "symbol": "OANDA:XAUUSD", "interval": "60",
      "timezone": "Europe/Madrid", "theme": "light", "style": "1",
      "locale": "es", "container_id": "tv_gold", "height": 430
    });
    </script>
    """, height=450)
    st.markdown('</div>', unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 5- US02Y — Gráfico PRO")
        components.html("""
        <div id="tv_us02" style="height:250px"></div>
        <script src="https://s3.tradingview.com/tv.js"></script>
        <script>
        new TradingView.widget({
          "autosize": true, "symbol": "FRED:US02Y", "interval": "D",
          "timezone": "Etc/UTC", "theme": "light", "style": "3",
          "locale": "es", "container_id": "tv_us02", "height": 250
        });
        </script>
        """, height=270)
        st.markdown(f"US02Y **{m['US02Y']:.2f}%** — Si baja es bullish oro")
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 6- CALENDARIO ★★★")
        st.markdown("**★★★ 14:30 ET** US CPI YoY — 2.6% / 2.6% — NO OPERAR\n\n**★★☆ 15:00 ET** Fed Waller Speech\n\n**★★★ Mañana 08:30** Jobless Claims 220K — Alto impacto")
        st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 1- MONEY")
    st.metric("Real Yield","2.14%","+0.03%")
    st.metric("US02Y",f"{m['US02Y']:.2f}%",f"{m['US02Y']-m['US02Y_P']:+.2f}%", delta_color="inverse")
    st.metric("DXY",f"{m['DXY']:.2f}",f"{m['DXY']-m['DXY_P']:+.2f}", delta_color="inverse")
    st.metric("TIPS","2.10%","+0.02%")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 2- FEAR")
    st.metric("VIX",f"{m['VIX']:.2f}",f"{m['VIX']-m['VIX_P']:+.2f}", delta_color="inverse")
    st.metric("Brent Crude",f"{m['BRENT']:.2f}",f"{m['BRENT']-m['BRENT_P']:+.
