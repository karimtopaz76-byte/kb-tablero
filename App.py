with c2:
    st.markdown("<h1 style='margin-top:30px;font-weight:900;line-height:0.9'>KB VINUELA<br>TRADING</h1>", unsafe_allow_html=True)
    st.markdown("<div class='gold-bar'>REGLA DE ORO: SIN 5/5 NO HAY TRADE</div>", unsafe_allow_html=True)

with c3:
    with st.container(border=True):
        st.markdown("*⚡ ACCESO RÁPIDO*")
        b1, b2 = st.columns(2)
        b1.link_button("▶️ YouTube", "https://www.youtube.com", use_container_width=True)
        b2.link_button("📊 Excel", "https://github.com/tebyte/kb-tablero/blob/main/seguiiento%20trading.xlsx", use_container_width=True)

        st.divider()
        st.markdown("*📂 SEGUIMIENTO*")
        try:
            df = pd.read_excel("seguiiento trading.xlsx")
            st.dataframe(df, height=150, use_container_width=True)
        except:
            st.caption("Excel no encontrado, súbelo a GitHub")

        st.divider()
        st.markdown("*💰 XAUUSD*")
        components.html("""
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
        {"symbol": "OANDA:XAUUSD", "width": "100%", "colorTheme": "light", "isTransparent": true}
        </script>
        """, height=70)

        st.divider()
        d1 = st.selectbox("DIARIO", ["ALCISTA 🟢", "BAJISTA 🔴", "LATERAL ⚪"], key="d1")
        h4 = st.selectbox("H4", ["ALCISTA 🟢", "BAJISTA 🔴", "LATERAL ⚪"], key="h4")
        if "ALCISTA" in d1 and "ALCISTA" in h4:
            st.success("✅ SOLO COMPRAS")
        elif "BAJISTA" in d1 and "BAJISTA" in h4:
            st.error("🔻 SOLO VENTAS")
        else:
            st.warning("⚠️ ESPERA")
