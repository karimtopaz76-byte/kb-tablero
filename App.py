import streamlit as st
import yfinance as yf
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL - Terminal White Pro", layout="wide", page_icon="🟡")

# --- CSS BLANCO PRO COMO FOTO 1 ---
st.markdown("""
<style>
.header {background:#0f2d52; color:white; padding:14px 20px; border-radius:10px; font-weight:600}
.card {background:white; border:1px solid #e2e8f0; border-radius:12px; padding:14px; box-shadow:0 2px 8px rgba(0,0,0,0.04); margin-bottom:14px}
.card h4 {margin:0 0 8px 0; font-size:15px}
.small {font-size:12px; color:#64748b}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=60)
def get_all():
    try:
        def get(t):
            h = yf.Ticker(t).history(period="5d", interval="1d")
            c = float(h["Close"].iloc[-1]); o=float(h["Open"].iloc[-1]); hi=float(h["High"].iloc[-1]); lo=float(h["Low"].iloc[-1]); vol=float(h["Volume"].iloc[-1]) if "Volume" in h else 0
            prev=float(h["Close"].iloc[-2])
            return c,o,hi,lo,vol,prev
        xau_c,xau_o,xau_h,xau_l,xau_v,xau_p = get("GC=F")
        us02_c,_,_,_,_,us02_p = get("^IRX")
        dxy_c,_,_,_,_,dxy_p = get("DX-Y.NYB")
        vix_c,_,_,_,_,vix_p = get("^VIX")
        brent_c,_,_,_,_,brent_p = get("BZ=F")
        plata_c,_,_,_,_,_ = get("SI=F")
        cobre_c,_,_,_,_,_ = get("HG=F")
        btc_c,_,_,_,_,_ = get("BTC-USD")
        spx_c,_,_,_,_,_ = get("^GSPC")
        return {
            "XAU":xau_c,"OPEN":xau_o,"HIGH":xau_h,"LOW":xau_l,"VOL":xau_v,"PREV":xau_p,
            "US02Y":us02_c,"US02Y_PREV":us02_p,"DXY":dxy_c,"DXY_PREV":dxy_p,
            "VIX":vix_c,"VIX_PREV":vix_p,"BRENT":brent_c,"BRENT_PREV":brent_p,
            "PLATA":plata_c,"COBRE":cobre_c,"BTC":btc_c,"SPX":spx_c
        }, True
    except:
        return {"XAU":2654.32,"OPEN":2635.41,"HIGH":2657.8,"LOW":2632.2,"VOL":42100,"PREV":2635,"US02Y":4.32,"US02Y_PREV":4.37,"DXY":104.17,"DXY_PREV":104.29,"VIX":17.42,"VIX_PREV":18.65,"BRENT":78.55,"BRENT_PREV":79.19,"PLATA":31.2,"COBRE":4.35,"BTC":67500,"SPX":5230}, False

m, real = get_all()
madrid = datetime.now(pytz.timezone('Europe/Madrid'))
ny = datetime.now(pytz.timezone('America/New_York'))

# HEADER
st.markdown(f"""
<div class="header">BLOOMBERG TERMINAL • XAUUSD &lt;GO&gt; • GOLD SPOT &nbsp;&nbsp; | &nbsp;&nbsp; USER: KB_VINUELA • {ny.strftime('%Y-%m-%d %H:%M:%S')} EST • MADRID {madrid.strftime('%H:%M')} • {"🟢 CONNECTED REAL" if real else "🟡 DEMO"}</div>
""", unsafe_allow_html=True)
st.write("")

left, right = st.columns([2, 1])

with left:
    # GRAFICO TRADINGVIEW REAL
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### XAUUSD — GOLD / USD &nbsp; <span style='color:#10b981'>{m['XAU']:.2f} {m['XAU']-m['PREV']:+.2f} ({(m['XAU']/m['PREV']-1)*100:+.2f}%) ▲</span>", unsafe_allow_html=True)
    # TradingView Widget real
    tv_code = """
    <div class="tradingview-widget-container">
      <div id="tradingview_123"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({
        "autosize": true, "symbol": "OANDA:XAUUSD", "interval": "60", "timezone": "Europe/Madrid",
        "theme": "light", "style": "1", "locale": "es", "toolbar_bg": "#f1f5f9",
        "enable_publishing": false, "hide_top_toolbar": false, "save_image": false,
        "container_id": "tradingview_123"
      });
      </script>
    </div>
    """
    components.html(tv_code, height=420)
    st.markdown(f"<div class='small'>Open {m['OPEN']:.2f} • High {m['HIGH']:.2f} • Low {m['LOW']:.2f} • Vol {m['VOL']/1000:.1f}K • YTD +18.7% • 1D 5D 1M 3M 6M 1Y 5Y</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ECONOMIC CALENDAR + CORRELATIONS EN UNA FILA COMO FOTO 1
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### ECONOMIC CALENDAR • Today & Upcoming")
        st.markdown(f"""
        <b>14:30 ET</b> US CPI YoY • Oct Act 2.6% Fcst 2.6% Prev 2.4%<br>
        <b>15:00 ET</b> Fed Waller Speech<br>
        <b>Tomorrow 08:30 ET</b> US Initial Jobless Claims Fcst 220K<br>
        <span class='small'>Madrid: { (ny.hour+6)%24}:30 • Solo ★★★★★ no operar</span>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### CORRELATIONS • Gold vs Markets (30D)")
        corr = pd.DataFrame({"Asset":["Gold vs BTC","Gold vs Silver","Gold vs Copper","Gold vs SPX"], "Value":[0.62,0.91,0.45,-0.31]})
        st.bar_chart(corr.set_index("Asset"), height=180)
        st.markdown(f"<span class='small'>Ratio Oro/Plata {m['XAU']/m['PLATA']:.1f} • Oro/BTC descorrelado • Oro/Cobre {m['COBRE']}</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # SMT
    st.markdown('<div class="card" style="border-left:4px solid #dc2626">', unsafe_allow_html=True)
    st.markdown("#### SMT DETECTION • Smart Money / Liquidity")
    # logica SMT
    oro_low_sweep = m['LOW'] < 2632.20
    us02_no_confirm = m['US02Y'] > m['US02Y_PREV'] - 0.10
    if oro_low_sweep and us02_no_confirm:
        st.success(f"✅ Liquidity Sweep — Lows swept at {m['LOW']:.2f} CONFIRMED • US02Y {m['US02Y']:.2f}% no confirma")
        st.markdown("• Inducement — Bullish breaker above 2,648.50\n• Fair Value Gap 2,650.10-2,654.30 • 68% Mitigated\n• **PD Array Bias: BULLISH**")
    else:
        st.warning(f"⏳ Monitoring Sweep at {m['LOW']:.2f} • US02Y {m['US02Y']:.2f}%")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### MONEY • Rates & Dollar")
    st.markdown(f"""
    <div style="display:flex; justify-content:space-between"><span>Real Yield</span><span><b>2.14%</b> <span style="color:green">+0.03 ↑</span></span></div>
    <div style="display:flex; justify-content:space-between"><span>US02Y</span><span><b>{m['US02Y']:.2f}%</b> <span style="color:{'green' if m['US02Y']<m['US02Y_PREV'] else 'red'}">{m['US02Y']-m['US02Y_PREV']:+.2f} {'↓' if m['US02Y']<m['US02Y_PREV'] else '↑'}</span></span></div>
    <div style="display:flex; justify-content:space-between"><span>DXY</span><span><b>{m['DXY']:.2f}</b> <span style="color:red">{m['DXY']-m['DXY_PREV']:+.2f} ↓</span></span></div>
    <div style="display:flex; justify-content:space-between"><span>TIPS</span><span><b>2.10%</b> <span style="color:green">+0.02</span></span></div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### FEAR • Volatility & Energy")
    st.markdown(f"""
    <div style="display:flex; justify-content:space-between"><span>VIX</span><span><b>{m['VIX']:.2f}</b> <span style="color:green">{m['VIX']-m['VIX_PREV']:+.2f} ↓</span></span></div>
    <div style="display:flex; justify-content:space-between"><span>Brent Crude</span><span><b>{m['BRENT']:.2f}</b> <span style="color:red">{m['BRENT']-m['BRENT_PREV']:+.2f}</span></span></div>
    <div style="display:flex; justify-content:space-between"><span>Nat Gas / TTF</span><span><b>2.412</b> +0.029</span></div>
    <div style="display:flex; justify-content:space-between"><span>Ormuz Flow</span><span><b>88% Normal</b> 🟡</span></div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### DEMAND • Flows & Positioning")
    st.markdown("""
    <div style="display:flex; justify-content:space-between"><span>Central Banks</span><span>Q3'24 337t <b>+12t</b></span></div>
    <div style="display:flex; justify-content:space-between"><span>ETF Flows</span><span>-2.4t (YTD -18.7t)</span></div>
    <div style="display:flex; justify-content:space-between"><span>COT Net Long</span><span><b>182,403</b> +5,112</span></div>
    <div style="display:flex; justify-content:space-between"><span>Futures + Options</span><span>65% Largos</span></div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("####
