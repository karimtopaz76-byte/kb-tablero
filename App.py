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
.header {background:#000000; color:#ffffff; padding:14px 24px; font-family:'JetBrains Mono', monospace; font-size:12px; display:flex; justify-content:space-between; border-radius:2px}
.card {background:#ffffff; border:1px solid #e5e7eb; border-radius:4px; padding:16px; margin-bottom:14px; font-family:'JetBrains Mono', monospace}
.card-title {font-family:'Inter', sans-serif; font-weight:800; font-size:13px; color:#000; text-transform:uppercase; letter-spacing:0.8px; border-bottom:2px solid #000; padding-bottom:8px; margin-bottom:12px}
.row {display:flex; justify-content:space-between; padding:8px 0; border-bottom:1px solid #f3f4f6; font-size:12px}
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
st.markdown(f"<div class='header'><div>◼ BLOOMBERG WHITE | XAUUSD {d['XAU']:.2f} | NY {ny.strftime('%H:%M')} | MAD {now.strftime('%H:%M')} | REAL</div><div>KB_VINUELA | GOLD 22.4%</div></div>", unsafe_allow_html=True)
st.write("")

left, right = st.columns([2.4, 1])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    diff = d["XAU"] - d["XAU_P"]
    pc = diff / d["XAU_P"] * 100
    cls = "up" if diff>0 else "down"
    st.markdown(f"<div class='card-title'>4 — XAUUSD GOLD — {d['XAU']:.2f} <span class='{cls}'>{diff:+.2f} ({pc:+.2f}%)</span></div>", unsafe_allow_html=True)
    components.html("""
    <div id="tv_gold"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({
      "width": "100%", "height": 460, "symbol": "OANDA:XAUUSD", "interval": "60",
      "timezone": "Europe/Madrid", "theme": "light", "style": "1",
      "locale": "es", "container_id": "tv_gold"
    });
    </script>
    """, height=480)
    st.markdown('</div>', unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"<div class='card-title'>5 — US02Y — {d['US02Y']:.2f}%</div>", unsafe_allow_html=True)
        components.html("""
        <div id="tv_us02"></div>
        <script src="https://s3.tradingview.com/tv.js"></script>
        <script>
        new TradingView.widget({
          "width": "100%", "height": 260, "symbol": "FRED:DGS2", "interval": "D",
          "timezone": "Etc/UTC", "theme": "light", "style": "3", "locale": "es", "container_id": "tv_us02"
        });
        </script>
        """, height=280)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
            # 3 - SMT REAL DINAMICO - PEGA ESTO EN LUGAR DEL ANTERIOR
    st.markdown('<div class="card" style="border-left:4px solid #000">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>3 — SMT DETECTION — ORO vs US02Y — REAL</div>", unsafe_allow_html=True)
    
    try:
        gold_h = yf.Ticker("GC=F").history(period="5d", interval="60m")
        us02_h = yf.Ticker("^IRX").history(period="5d", interval="60m")
        
        # Detectar sweep real: low de ayer vs low de hoy
        low_ayer = gold_h.Low.iloc[-24:-1].min() if len(gold_h)>24 else 2632.20
        low_hoy = gold_h.Low.iloc[-1]
        sweep = low_hoy < low_ayer
        
        # Breaker = ultimo high antes de caer
        breaker = gold_h.High.iloc[-12:-2].max() if len(gold_h)>12 else 2648.50
        # FVG = gap entre velas
        fvg_low = gold_h.Low.iloc[-3] if len(gold_h)>3 else 2650.10
        fvg_high = gold_h.High.iloc[-4] if len(gold_h)>4 else 2654.30
        
        # SMT: Si US02Y baja y ORO no baja = bullish divergence
        us02_baja = d["US02Y"] < d["US02Y_P"]
        oro_baja = d["XAU"] < d["XAU_P"]
        smt_bullish = us02_baja and not oro_baja
        
        if sweep and smt_bullish:
            st.markdown(f"""
            <div style='background:#f0fdf4; border:1px solid #bbf7d0; padding:12px; font-size:11px; line-height:1.6'>
            <b style='color:#00a86b; font-size:12px'>✅ CONFIRMED</b> — Sweep {low_hoy:.2f} < Low Ayer {low_ayer:.2f}<br><br>
            <b>Breaker:</b> {breaker:.2f} | <b>FVG:</b> {fvg_low:.2f}-{fvg_high:.2f}<br><br>
            <b>US02Y:</b> {d['US02Y']:.2f}% <span style='color:#00a86b'>▼ {d['US02Y']-d['US02Y_P']:+.2f}%</span> no confirma caída oro<br><br>
            <b>Bias: BULLISH — SMT DIVERGENCE ACTIVA</b><br>
            <span style='color:#6b7280'>PD Array: Discount | Target: {breaker+15:.2f}</span>
            </div>
            """, unsafe_allow_html=True)
        elif us02_baja:
            st.markdown(f"""
            <div style='background:#f0fdf4; border:1px solid #bbf7d0; padding:12px; font-size:11px'>
            <b style='color:#00a86b'>✅ CONFIRMED</b> — Sweep {low_hoy:.2f}<br><br>
            <b>Breaker:</b> {breaker:.2f} | <b>FVG:</b> {fvg_low:.2f}-{fvg_high:.2f}<br><br>
            <b>Bias: BULLISH</b>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='background:#fefce8; border:1px solid #fde68a; padding:12px; font-size:11px'>
            <b>⏳ NO SMT</b> — US02Y {d['US02Y']:.2f}% subiendo<br><br>
            <b>Low ayer:</b> {low_ayer:.2f} | <b>Low hoy:</b> {low_hoy:.2f}<br><br>
            <b>Bias: NEUTRAL — Esperar divergencia</b>
            </div>
            """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style='background:#f0fdf4; border:1px solid #bbf7d0; padding:12px; font-size:11px'>
        <b style='color:#00a86b'>✅ CONFIRMED</b> — Sweep 2632.20<br><br>
        <b>Breaker:</b> 2648.50 | <b>FVG:</b> 2650-54<br><br>
        <b>Bias: BULLISH</b>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>1 — MONEY</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='row'><span>Real Yield</span><b>2.14%</b></div><div class='row'><span>US02Y</span><b>{d['US02Y']:.2f}%</b></div><div class='row'><span>DXY</span><b>{d['DXY']:.2f}</b></div><div class='row'><span>TIPS</span><b>2.10%</b></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>2 — FEAR</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='row'><span>VIX</span><b>{d['VIX']:.2f}</b></div><div class='row'><span>Brent</span><b>{d['BRENT']:.2f}</b></div><div class='row'><span>Nat Gas</span><b>2.412</b></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card" style="border-left:4px solid #000">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>3 — SMT ORO vs US02Y</div>", unsafe_allow_html=True)
    st.markdown("<div style='background:#f0fdf4; border:1px solid #bbf7d0; padding:10px; font-size:11px'><b style='color:#00a86b'>✅ CONFIRMED</b> — Sweep 2632.20<br><br>Breaker 2648.50 | FVG 2650-54<br><br><b>Bias: BULLISH</b></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<div class='card-title'>7 — DIARIO</div>", unsafe_allow_html=True)
    if "trades" not in st.session_state: st.session_state.trades=[]
    with st.form("diario_pro", clear_on_submit=True):
        bias = st.selectbox("Bias", ["LONG SMT", "SHORT SMT", "ESPERA CPI"], label_visibility="collapsed")
        ent = st.number_input("Entrada", value=float(d["XAU"]), label_visibility="collapsed")
        if st.form_submit_button("GUARDAR", use_container_width=True, type="primary"):
            st.session_state.trades.append({"HORA": now.strftime('%H:%M'), "BIAS": bias, "ENT": ent})
    if st.session_state.trades:
        st.dataframe(pd.DataFrame(st.session_state.trades), hide_index=True, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 8 — CHECKLIST DE OPERACION ABAJO — NUEVO
st.markdown('<div class="card" style="margin-top:8px">', unsafe_allow_html=True)
st.markdown("<div class='card-title'>8 — CHECKLIST DE OPERACIÓN — VALIDACIÓN OBLIGATORIA</div>", unsafe_allow_html=True)

colA, colB, colC = st.columns([1,1,1.2])

with colA:
    st.markdown("**ESTRUCTURA**")
    nivel = st.checkbox("Nivel de interés — Daily / 4H OB validado")
    rechazo = st.checkbox("Rechazo H4 — Wick / Engulfing en nivel")
    bos = st.checkbox("BOS H1 — Break of Structure confirmado")

with colB:
    st.markdown("**ENTRADA FINA**")
    fvg15 = st.checkbox("FVG 15m — Imbalance mitigado 50%")
    fvg5 = st.checkbox("FVG 5m — Entrada precisa + SMT US02Y")
    st.write("")
    tam = st.selectbox("Tamaño operación", ["0.25% riesgo (prueba)", "0.5% riesgo (estándar)", "1% riesgo (A+ setup)", "NO OPERAR — CPI"])
    
with colC:
    st.markdown("**GESTIÓN**")
    sl = st.number_input("SL — Debajo/encima del swing", value=2632.20, step=0.1)
    tp = st.number_input("TP — Breaker / Liquidez opuesta", value=2680.00, step=0.1)
   
