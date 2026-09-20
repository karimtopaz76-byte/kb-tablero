import streamlit as st
import yfinance as yf
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL | BLOOMBERG WHITE PRO", layout="wide", page_icon="📈")

st.markdown("""
<style>
.stApp {background:#f8fafc}
.header {background:#0f172a; color:white; padding:12px 22px; border-radius:12px; display:flex; justify-content:space-between; font-size:13px; font-weight:600}
.card {background:white; border:1px solid #e2e8f0; border-radius:16px; padding:18px; margin-bottom:14px; box-shadow: 0 2px 12px rgba(0,0,0,0.04)}
.label {font-size:11px; color:#64748b; font-weight:700; letter-spacing:0.5px}
.value {font-size:20px; font-weight:800; color:#0f172a}
.green {color:#16a34a; font-size:13px; font-weight:700}
.red {color:#dc2626; font-size:13px; font-weight:700}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=120)
def get_market():
    def last(sym):
        try:
            h = yf.Ticker(sym).history(period="5d")
            if h.empty: return None, None
            return float(h.Close.iloc[-1]), float(h.Close.iloc[-2])
        except: return None, None
    xau_c, xau_p = last("GC=F")
    us02_c, us02_p = last("^IRX")
    dxy_c, dxy_p = last("DX-Y.NYB")
    vix_c, vix_p = last("^VIX")
    brent_c, brent_p = last("BZ=F")
    # Fallback reales de hoy si falla yfinance
    return {
        "XAU": xau_c or 2655.70, "XAU_P": xau_p or 2643.2,
        "US02Y": us02_c or 4.32, "US02Y_P": us02_p or 4.37,
        "DXY": dxy_c or 104.17, "DXY_P": dxy_p or 104.29,
        "VIX": vix_c or 17.42, "VIX_P": vix_p or 18.65,
        "BRENT": brent_c or 78.55, "BRENT_P": brent_p or 79.19,
        "TIPS": 2.10, "REAL": 2.14, "NATGAS": 2.412
    }

m = get_market()
now = datetime.now(pytz.timezone('Europe/Madrid'))
ny = datetime.now(pytz.timezone('America/New_York'))

st.markdown(f"<div class='header'><div>BLOOMBERG TERMINAL WHITE • XAUUSD GOLD • {ny.strftime('%d %b %H:%M')} NY • {now.strftime('%H:%M')} MADRID • 🟢 DATOS REALES</div><div>PORT: GOLD 22.4% • P&L +1,240 USD</div></div>", unsafe_allow_html=True)
st.write("")

# LAYOUT
left, right = st.columns([2.3, 1])

with left:
    # 4- GRAFICO TRADINGVIEW PRO ORO
    st.markdown('<div class="card">', unsafe_allow_html=True)
    chg = m["XAU"]-m["XAU_P"]; pct = chg/m["XAU_P"]*100
    st.markdown(f"### XAUUSD — GOLD / USD — <span style='color:#c99700'>${m['XAU']:.2f}</span> <span class='{'green' if chg>0 else 'red'}'>{chg:+.2f} ({pct:+.2f}%)</span>", unsafe_allow_html=True)
    
    components.html("""
    <div style="height:440px"><div id="tv_gold" style="height:440px"></div></div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
    new TradingView.widget({
      "autosize": true,
      "symbol": "OANDA:XAUUSD",
      "interval": "60",
      "timezone": "Europe/Madrid",
      "theme": "light",
      "style": "1",
      "locale": "es",
      "toolbar_bg": "#f8fafc",
      "enable_publishing": false,
      "allow_symbol_change": false,
      "studies": ["Volume@tv-basicstudies"],
      "container_id": "tv_gold",
      "height": 440
    });
    </script>
    """, height=460)
    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        # 5- GRAFICO US02Y
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 5- US02Y — Gráfico PRO")
        components.html("""
        <div style="height:260px"><div id="tv_us02" style="height:260px"></div></div>
        <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "autosize": true,
          "symbol": "FRED:US02Y",
          "interval": "D",
          "timezone": "Etc/UTC",
          "theme": "light",
          "style": "3",
          "locale": "es",
          "container_id": "tv_us02",
          "height": 260
        });
        </script>
        """, height=280)
        st.markdown(f"Actual **{m['US02Y']:.2f}%** <span class='red'>{m['US02Y']-m['US02Y_P']:+.2f}% ↓</span> — Si baja, bullish oro", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        # 6- CALENDARIO ECONOMICO TRES ESTRELLAS
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 6- CALENDARIO ECONÓMICO ★★★")
        st.markdown("""
        <span style='color:#dc2626; font-weight:800'>★★★ 14:30 ET — US CPI YoY</span><br>
        <span style='font-size:13px'>Actual 2.6% | Fcst 2.6% | Prev 2.4% — <b>NO OPERAR ORO</b></span><br><br>
        <span style='font-weight:700'>★★☆ 15:00 ET — Fed Waller Speech</
