import streamlit as st
from datetime import datetime
import pytz
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components

# 1. AUTO REFRESCO CADA 60 SEGUNDOS
st_autorefresh(interval=60 * 1000, key="kb_reloj")

# 2. CONFIGURACION PAGINA
st.set_page_config(
    page_title="KB VIÑUELA TRADING",
    page_icon="👑",
    layout="wide"
)

# 3. ESTILO NEGRO Y DORADO - COMO TU LOGO
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
    font-family: 'Times New Roman', serif;
    letter-spacing: 1px;
    box-shadow: 0 0 12px rgba(201,168,106,0.4);
}
.titulo-oro {
    color: #C9A86A;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 4. CABECERA CON LOGO ESQUERDA + HORA MADRID
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
    madrid_tz = pytz.timezone('Europe/Madrid')
    ahora = datetime.now(madrid_tz)
    html_hora = f"""
    <div class="hora-oro">
        {ahora.hour:02d}:{ahora.minute:02d} MADRID
        <br><span style="font-size:13px; font-weight:400;">{ahora.day:02d}/{ahora.month:02d}/{ahora.year}</span>
    </div>
    """
    st.markdown(html_hora, unsafe_allow_html=True)

st.divider()

# 5. CUERPO PRINCIPAL
col_izq, col_der = st.columns([1.2, 1])

with col_izq:
    st.subheader("📅 CALENDARIO - SOLO 3 ESTRELLAS")
    # Calendario Investing filtrado
    components.iframe(
        "https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12",
        height=650,
        scrolling=True
    )

with col_der:
    hoy_str = ahora.strftime("%d-%m-%Y")
    st.subheader(f"📊 PILARES - HOY {hoy_str}")

    st.error("**PILAR 1 - IPC USA:** 3.4% Agosto - NEUTRO-ALTO = Cuidado ORO sube lento")

    st.warning("**PILAR 3 - FED:** 3.75% - 4.00% (Subio 17 Sep) - Tasa SUBE = DXY SUBE / ORO BAJA en corto")

    st.success("**PILAR 2 - NFP:** Esperando 1er Viernes - Si >200k = DXY FUERTE")

    st.info("**DXY HOY:** 99.67 FUERTE | **ORO:** Soporte 2140 / Resistencia 2180")

    with st.expander("🎯 ESTRATEGIA FUERTE +200k - ORO BAJA"):
        st.write("Si NFP sale +200k, buscamos VENTA ORO en Killzone Londres/NY con DXY fuerte.")

    with st.expander("😌 ESTRATEGIA CALMA - RANGO"):
        st.write("Si datos mixtos, operar rango 2140-2180. No entrar en noticias.")

    st.markdown("---")
    st.markdown("**⏰ KILLZONE MADRID:**")
    st.markdown("**08:00 - 11:00** Londres | **14:00 - 17:00** New York")

st.divider()
st.caption("KB VIÑUELA TRADING © 2026 - Hecho para ganar")
