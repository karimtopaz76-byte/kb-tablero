import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="KB VINUELA TRADING", layout="wide")

c1,c2,c3 = st.columns([1,2.2,2.5])

with c1:
    try: st.image("logo.png", width=180)
    except: pass
with c2:
    st.markdown("<h1 style='font-weight:900;line-height:0.9'>KB VIÑUELA<br>TRADING</h1>", unsafe_allow_html=True)
    st.markdown("<div style='background:#111;color:#FFD60A;text-align:center;padding:12px;font-weight:900;border-radius:8px'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)

    st.markdown("### XAUUSD - ORO")
    with st.container(border=True):
        components.html("""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
          {"symbol": "OANDA:XAUUSD","width": "100%","height": 120,"locale": "es","dateRange": "1D","colorTheme": "light","isTransparent": false}
          </script>
        </div>
        """, height=130)

    st.markdown("### DXY - DOLAR (Inverso al Oro)")
    with st.container(border=True):
        components.html("""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
          {"symbol": "TVC:DXY","width": "100%","height": 120,"locale": "es","dateRange": "1D","colorTheme": "light","isTransparent": false}
          </script>
        </div>
        """, height=130)

with c3:
    with st.container(border=True):
        st.markdown("*⚡ ACCESO RÁPIDO*")
        b1,b2 = st.columns(2)
        b1.link_button("▶️ YouTube", "https://www.youtube.com", use_container_width=True)
        b2.link_button("📊 Excel", "https://github.com/karimtopaz76-byte/kb-tablero/blob/main/trading.xlsx", use_container_width=True)
        st.divider()
        st.markdown("*📂 SEGUIMIENTO*")
        try:
            tmp = pd.read_excel("trading.xlsx", header=None)
            fila = 0
            for i in range(len(tmp)):
                if "Fecha" in str(tmp.iloc[i].values): fila=i; break
            df = pd.read_excel("trading.xlsx", header=fila)
            df = df.dropna(how='all')
            df = df.loc[:, ~df.columns.astype(str).str.contains('Unnamed', na=False)]
            st.dataframe(df, use_container_width=True, height=220)
        except Exception as e:
            st.error(f"{e}")

# GRAFICOS - IDs DIFERENTES PARA QUE NO SALGA APPLE
st.divider()
g1,g2 = st.columns(2)

with g1:
    st.markdown("### 📈 XAUUSD - ORO")
    components.html("""
    <div id="chart_xau" style="height:600px"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"light","container_id":"chart_xau"});
    </script>
    """, height=620)

with g2:
    st.markdown("### 📉 DXY - INDICE DOLAR")
    components.html("""
    <div id="chart_dxy" style="height:600px"></div>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <script>
    new TradingView.widget({"autosize":true,"symbol":"TVC:DXY","interval":"60","timezone":"Europe/Madrid","theme":"light","container_id":"chart_dxy"});
    </script>
    """, height=620)
