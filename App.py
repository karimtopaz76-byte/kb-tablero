import streamlit as st
from datetime import datetime
import pytz
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components

# Auto-refresco cada 60 segundos para la hora
st_autorefresh(interval=60 * 1000, key="reloj_madrid")

st.set_page_config(page_title="KB VIÑUELA TRADING", layout="wide")

# CSS cuadro negro / dorado
st.markdown("""
<style>
.hora-oro {
    background-color: #000000;
    color: #C9A86A;
    border: 1.5px solid #C9A86A;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: center;
    font-weight: 700;
    font-family: serif;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# CABECERA
col_logo, col_titulo, col_hora = st.columns([1, 3, 1.3])

with col_logo:
    try:
        st.image("logo.png", width=140)
    except:
        st.markdown("### 👑 KB")

with col_titulo:
    st.markdown("## KB VIÑUELA TRADING")
    st.caption("Diario 100% funcional + Escudo")

with col_hora:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    hora_html = f"""
    <div class="hora-oro">
        {madrid.hour:02d}:{madrid.minute:02d} MADRID<br>
        <span style="font-size:12px">{madrid.day:02d}/{madrid.month:02d}/{madrid.year}</span>
    </div>
    """
    st.markdown(hora_html, unsafe_allow_html=True)

st.divider()

# CUERPO
col_cal, col_pil = st.columns(2)

with col_cal:
    st.subheader("CALENDARIO - SOLO 3 ESTRELLAS")
    components.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=600, scrolling=True)

with col_pil:
    hoy = datetime.now(pytz.timezone('Europe/Madrid')).strftime("%d-%m-%Y")
    st.subheader(f"PILARES - HOY {hoy}")
    
    st.error("PILAR 1 - IPC USA: 3.4% Agosto - NEUTRO-ALTO = Cuidado ORO")
    st.warning("PILAR 3 - FED HOY: 3.75% - 4.00% - Subio ayer 17 Sep - Tasa SUBE = DXY SUBE / ORO BAJA CORTO")
    
    with st.expander("Fuerte +200k - Oro baja"):
        st.write("Si NFP > 200k, DXY fuerte, ORO corto")
    
    with st.expander("Calma"):
        st.write("Mercado en rango, esperar Killzone")
        
    st.info("Killzone 08-11h y 14-17h Madrid - DXY 99.67 fuerte")
