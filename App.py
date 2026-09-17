import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide", page_icon="💰")

# ESTILOS
st.markdown("""
<style>
.stApp{background:#FFFFFF}
.gold-bar{background:#111;color:#FFD60A;text-align:center;padding:12px;font-weight:900;border-radius:8px;font-size:16px}
.card{border:1px solid #eee;border-radius:10px;padding:15px;background:white}
</style>
""", unsafe_allow_html=True)

# CABECERA
c1,c2,c3 = st.columns([1,2.2,2.5])

with c1:
    try: st.image("logo.png", width=180)
    except: st.markdown("### KB")
    madrid = datetime.now(pytz.timezone('Europe/Madrid')).strftime("%H:%M:%S")
    st.caption(f"🕒 Madrid: {madrid}")

with c2:
    st.markdown("<h1 style='font-weight:900;line-height:0.9;margin-top:10px'>KB VIÑUELA<br>TRADING</h1>", unsafe_allow_html=True)
    st.markdown("<div class='gold-bar'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)
    st.markdown("### XAUUSD - ORO")
    components.html("""<div class="tradingview-widget-container"><script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>{"symbol": "OANDA:XAUUSD","width": "100%","colorTheme": "light","isTransparent": true}</script></div>""", height=80)

with c3:
    with st.container(border=True):
        st.markdown("*⚡ ACCESO RÁPIDO*")
        b1,b2,b3 = st.columns(3)
        b1.link_button("▶️ YouTube", "https://www.youtube.com", use_container_width=True)
        b2.link_button("📊 Excel", "https://github.com/karimtopaz76-byte/kb-tablero/blob/main/trading.xlsx", use_container_width=True)
        b3.link_button("📈 TradingView", "https://www.tradingview.com/chart/?symbol=OANDA%3AXAUUSD", use_container_width=True)
        
        st.divider()
        st.markdown("*📂 SEGUIMIENTO TRADING*")
        try:
            df = pd.read_excel("trading.xlsx")
            st.dataframe(df, use_container_width=True, height=220)
        except:
            st.warning("trading.xlsx no encontrado")
            st.dataframe(pd.DataFrame({"Fecha":["HOY"],"Par":["XAUUSD"],"Resultado":["-"]}), use_container_width=True)

        st.divider()
        st.markdown("*📊 TENDENCIA*")
        d1 = st.selectbox("DIARIO D1", ["ALCISTA 🟢","BAJISTA 🔴","LATERAL ⚪"], key="d1")
        h4 = st.selectbox("H4", ["ALCISTA 🟢","BAJISTA 🔴","LATERAL ⚪"], key="h4")
        if "ALCISTA" in d1 and "ALCISTA" in h4: 
            st.success("✅ SOLO BUSCAR COMPRAS")
        elif "BAJISTA" in d1 and "BAJISTA" in h4: 
            st.error("🔻 SOLO BUSCAR VENTAS")
        else: 
            st.warning("⚠️ ESPERA - SIN TENDENCIA CLARA")

# GRAFICO PRINCIPAL
st.divider()
st.markdown("### 📈 GRÁFICO XAUUSD - OANDA")
components.html('<div id="tv1" style="height:650px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","container_id":"tv1"});</script>', height=670)

# SEGUNDA FILA - LO QUE TE FALTABA
st.divider()
k1,k2,k3 = st.columns(3)

with k1:
    with st.container(border=True):
        st.markdown("*✅ CHECKLIST 5/5 (REGLA DE ORO)*")
        c_a = st.checkbox("1. Tendencia D1 + H4 alineada")
        c_b = st.checkbox("2. Zona de liquidez clara")
        c_c = st.checkbox("3. BOS / CHoCH en M15")
        c_d = st.checkbox("4. Entrada en FVG / OB")
        c_e = st.checkbox("5. RR mínimo 1:2")
        total = sum([c_a,c_b,c_c,c_d,c_e])
        st.progress(total/5)
        if total==5: st.success("🔥 5/5 - PUEDES OPERAR")
        else: st.error(f"{total}/5 - NO OPERES")

with k2:
    with st.container(border=True):
        st.markdown("*💰 CALCULADORA LOTE ORO*")
        balance = st.number_input("Balance $", value=1000)
        riesgo = st.number_input("Riesgo %", value=1.0)
        sl = st.number_input("SL en $ oro (ej: 3 = 3$)", value=2.5)
        if sl>0:
            lote = (balance * riesgo/100) / (sl*100) # aprox oro
            st.metric("Lote recomendado", f"{lote:.2f}")
        st.caption("Fórmula para XAUUSD: (Balance*%Riesgo)/(SL*100)")

with k3:
    with st.container(border=True):
        st.markdown("*🗓️ CALENDARIO ECONÓMICO*")
        components.html("""<div style="height:350px"><script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>{"colorTheme": "light","isTransparent": true,"width": "100%","height": "330","importanceFilter": "0,1"}</script></div>""", height=360)

st.markdown("<center><small>KB VIÑUELA TRADING © 2026 - Hecho con disciplina</small></center>", unsafe_allow_html=True)
