import streamlit as st
from datetime import datetime
import pytz

# Configuración de la página
st.set_page_config(page_title="KB VINUELA TRADING Premium", page_icon=":moneybag:", layout="wide")

# Colores
color_fondo = "#000000"
color_dorado = "#C9A86A"
color_texto = "#FFFFFF"

# Aplicar estilo general
st.markdown(
    f"""
    <style>
    .main {{
        background-color: {color_fondo};
        color: {color_texto};
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    .stButton>button {{
        background-color: {color_dorado};
        color: {color_fondo};
        font-weight: bold;
    }}
    .stTabs [data-baseweb="tab-list"] button {{
        color: {color_dorado};
        background-color: {color_fondo};
        font-weight: bold;
    }}
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
        border-bottom: 2px solid {color_dorado};
        color: {color_dorado};
    }}
    .pillars {
        font-size: 18px;
        color: {color_dorado};
        font-weight: bold;
        padding: 10px 15px;
        border: 2px solid {color_dorado};
        border-radius: 12px;
        margin-bottom: 10px;
        max-width: 500px;
        background-color: {color_fondo};
    }}
    form {
        background-color: #111111;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid {color_dorado};
        color: {color_dorado};
    }
    label, input, select, textarea {
        color: {color_dorado};
        background-color: {color_fondo};
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Función reloj vivo con actualización cada segundo
def reloj_vivo():
    tz_madrid = pytz.timezone('Europe/Madrid')
    now = datetime.now(tz_madrid)
    fecha_hora = now.strftime("%H:%M:%S")
    # Reloj en negro y dorado con segundos que actualiza
    st.markdown(
        f"""
        <div style="color: {color_dorado}; font-weight: bold; font-family: monospace; font-size: 24px; background-color: {color_fondo}; padding: 5px 15px; border-radius: 8px; border: 2px solid {color_dorado}; width: 130px; text-align: center;">
            {fecha_hora}
        </div>
        """,
        unsafe_allow_html=True
    )
    st.experimental_rerun()

# Header con 3 columnas: logo izq, título centro, reloj der
col1, col2, col3 = st.columns([1, 4, 2])

with col1:
    try:
        st.image("logo.png", width=80)
    except:
        pass

with col2:
    st.markdown(f'<h1 style="color: {color_dorado}; text-align:center; font-family: serif;">KB VINUELA TRADING</h1>',
                unsafe_allow_html=True)

with col3:
    # Mostrar reloj que actualiza cada segundo
    # Aquí la forma sencilla con st.empty para actualizar sin rerun total
    relojeria = st.empty()
    import time
    import threading

    def mostrar_reloj():
        while True:
            now = datetime.now(pytz.timezone('Europe/Madrid'))
            reloj_html = f"""
                <div style="color: {color_dorado}; font-weight: bold; font-family: monospace; font-size: 24px; background-color: {color_fondo}; padding: 5px 15px; border-radius: 8px; border: 2px solid {color_dorado}; text-align: center;">
                    {now.strftime('%H:%M:%S')}
                </div>
            """
            relojeria.markdown(reloj_html, unsafe_allow_html=True)
            time.sleep(1)

    # Ejecutar reloj en hilo para que no bloquee la app
    threading.Thread(target=mostrar_reloj, daemon=True).start()

# Pestañas
tabs = st.tabs(["PANEL HOY", "CALENDARIO", "DIARIO"])

with tabs[0]:
    st.markdown("<h2 style='color: #C9A86A;'>Pilares de Hoy</h2>", unsafe_allow_html=True)

    pilares = [
        "IPC 3.4%",
        "FED 3.75-4%",
        "DXY 99.67 FUERTE",
        "NFP >200k",
        "ORO VENTA",
        "Killzones 08-11h Londres / 14-17h NY"
    ]

    for pilar in pilares:
        st.markdown(f"<div class='pillars'>{pilar}</div>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown("<h2 style='color: #C9A86A;'>Calendario Económico</h2>", unsafe_allow_html=True)
    # iframe de investing.com inserta con timezone Madrid
    # Ajustamos tamaño para que se vea bien
    st.components.v1.html(
        """
        <iframe src="https://es.investing.com/economic-calendar/" width="100%" height="600px" frameborder="0"></iframe>
        """,
        height=600,
        scrolling=True,
    )

with tabs[2]:
    st.markdown("<h2 style='color: #C9A86A;'>Diario de Trading</h2>", unsafe_allow_html=True)
    with st.form(key='diario_form'):
        par = st.text_input("Par (ejemplo: EUR/USD):")
        direccion = st.selectbox("Dirección", ["Compra", "Venta"])
        resultado = st.text_input("Resultado (pips, USD, etc.):")
        enviar = st.form_submit_button("Guardar")
        if enviar:
            st.success(f"Registro guardado:\nPar: {par}, Dirección: {direccion}, Resultado: {resultado}")
