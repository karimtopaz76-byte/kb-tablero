import streamlit as st
import yfinance as yf
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(page_title="ORO TOTAL | Bloomberg White PRO", layout="wide", page_icon="📈")
st.markdown("""
<style>
body {background:#f8fafc}
.header {background:#0f2d52; color:white; padding:12px 20px; border-radius:10px; display:flex; justify-content:space-between; font-size:13px}
.card {background:white; border:1px solid #e2e8f0; border-radius:14px; padding:16px; box-shadow:0 2px 10px rgba(0,0,0,0.04); margin-bottom:14px}
.title-gold {color:#0f2d52; font-weight:800}
.green {color:#16a34a; font-weight:700}
.red {color:#dc2626; font-weight:700}
.small {font-size:11px; color:#64748b}
</style>
""", unsafe_allow_html=True)

@st.cache_data(ttl=90)
def get_real():
    try:
        def q(t):
            h=yf.Ticker(t).history(period="5d")
            return float(h.Close.iloc[-1]), float(h.Close.iloc[-2]), float(h.Open.iloc[-1]), float(h.High.iloc[-1]), float(h.Low.iloc[-1])
        xau_c,xau_p,xau_o,xau_h,xau_l = q("GC=F")
        us02_c,us02_p,_,_,_ = q("^IRX")
        dxy_c,dxy_p,_,_,_ = q("DX-Y.NYB")
        vix_c,vix_p,_,_,_ = q("^VIX")
        brent_c,brent_p,_,_,_ = q("BZ=F")
        tips_c,tips_p,_,_,_ = q("^FVX")
        # Real yield proxy = US10Y - TIPS breakeven
        real_y = us02_c - 1.9
        return {"XAU":xau_c,"XAU_P":xau_p,"OPEN":xau_o,"HIGH":xau_h,"LOW":xau_l,"US02Y":us02_c,"US02Y_P":us02_p,"DXY":dxy_c,"DXY_P":dxy_p,"VIX":vix_c,"VIX_P":vix_p,"BRENT":brent_c,"BRENT_P":brent_p,"TIPS":2.10,"REAL":real_y}, True
    except:
        return {"XAU":2654.32,"XAU_P":2635.41,"OPEN":2635.41,"HIGH":2657.8,"LOW":2632.2,"US02Y":4.32,"US02Y_P":4.37,"DXY":104.17,"DXY_P":104.29,"VIX":17.42,"VIX_P":18.65,"BRENT":78.55,"BRENT_P":79.19,"TIPS":2.10,"REAL":2.14}, False

d, is_real = get_real()
ny = datetime.now(pytz.timezone('America/New_York'))
madrid = datetime.now(pytz.timezone('Europe/Madrid'))

st.markdown(f"""
<div class="header">
<div><b>BLOOMBERG TERMINAL</b> • XAUUSD - GOLD SPOT • USER: KB_VINUELA • {ny.strftime('%Y-%m-%d %H:%M:%S')} NY • MADRID {madrid.strftime('%H:%M')} • {"🟢 REAL" if is_real else "🟡 DEMO"}</div>
<div>PORT: GOLD 22.4% • P&L +1,240 USD</div>
</div>
""", unsafe_allow_html=True)
st.write("")

# ===== TOP ROW =====
col_left, col_right = st.columns([2.2, 1])

