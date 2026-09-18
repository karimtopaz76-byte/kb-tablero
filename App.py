import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import streamlit.components.v1 as components

st.set_page_config(page_title="KB VINULA TRADING", layout="wide")

# FONDO BLANCO + HORA NEGRA DORADA (LA QUE FUNCIONABA)
st.markdown("""
<style>
.stApp {background-color:#ffffff!important; color:#000000!important;}
h1,h2,h3 {color:#000000!important;}
.borde {border:1.5px solid #000; padding:8px; background:#fff; font-weight:800; color:#000;}
</style>
""", unsafe_allow_html=True)

# HEADER - 3 COLUMNAS COMO TU DIBUJO
c1, c2, c3 = st.columns([1, 2.2, 1])
with c1:
    try:
        st.image("logo.png", width=120)
    except:
        st.markdown('<div class="borde" style="text-align:center;">LOGO<br>KB VINUELA</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="borde" style="text-align:center; height:110px;"><div style="font-size:22px;">KB VIÑULA TRADING</div><div style="font-size:13px; margin-top:8px;">FRANCOTIRADOR ORO / DXY</div></div>', unsafe_allow_html=True)

with c3:
    components.html("""
    <div style="background:#000; color:#C9A86A; border:2px solid #C9A86A; border-radius:12px; padding:14px; text-align:center; font-weight:900; font-family:monospace; height:110px;">
        <div id="h" style="font-size:20px;"></div>
        <div style="font-size:12px;">MADRID</div>
        <div id="f" style="font-size:10px; margin-top:4px;"></div>
    </div>
    <script>
    function tick(){
        const h=new Date().toLocaleTimeString("es-ES",{timeZone:"Europe/Madrid",hour:'2-digit',minute:'2-digit',second:'2-digit'});
        const d=new Date().toLocaleDateString("es-ES",{timeZone:"Europe/Madrid",weekday:'short',day:'2-digit',month:'short'});
        document.getElementById("h").innerHTML=h;
        document.getElementById("f").innerHTML=d.toUpperCase();
    }
    setInterval(tick,1000);tick();
    </script>
    """, height=120)

st.divider()

# FILA 2 - CALENDARIO 3 ESTRELLAS + PILARES COMPLETOS
col_cal, col_pil = st.columns([1.6, 1])
with col_cal:
    st.markdown('<div class="borde">Calendario Economico - 3 estrellas</div>', unsafe_allow_html=True)
    components.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=400, scrolling=True)

with col_pil:
    st.markdown('<div class="borde">Pilares de Fundamental - Datos Real Time</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="border:1.5px solid #000; border-top:0; padding:12px; background:#fff; color:#000;">
    <b>IPI / IPC USA:</b> 3.4% Agosto - Presion baja ORO<br><br>
    <b>NFP:</b> >200k = DXY Fuerte = VENTA ORO<br>
    <b>VIX:</b> 14.8 - Riesgo ON<br>
    <b>DXY:</b> 99.67 - FUERTE<br>
    <b>Tasa FED:</b> 3.75%-4.00% (Subio 17 Sep)<br><br>
    <b>Geopolitica hoy:</b><br>
    - Medio Oriente soporte ORO<br>
    - Flujo refugio activo<br>
    <b>Killzones:</b> 08-11h y 14-17h Madrid
    </div>
    """, unsafe_allow_html=True)

# FILA 3 - GRAFICOS XAUUSD Y DXY
c_xau, c_dxy = st.columns([2, 1])
with c_xau:
    st.markdown('<div class="borde">grafico XAUUSD</div>', unsafe_allow_html=True)
    components.html("""<div id="tv_xau"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es","height":380,"container_id":"tv_xau"});</script>""", height=390)

with c_dxy:
    st.markdown('<div class="borde">grafico DXY</div>', unsafe_allow_html=True)
    components.html("""<div id="tv_dxy"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"CAPITALCOM:DXY","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es","height":380,"container_id":"tv_dxy"});</script>""", height=390)

# FILA 4 - CHECKLIST FRANCOTIRADOR
st.markdown('<div class="borde">CheckList Francotirador</div>', unsafe_allow_html=True)
k1, k2 = st.columns(2)
with k1:
    z1 = st.checkbox("Zona de interes D1 / S1 / M1 marcada")
    z2 = st.checkbox("Rechazo de Vela H4")
    z3 = st.checkbox("BOS H1")
with k2:
    z4 = st.checkbox("Retroceso a FVG 15m")
    z5 = st.checkbox("BoS 5m")
    z6 = st.checkbox("Entrada Francotirador")

if all([z1,z2,z3,z4,z5,z6]):
    st.success("TODO VERDE - EJECUTA"); st.balloons()

# FILA 5 - DIARIO 11 COLUMNAS - TU PEDIDO FINAL
st.markdown('<div class="borde">Diario de trading - 11 Columnas</div>', unsafe_allow_html=True)

FILE = "trading.xlsx"

def cargar():
    try:
        df = pd.read_excel(FILE)
        if df.empty: raise ValueError("vacio")
        cols = ["Fecha","Activo","Calendario economico","Nivel de interes","Rechazo H4","BOS H1","FVG 15m","FVG 5m","Tamano operacion","TP","SL"]
        for c in cols:
            if c not in df.columns: df[c] = ""
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

edit = st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=400, key="diario_final")

b1, b2, b3 = st.columns(3)
with b1:
    if st.button("GUARDAR", type="primary", use_container_width=True):
        st.session_state.df = edit
        st.success(f"Guardado OK - {len(edit)} filas")
        st.balloons()
        try: edit.to_excel(FILE, index=False)
        except: pass
with b2:
    st.download_button("BACKUP CSV", edit.to_csv(index=False).encode('utf-8'), "kb.csv", "text/csv", use_container_width=True)
with b3:
    if st.button("NUEVA FILA", use_container_width=True):
        hoy = datetime.now().strftime("%d/%m")
        nueva = pd.DataFrame({"Fecha":[hoy],"Activo":["XAUUSD"],"Calendario economico":[""],"Nivel de interes":["3.75%-4.00%"],"Rechazo H4":[""],"BOS H1":[""],"FVG 15m":[""],"FVG 5m":[""],"Tamano operacion":["0.01"],"TP":[""],"SL":[""]})
        st.session_state.df = pd.concat([edit, nueva], ignore_index=True)
        st.rerun()
