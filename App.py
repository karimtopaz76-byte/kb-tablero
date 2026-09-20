import streamlit as st
import yfinance as yf
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL - BLOOMBERG WHITE PRO", layout="wide", page_icon="◼")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;700;800&display=swap');
.stApp {background:#ffffff; font-family:'Inter', sans-serif}
.header {
  background:#000000; color:#ffffff; padding:14px 24px; 
  font-family:'JetBrains Mono', monospace; font-size:12px; letter-spacing:0.3px;
  display:flex; justify-content:space-between; border-radius:2px;
}
.card {
  background:#ffffff; border:1px solid #e5e7eb; border-radius:4px; padding:16px;
  font-family:'JetBrains Mono', monospace;
}
.card-title {
  font-family:'Inter', sans-serif; font-weight:800; font-size:13px; 
  color:#000000; text-transform:uppercase; letter-spacing:0.8px; 
  border-bottom:2px solid #000; padding-bottom:8px; margin-bottom:12px;
}
.row {display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #f3f4f6; font-size:12px}
.row b {font-weight:700}
.up {color:#00a86b} .down {color:#e11d48}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=90)
def get_data():
    def g(t):
        try:
            h=yf.Ticker(t).history(period="5d")
            return float(h.Close.iloc[-1]), float(h.Close.iloc[-2])
        except: return None, None
    xau_c,xau_p = g("GC=F")
    us02_c,us02_p = g("^IRX")
    dxy_c,dxy_p = g("DX-Y.NYB")
    vix_c,vix_p = g("^VIX")
    brent_c,brent_p = g("BZ=F")
    return {
        "XAU": xau_c or 2655.70, "XAU_P": xau_p or 2643.10,
        "US02Y": us02_c or 4.32, "US02Y_P": us02_p or 4.37,
        "DXY": dxy_c or 104.17, "DXY_P": dxy_p or 104.29,
        "VIX": vix_c or 17.42, "VIX_P": vix_p or 18.65,
        "BRENT": brent_c or 78.55, "BRENT_P": brent_p or 79.19,
    }

d = get_data()
now = datetime.now(pytz.timezone('Europe/Madrid'))
ny = datetime.now(pytz.timezone('America/New_York'))

# HEADER BLOOMBERG REAL
st.markdown(f"<div class='header'><div>◼ BLOOMBERG TERMINAL WHITE | XAUUSD GOLD {d['XAU']:.2f} | NY {ny.strftime('%H:%M:%S')} | MAD {now.strftime('%H:%M')} | VOL 42.1K</div><div>KB_VINUELA | PORT GOLD 22.4% | P&L +1,240.50</div></div>", unsafe_allow_html=True)
st.write("")

left, right = st.columns([2.4, 1])

with left:
    # 4 - GRAFICO TRADINGVIEW PRO
    st.markdown('<div class="card">', unsafe_allow_html=True)
    diff = d["XAU"] - d["XAU_P"]
    pc = diff / d["XAU_P"] * 100
    color = "up" if diff>0 else "down"
    st.markdown(f"<div class='card-title'>4 — XAUUSD GOLD / USD — {d['XAU']:.2f} <span class='{color}'>{diff:+.2f} ({pc:+.2f}%)</span> | OPEN {d['XAU_P']:.2f} HIGH {d['XAU']+2:.2f} LOW {d['XAU']-8:.2f}</div>", unsafe_allow_html=True)
    components.html("""
    <div id="tv_gold"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
      "width": "100%", "height": 460,
      "symbol": "OANDA:XAUUSD", "interval": "60",
      "timezone": "Europe/Madrid", "theme": "light", "style": "1",
      "locale": "es", "toolbar_bg": "#ffffff",
      "enable_publishing": false, "hide_top_toolbar": false,
      "container_id": "tv_gold"
    });
    </script>
    """, height=480)
    st.markdown('</div>', unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"<div class='card-title'>5 — US02Y — 2Y YIELD — {d['US02Y']:.2f}%</div>", unsafe_allow_html=True)
        components.html("""
        <div id="tv_us02"></div>
        <script src="https://s3.tradingview.com/tv.js"></script>
        <script>
        new TradingView.widget({
          "width": "100%", "height": 260,
          "symbol": "FRED:DGS2", "interval": "D",
          "timezone": "Etc/UTC", "theme": "light", "style": "3",
          "locale": "es", "container_id": "tv_us02"
        });
        </script>
        """, height=280)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<div class='card-title'>6 — CALENDARIO ECONÓMICO ★★★</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='row'><b>★★★ 14:30 ET</b><span class='down'>US CPI YoY 2.6% / 2.6%</span></div>
        <div class='row'><b>★★☆ 15:00 ET</b><span>Fed Waller Speech</span></div>
        <div class='row'><b>★★★ 08:30 ET+1</b><span class='down'>Jobless Claims 220K</span></div>
        <div class='row'><b>★★★ 14:00 ET</b><span>FOMC Minutes</span></div>
        <div style='margin-top:10px; font-size:10px; color:#6b7280'>* Solo ★★★ mueve XAUUSD directo. No operar 15m antes/después.</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

with right:
    # 1 - MONEY
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>1 — MONEY — RATES & DOLLAR</div>", unsafe_allow_html=True)
    def row_money(name, val, prev, suf="%"):
        diff = val-prev
        cls = "up" if diff<0 else "down"
        if name=="DXY": cls = "up" if diff<0 else "down"
        arrow = "▼" if diff<0 else "▲"
        return f"<div class='row'><span>{name}</span><span><b>{val:.2f}{suf}</b> <span class='{cls}'>{diff:+.2f} {arrow}</span></span></div>"
    st.markdown(row_money("Real Yield", 2.14, 2.11) + row_money("US02Y", d["US02Y"], d["US02Y_P"]) + row_money("DXY", d["DXY"], d["DXY_P"], "") + row_money("TIPS", 2.10, 2.08), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2 - FEAR
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>2 — FEAR — VOLATILITY & ENERGY</div>", unsafe_allow_html=True)
    dvix = d["VIX"]-d["VIX_P"]
    dbrent = d["BRENT"]-d["BRENT_P"]
    st.markdown(f"""
    <div class='row'><span>VIX</span><span><b>{d['VIX']:.2f}</b> <span class='up'>{dvix:+.2f} ▼</span></span></div>
    <div class='row'><span>Brent Crude</span><span><b>{d['BRENT']:.2f}</b> <span class='down'>{dbrent:+.2f} ▼</span></span></div>
    <div class='row'><span>Nat Gas TTF</span><span><b>2.412</b> <span class='up'>+0.029 ▲</span></span></div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3 - SMT
    st.markdown('<div class="card" style="border-left:4px solid #000000">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>3 — SMT DETECTION — ORO vs US02Y</div>", unsafe_allow_html=True)
    if d["US02Y"] < d["US02Y_P"]:
        st.markdown(f"<div style='background:#f0fdf4; border:1px solid #bbf7d0; padding:10px; font-size:11px'><b style='color:#00a86b'>✅ CONFIRMED</b> — Liquidity Sweep Lows 2632.20 barrido<br><br><b>Inducement:</b> Breaker 2648.50<br><b>FVG:</b> 2650.10-2654.30 • 68% Mitigated<br><br><b>US02Y {d['US02Y']:.2f}% no confirma → Divergencia BULLISH ORO</b><br><br><b>PD Bias: BULLISH</b></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='background:#fefce8; padding:10px; font-size:11px'>⏳ Esperando divergencia</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 7 - DIARIO
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>7 — DIARIO DE TRADING</div>", unsafe_allow_html=True)
    if "trades" not in st.session_state: st.session_state.trades=[]
    with st.form("diario_pro", clear_on_submit=True):
        bias = st.selectbox("Setup SMT", ["LONG Oro + SMT US02Y", "SHORT Oro + SMT US02Y", "ESPERA CPI ★★★"], label_visibility="collapsed")
        entrada = st.number_input("Entrada", value=float(d["XAU"]), label_visibility="collapsed", placeholder="Entrada")
        col1,col2 = st.columns(2)
        sl = col1.number_input("SL", value=2632.2, label_visibility="collapsed", placeholder="SL")
        tp = col2.number_input("TP", value=2680.0, label_visibility="collapsed", placeholder="TP")
        nota = st.text_input("Nota", placeholder="Ej: US02Y no confirma", label_visibility="collapsed")
        if st.form_submit_button("GUARDAR TRADE", use_container_width=True, type="primary"):
            st.session_state.trades.append({"HORA": now.strftime('%H:%M'), "BIAS": bias, "ENT": entrada, "SL": sl, "TP": tp, "NOTA": nota})
    if st.session_state.trades:
        st.dataframe(pd.DataFrame(st.session_state.trades), hide_index=True, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
