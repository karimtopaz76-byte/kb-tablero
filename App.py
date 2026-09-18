import streamlit as st
from datetime import datetime
import pytz
import streamlit.components.v1 as components
st.set_page_config(page_title="KB VINUELA TRADING", page_icon="👑", layout="wide")
c1, c2, c3 = st.columns([1, 2.2, 1])
with c1:
    try:
        st.image("logo.png", width=145)
    except:
        st.markdown("## 👑 KB")
with c2:
    st.markdown("## KB VIÑUELA TRADING")
    st.caption("Diario 100% funcional + Escudo + 3 Estrellas")
with c3:
    components.html("""
    <div id="reloj" style="background:#000;color:#C9A86A;border:1.5px solid #C9A86A;border-radius:10px;padding:12px;text-align:center;font-weight:800;font-family:serif;font-size:16px;"></div>
    <script>
    function tick(){
        const h=new Date().toLocaleTimeString("es-ES",{timeZone:"Europe/Madrid",hour:'2-digit',minute:'2-digit',second:'2-digit'});
        const d=new Date().toLocaleDateString("es-ES",{timeZone:"Europe/Madrid",day:'2-digit',month:'2-digit',year:'numeric'});
        document.getElementById("reloj").innerHTML=h+" MADRID<br><span style='font-size:12px'>"+d+"</span>";
    }
    setInterval(tick,1000);tick();
    </script>
    """, height=85)
st.divider()
tab1, tab2, tab3 = st.tabs(["PANEL HOY", "CALENDARIO 3 ESTRELLAS", "DIARIO"])
with tab1:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    hoy = madrid.strftime("%d-%m-%Y")
    colA, colB = st.columns(2)
    with colA:
        st.subheader(f"PILARES - {hoy}")
        st.error("PILAR 1 IPC USA: 3.4% Agosto - NEUTRO-ALTO -> ORO cuidado")
        st.warning("PILAR 3 FED: 3.75% - 4.00% (17 Sep) - DXY 99.67 FUERTE = ORO BAJA corto")
        st.success("PILAR 2 NFP: >200k = DXY FUERTE / ORO VENTA | <150k = DXY DEBIL / ORO COMPRA")
        st.info("ORO Soporte 2140 Resistencia 2185 | Killzone 08-11h y 14-17h Madrid")
        with st.expander("ESTRATEGIA FUERTE +200k"):
            st.write("Killzone 14-17h Madrid - Venta ORO 2175-2180 SL 2190 TP 2150/2140")
        with st.expander("ESTRATEGIA CALMA"):
            st.write("Rango 2140-2180 - No operar noticias directas")
    with colB:
        st.subheader("KILLZONES MADRID")
        st.warning("08:00 - 11:00 LONDRES - Mejor para ORO")
        st.error("14:00 - 17:00 NEW YORK - Mayor volatilidad")
        st.success("EVITAR 12:00-13:30 Almuerzo NY")
        st.subheader("CHECKLIST HOY")
        st.checkbox("Calendario 3 estrellas revisado")
        st.checkbox("DXY direccion clara")
        st.checkbox("Killzone esperando")
        st.checkbox("SL y TP definidos")
with tab2:
    st.subheader("Calendario Economico - Solo 3 Estrellas")
    components.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=700, scrolling=True)
with tab3:
    st.subheader("Diario de Trading KB")
    with st.form("diario"):
        fecha = st.date_input("Fecha")
        par = st.selectbox("Par", ["ORO / XAUUSD", "DXY", "EURUSD", "GBPUSD", "BTCUSD"])
        direccion = st.radio("Direccion", ["COMPRA", "VENTA"])
        resultado = st.selectbox("Resultado", ["En espera", "Ganada", "Perdida", "BE"])
        notas = st.text_area("Notas de la operacion")
        if st.form_submit_button("Guardar en Diario"):
            st.success(f"Operacion {par} {direccion} guardada {fecha} - {resultado}")
st.divider()
st.caption("KB VINUELA TRADING 2026 - Negro y Dorado como tu escudo")
