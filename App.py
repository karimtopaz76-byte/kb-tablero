import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide")

c1,c2,c3 = st.columns([1,2,2.3])

with c1:
    try:
        st.image("logo.png", width=160)
    except:
        st.write("KB")

with c2:
    st.markdown("<h1 style='font-weight:900'>KB VINUELA<br>TRADING</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background:#111;color:#FFD60A;text-align:center;padding:10px;font-weight:900;border-radius:8px'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)

with c3:
    with st.container(border=True):
        st.markdown("*⚡ ACCESO RÁPIDO*")
        b1,b2 = st.columns(2)
        b1.link_button("▶️ YouTube", "https://www.youtube.com", use_container_width=True)
        b2.link_button("📊 Excel", "https://github.com/karimtopaz76-byte/kb-tablero/blob/main/trading.xlsx", use_container_width=True)
        st.divider()
        st.markdown("*📂 SEGUIMIENTO*")
        try:
            df = pd.read_excel("trading.xlsx")
            st.dataframe(df, use_container_width=True, height=200)
        except Exception as e:
            st.error(f"Error: {e}")
        st.divider()
        d1 = st.selectbox("DIARIO", ["ALCISTA 🟢","BAJISTA 🔴","LATERAL ⚪"])
        h4 = st.selectbox("H4", ["ALCISTA 🟢","BAJISTA 🔴","LATERAL ⚪"])
        if "ALCISTA" in d1 and "ALCISTA" in h4:
            st.success("✅ SOLO COMPRAS")
        elif "BAJISTA" in d1 and "BAJISTA" in h4:
            st.error("🔻 SOLO VENTAS")
        else:
            st.warning("⚠️ ESPERA")

st.divider()
st.markdown("### XAUUSD - OANDA")
components.html('<div id="tv" style="height:600px"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","container_id":"tv"});</script>', height=620)
