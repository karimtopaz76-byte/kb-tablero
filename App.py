import streamlit as st
from datetime import datetime
import pytz
import streamlit.components.v1 as components

st.set_page_config(page_title="KB VINUELA TRADING", page_icon="👑", layout="wide")

# ESTILO NEGRO Y DORADO COMO TU LOGO
st.markdown("""
<style>
.hora-oro {
    background-color: #000000;
    color: #C9A86A;
    border: 1.5px solid #C9A86A;
    border-radius: 10px;
    padding: 14px 10px;
    text-align: center;
    font-weight: 800;
    font-size: 18px;
    font-family: serif;
    letter-spacing: 1px;
    box-shadow: 0 0 12px rgba(201,168,106,0.4);
}
</style>
""", unsafe_allow_html=True)

# CABECERA
col_logo, col_titulo, col_hora = st.columns([1, 2.5, 1.2])

with col_logo:
    try:
        st.image("logo.png", width=145)
    except:
        st.markdown("## 👑")

with col_titulo:
    st.markdown("## KB VIÑUELA TRADING")
    st.caption("Diario 100% funcional + Escudo + 3 Estrellas")

with col_hora:
    # RELOJ NEGRO/DORADO AUTOMATICO CON JAVASCRIPT - SIN LIBRERIAS
    components.html("""
    <div id="reloj" class="hora-oro" style="
        background-color:#000000; color:#C9A86A; border:1.5px solid #C9A86A;
        border-radius:10px; padding:14px 10px; text-align:center;
        font-weight:800; font-size:18px; font-family:serif;">
    </div>
    <script>
    function actualizarHora() {
        const ahora = new Date().toLocaleString("es-ES", {timeZone: "Europe/Madrid"});
        const fecha = new Date().toLocaleString("es-ES", {timeZone: "Europe/Madrid", day:'2-digit', month:'2-digit', year:'numeric'});
        const hora = new Date().toLocaleTimeString("es-ES", {timeZone: "Europe/Madrid", hour:'2-digit', minute:'2-digit'});
        document.getElementById("reloj").innerHTML = hora + " MADRID<br><span style='font-size:13px; font-weight:400;'>" + fecha + "</span>";
    }
    setInterval(actualizarHora, 1000);
    actualizarHora();
    </script>
    """, height=85)

st.divider()

# CUERPO
col_izq, col_der = st.columns([1.2, 1])

with col_izq:
    st.subheader("📅 CALENDARIO - SOLO 3 ESTRELLAS")
    components.iframe(
        "https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12",
        height=650, scrolling=True
    )

with col_der:
    madrid_tz = pytz.timezone('Europe/Madrid')
    hoy_str = datetime.now(madrid_tz).strftime("%d-%m-%Y")
    st.subheader(f"📊 PILARES - HOY {hoy_str}")
    st.error("**PILAR 1 - IPC USA:** 3.4% Agosto - NEUTRO-ALTO")
    st.warning("**PILAR 3 - FED:** 3.75% - 4.00% (17 Sep) - DXY 99.67 FUERTE")
    st.success("**PILAR 2 - NFP:** Si >200k = DXY FUERTE / ORO BAJA")
    st.info("**KILLZONE:** 08-11h Londres | 14-17h NY Madrid")
    
    with st.expander("🎯 ESTRATEGIA FUERTE"):
        st.write("NFP +200k -> Venta ORO en Killzone")
    with st.expander("😌 ESTRATEGIA CALMA"):
        st.write("Rango 2140-2180, esperar")
