import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import streamlit.components.v1 as components
st.set_page_config(page_title="KB VINUELA TRADING", page_icon="👑", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
.stApp {background-color:#0a0a0a; color:#e0e0e0;}
h1,h2,h3 {color:#C9A86A !important; font-family:serif;}
</style>
""", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1.2, 2, 1.2])
with c1:
    try:
        st.image("logo.png", width=160)
    except:
        st.markdown('<div style="background:#000;border:2px solid #C9A86A;color:#C9A86A;padding:20px;text-align:center;font-weight:900;font-size:22px;border-radius:10px;">KB<br>VINUELA</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<h1 style="text-align:center;margin:0;">KB VIÑUELA TRADING</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;color:#C9A86A;letter-spacing:2px;">FRANCOTIRADOR - ORO & DXY</p>', unsafe_allow_html=True)
with c3:
    components.html("""
    <div id="reloj" style="background:#000;color:#C9A86A;border:2px solid #C9A86A;border-radius:12px;padding:14px;text-align:center;font-weight:900;font-family:serif;font-size:18px;"></div>
    <script>
    function tick(){
        const h=new Date().toLocaleTimeString("es-ES",{timeZone:"Europe/Madrid",hour:'2-digit',minute:'2-digit',second:'2-digit'});
        const d=new Date().toLocaleDateString("es-ES",{timeZone:"Europe/Madrid",weekday:'short',day:'2-digit',month:'short'});
        document.getElementById("reloj").innerHTML=h+" MADRID<br><span style='font-size:11px'>"+d.toUpperCase()+"</span>";
    }
    setInterval(tick,1000);tick();
    </script>
    """, height=90)
st.divider()
tab1, tab2, tab3, tab4, tab5 = st.tabs(["⚡ PILARES HOY", "📅 CALENDARIO 3⭐", "📈 GRAFICOS XAU & DXY", "🎯 CHECKLIST FRANCOTIRADOR", "📓 DIARIO COMPLETO"])
with tab1:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.subheader(f"PILARES FUNDAMENTALES - {madrid.strftime('%d/%m/%Y')}")
    colA, colB, colC = st.columns(3)
    with colA:
        st.error("**IPI / IPC USA:** 3.4% - NEUTRO-ALTO - ORO presionado")
        st.warning("**NFP:** >200k = DXY FUERTE = VENTA ORO | <150k = COMPRA ORO")
    with colB:
        st.info("**VIX:** <15 = ORO cae | >20 = ORO sube")
        st.success("**DXY:** 99.67 - FUERTE")
    with colC:
        st.markdown("**🌍 GEOPOLITICA**")
        st.write("- Medio Oriente: Soporte ORO")
        st.write("- Fed 17 Sep: 3.75%-4.00%")
        st.write("- Killzones 08-11h y 14-17h Madrid")
with tab2:
    st.subheader("Calendario 3 Estrellas")
    components.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=700, scrolling=True)
with tab3:
    st.subheader("Graficos en Vivo")
    g1, g2 = st.columns(2)
    with g1:
        st.markdown("**XAUUSD - ORO**")
        components.html("""<div id="tv_xau"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"dark","style":"1","locale":"es","height":400,"container_id":"tv_xau"});</script>""", height=420)
    with g2:
        st.markdown("**DXY**")
        components.html("""<div id="tv_dxy"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"CAPITALCOM:DXY","interval":"60","timezone":"Europe/Madrid","theme":"dark","style":"1","locale":"es","height":400,"container_id":"tv_dxy"});</script>""", height=420)
with tab4:
    st.subheader("CHECKLIST FRANCOTIRADOR")
    c1, c2 = st.columns(2)
    with c1:
        z1 = st.checkbox("1. Zona de Interes D1 / S1 / M1 marcada")
        z2 = st.checkbox("2. Rechazo de Vela H4")
        z3 = st.checkbox("3. BOS H1")
    with c2:
        z4 = st.checkbox("4. Retraso a FVG 15m")
        z5 = st.checkbox("5. BoS 5m")
        z6 = st.checkbox("6. ENTRADA")
    if all([z1,z2,z3,z4,z5,z6]):
        st.success("✅ TODO VERDE - EJECUTA")
        st.balloons()
    else:
        st.warning(f"Faltan {6 - sum([z1,z2,z3,z4,z5,z6])} pasos")
with tab5:
    st.subheader("Diario KB")
    if "diario" not in st.session_state:
        st.session_state.diario = []
    with st.form("ficha_completa"):
        col1, col2, col3 = st.columns(3)
        with col1:
            ficha = st.text_input("Ficha #", value=f"KB-{datetime.now().strftime('%d%m')}-01")
            instrumento = st.selectbox("Instrumento", ["XAUUSD / ORO", "DXY", "EURUSD", "GBPUSD", "BTCUSD"])
            fundamento = st.selectbox("Fundamento", ["NFP Fuerte", "NFP Debil", "IPC Alto", "IPC Bajo", "FED Hawkish", "FED Dovish", "Geopolitica", "Tecnico puro"])
        with col2:
            tecnico = st.selectbox("Tecnico", ["BOS H1 + FVG 15m", "Rechazo H4", "Zona D1", "FVG 5m", "Killzone NY", "Otro"])
            entrada = st.number_input("Precio Entrada", value=0.0, format="%.2f")
            salida = st.number_input("Precio Salida", value=0.0, format="%.2f")
        with col3:
            sl = st.number_input("SL", value=0.0, format="%.2f")
            tp = st.number_input("TP", value=0.0, format="%.2f")
            resultado = st.selectbox("Resultado", ["En espera", "TP", "SL", "BE"])
        obs = st.text_area("Observaciones")
        if st.form_submit_button("💾 GUARDAR FICHA", use_container_width=True):
            st.session_state.diario.append({"Ficha":ficha,"Instrumento":instrumento,"Fundamento":fundamento,"Tecnico":tecnico,"Entrada":entrada,"Salida":salida,"SL":sl,"TP":tp,"Resultado":resultado,"Obs":obs,"Fecha":datetime.now(pytz.timezone('Europe/Madrid')).strftime('%d-%m %H:%M')})
            st.success(f"Ficha {ficha} guardada")
    if st.session_state.diario:
        df = pd.DataFrame(st.session_state.diario)
        st.dataframe(df, use_container_width=True)
        st.download_button("📥 Descargar CSV", df.to_csv(index=False).encode('utf-8'), "diario_KB.csv", "text/csv")