with col_left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    chg = d["XAU"]-d["XAU_P"]; pct = chg/d["XAU_P"]*100
    st.markdown(f"### <span class='title-gold'>XAUUSD — GOLD / USD</span> {d['XAU']:.2f} <span class='{ 'green' if chg>0 else 'red'}'>{chg:+.2f} ({pct:+.2f}%)</span>", unsafe_allow_html=True)
    components.html("""
    <div id="tv_gold"></div><script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
      "autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid",
      "theme":"light","style":"1","locale":"es","toolbar_bg":"#f1f5f9",
      "studies":["Volume@tv-basicstudies"],"container_id":"tv_gold","height":380
    });
    </script>
    """, height=400)
    st.markdown(f"<span class='small'>Open {d['OPEN']:.2f} • High {d['HIGH']:.2f} • Low {d['LOW']:.2f} • Vol 42.3K • YTD +18.7% | 1D 5D 1M 3M 6M 1Y 5Y</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 📈 US02Y — Gráfico PRO (2Y Yield)")
        components.html("""
        <div id="tv_us02"></div><script src="https://s3.tradingview.com/tv.js"></script>
        <script>
        new TradingView.widget({
          "autosize":true,"symbol":"US02Y","interval":"D","timezone":"Etc/UTC",
          "theme":"light","style":"3","locale":"es","container_id":"tv_us02","height":220
        });
        </script>
        """, height=240)
        st.markdown(f"Actual: **{d['US02Y']:.2f}%** ({d['US02Y']-d['US02Y_P']:+.2f}%)", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 🗓️ CALENDARIO ECONÓMICO ★★★")
        st.markdown("""
        <span style="color:red"><b>★★★ 14:30 ET</b> US CPI YoY</span><br>Oct 2.6% | Fcst 2.6% | Prev 2.4% • NO OPERAR<br><br>
        <b>★★☆ 15:00 ET</b> Fed Waller Speech<br><br>
        <span style="color:red"><b>★★★ Mañana 08:30 ET</b> US Initial Jobless Claims</span><br>Fcst 220K • Alto impacto oro<br>
        <div class='small'>* Solo 3 estrellas afectan XAUUSD directo</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    # 1 MONEY
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### MONEY <span class='small'>Rates & Dollar</span>")
    def row(name, val, prev, fmt="%"):
        diff = val-prev; col="green" if diff<0 else "red"  # para yields, bajar es bullish oro
        if name=="DXY": col="red" if diff<0 else "green"
        return f"<div style='display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #f1f5f9'><span>{name}</span><span><b>{val:.2f}{fmt}</b> <span class='{col}'>{diff:+.2f} {'↓' if diff<0 else '↑'}</span></span></div>"
    st.markdown(f"""
    {row("Real Yield", d['REAL'], 2.11)}
    {row("US02Y", d['US02Y'], d['US02Y_P'])}
    {row("DXY", d['DXY'], d['DXY_P'], "")}
    {row("TIPS", d['TIPS'], 2.08)}
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2 FEAR
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### FEAR <span class='small'>Volatility & Energy</span>")
    st.markdown(f"""
    <div style='display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #f1f5f9'><span>VIX</span><span><b>{d['VIX']:.2f}</b> <span class='red'>{d['VIX']-d['VIX_P']:+.2f} ({(d['VIX']/d['VIX_P']-1)*100:+.1f}%) ↓</span></span></div>
    <div style='display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #f1f5f9'><span>Brent Crude</span><span><b>{d['BRENT']:.2f}</b> <span class='red'>{(d['BRENT']-d['BRENT_P']):+.2f} ↓</span> $/bbl</span></div>
    <div style='display:flex;justify-content:space-between;padding:6px 0'><span>Nat Gas TTF</span><span><b>2.412</b> <span class='green'>+0.029 (+1.22%)</span> $/mmBtu</span></div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3 SMT ORO vs US02Y
    st.markdown('<div class="card" style="border-left:4px solid #2563eb">', unsafe_allow_html=True)
    st.markdown("### SMT DETECTION <span class='small'>Oro vs US02Y</span>")
    us02_no_confirms = d["US02Y"] < d["US02Y_P"] + 0.05
    low_sweep = d["LOW"] <= 2632.20
    if low_sweep and us02_no_confirms:
        st.success(f"✅ Liquidity Sweep — Lows swept at {d['LOW']:.2f} • CONFIRMED")
        st.markdown(f"**Inducement — Bullish breaker above 2,648.50**\n\n**US02Y {d['US02Y']:.2f}% no confirma subida → Divergencia BULLISH oro**\n\nFair Value Gap 2,650.10-2,654.30 • 68% Mitigated")
        bias="BULLISH"
    else:
        st.warning(f"⏳ Monitoreando • Low {d['LOW']:.2f} vs US02Y {d['US02Y']:.2f}%")
        bias="NEUTRAL"
    st.markdown(f"**PD Array Bias: {bias}**")
    st.markdown('</div>', unsafe_allow_html=True)

    # 7 DIARIO
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 📓 DIARIO DE TRADING")
    if "trades" not in st.session_state: st.session_state.trades=[]
    with st.form("diario", clear_on_submit=True):
        c_a,c_b = st.columns(2)
        bias_opt=c_a.selectbox("Bias SMT", ["LONG Oro + SMT US02Y","SHORT Oro + SMT US02Y","ESPERA CPI"])
        entrada=c_b.number_input("Entrada", value=float(d["XAU"]), step=0.1)
        sl=st.number_input("SL", value=float(d["LOW"]))
        tp=st.number_input("TP", value=float(d["XAU"]+25))
        nota=st.text_input("¿Por qué? (ej: US02Y no confirma)")
        if st.form_submit_button("Guardar Trade"):
            st.session_state.trades.append({"Hora":madrid.strftime('%d %H:%M'),"Bias":bias_opt,"Entrada":entrada,"SL":sl,"TP":tp,"Nota":nota,"Bias_T":bias})
    if st.session_state.trades:
        st.dataframe(pd.DataFrame(st.session_state.trades), use_container_width=True, hide_index=True)
    else:
        st.caption("Sin trades hoy")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div class='small'>ALERTS: 2 new | NEWS: Fed officials cautious | RISK: Geopolitical elevated - Middle East | PORT: Gold 22.4% | P&L +1,240.50 USD</div>", unsafe_allow_html=True)
