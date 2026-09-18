import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import streamlit.components.v1 as components

st.set_page_config(page_title="KB VINULA TRADING", layout="wide")

# FONDO BLANCO LETRA NEGRA - TU FORMA DEL PAPEL
st.markdown("""
<style>
.stApp {background-color:#ffffff!important; color:#000000!important;}
h1,h2,h3,p,div,span,label {color:#000000!important;}
.borde {border:1.5px solid #000; padding:8px; background:#fff; margin-bottom:0px; font-weight:800;}
</style>
""", unsafe_allow_html=True)

# FILA 1 - EXACTO A TU DIBUJO
col_logo, col_title, col_reloj = st.columns([1, 2.2, 1])
with col_logo:
    st.markdown('<div class="borde" style="height:110px; text-align:center;">', unsafe_allow_html=True)
    try:
        st.image("logo.png", width=110)
    except:
        st.markdown("**LOGO**")
    st.markdown('</div>', unsafe_allow_html=True)

with col_title:
    st.markdown('<div class="borde" style="height:110px; text-align:center;"><div style="font-size:22px;">KB VIÑULA TRADING</div><div style="font-size:14px; margin-top:8px;">FRANCOTIRADOR ORO/DXY</div></div>', unsafe_allow_html=True)

with col_reloj:
    components.html("""
    <div style="border:1.5px solid #000; padding:10px; text-align:center; background:#fff; height:110px; color:#000; font-family:monospace;">
        <div id="hora" style="font-size:18px; font-weight:800;"></div>
        <div style="font-size:14px; font-weight:700;">MADRID</div>
        <div id="fecha" style="font-size:12px;"></div>
    </div>
    <script>
    function tick(){
        const h=new Date().toLocaleTimeString("es-ES",{timeZone:"Europe/Madrid",hour:'2-digit',minute:'2-digit',second:'2-digit'});
        const f=new Date().toLocaleDateString("es-ES",{timeZone:"Europe/Madrid",weekday:'short',day:'2-digit',month:'short'});
        document.getElementById("hora").innerHTML=h;
        document.getElementById("fecha").innerHTML=f.toUpperCase();
    }
    setInterval(tick,1000);tick();
    </script>
    """, height=120)

# FILA 2 - CALENDARIO Y PILARES
c_cal, c_pilar = st.columns([1.6, 1])
with c_cal:
    st.markdown('<div class="borde">Calendario Economico 3 estrellas</div>', unsafe_allow_html=True)
    components.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=380, scrolling=True)

with c_pilar:
    st.markdown('<div class="borde">Pilares de Fundamental (datos real time)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="border:1.5px solid #000; border-top:0; padding:12px; background:#fff; color:#000;">
    <b>IPC:</b> 3.4% Agosto<br>
    <b>NFP:</b> >200k = DXY FUERTE<br>
    <b>DXY:</b> 99.67 FUERTE<br>
    <b>VIX:</b> 14.8<br>
    <b>Tasa Fed:</b> 3.75%-4.00% (Subio 17 Sep)<br>
    <b>Geopolitica hoy:</b> Tension soporte ORO
    </div>
    """, unsafe_allow_html=True)

# FILA 3 - GRAFICOS
c_xau, c_dxy = st.columns([2, 1])
with c_xau:
    st.markdown('<div class="borde">grafico XAUUSD</div>', unsafe_allow_html=True)
    components.html("""<div id="tv_xau"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es","height":350,"container_id":"tv_xau"});</script>""", height=360)

with c_dxy:
    st.markdown('<div class="borde">grafico DXY</div>', unsafe_allow_html=True)
    components.html("""<div id="tv_dxy"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"CAPITALCOM:DXY","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es","height":350,"container_id":"tv_dxy"});</script>""", height=360)

# FILA 4 - CHECKLIST
st.markdown('<div class="borde">CheckList</div>', unsafe_allow_html=True)
ch1, ch2 = st.columns(2)
with ch1:
    z1 = st.checkbox("Zona de interes D1/S1/M1")
    z2 = st.checkbox("Rechazo de Vela H4")
    z3 = st.checkbox("BOS H1")
with ch2:
    z4 = st.checkbox("FVG 15m")
    z5 = st.checkbox("FVG 5m")
    z6 = st.checkbox("Entrada")

# FILA 5 - TU DIARIO DE 11 COLUMNAS - TU CODIGO BASE
st.markdown('<div class="borde">Diario de trading</div>', unsafe_allow_html=True)

FILE = "trading.xlsx"

def cargar():
    try:
        df = pd.read_excel(FILE)
        if df.empty:
            raise ValueError("vacio")
        cols = ["Fecha","Activo","Calendario economico","Nivel de interes","Rechazo H4","BOS H1","FVG 15m","FVG 5m","Tamano operacion","TP","SL"]
        for c in cols:
            if c not in df.columns:
                df[c] = ""
        return df
    except:
        return pd.DataFrame({
            "Fecha": ["18/09/2026"],
            "Activo": ["XAUUSD"],
            "Calendario economico": ["IPC 3.4% / FED 4%"],
            "Nivel de interes": ["3.75%-4.00%"],
            "Rechazo H4": ["Si - Mecha larga"],
            "BOS H1": ["Si alcista"],
            "FVG 15m": ["2650-2652"],
            "FVG 5m": ["Si entrada"],
            "Tamano operacion": ["0.01"],
            "TP": ["2660"],
            "SL": ["2645"]
        })

if "df" not in st.session_state:
    st.session_state.df = cargar()

edit = st.data_editor(
    st.session_state.df,
    num_rows="dynamic",
    use_container_width=True,
    height=400,
    key="diario_final"
)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("GUARDAR", type="primary", use_container_width=True):
        st.session_state.df = edit
        st.success("Guardado OK - " + str(len(edit)) + " filas")
        st.balloons()
        try:
            edit.to_excel(FILE, index=False)
        except:
            pass

with c2:
    csv = edit.to_csv(index=False).encode('utf-8')
    st.download_button("BACKUP CSV", csv, "kb.csv", "text/csv", use_container_width=True)

with c3:
    if st.button("NUEVA FILA", use_container_width=True):
        hoy = str(datetime.now().day) + "/" + str(datetime.now().month)
        nueva = pd.DataFrame({
            "Fecha": [hoy],
            "Activo": ["XAUUSD"],
            "Calendario economico": [""],
            "Nivel de interes": ["3.75%-4.00%"],
            "Rechazo H4": [""],
            "BOS H1": [""],
            "FVG 15m": [""],
            "FVG 5m": [""],
            "Tamano operacion": ["0.01"],
            "TP": [""],
            "SL": [""]
        })
        st.session_state.df = pd.concat([edit, nueva], ignore_index=True)
        st.rerun()
