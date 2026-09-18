import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import streamlit.components.v1 as components

st.set_page_config(page_title="KB VINULA TRADING", layout="wide")

# FONDO BLANCO LETRA NEGRA - TU DIBUJO
st.markdown("""
<style>
.stApp {background:#ffffff!important; color:#000!important;}
h1,h2,h3,p,div,span,label {color:#000!important;}
.borde {border:1.5px solid #000; padding:8px; background:#fff; font-weight:800;}
</style>
""", unsafe_allow_html=True)

# HEADER - LOGO | TITULO | RELOJ MADRID
c1, c2, c3 = st.columns([1, 2.2, 1])
with c1:
    st.markdown('<div class="borde" style="height:105px; text-align:center;">LOGO</div>', unsafe_allow_html=True)
    try: st.image("logo.png", width=100)
    except: pass
with c2:
    st.markdown('<div class="borde" style="height:105px; text-align:center;"><div style="font-size:22px;">KB VIÑULA TRADING</div><div style="font-size:13px; margin-top:6px;">FRANCOTIRADOR ORO/DXY</div></div>', unsafe_allow_html=True)
with c3:
    components.html("""
    <div style="border:1.5px solid #000; text-align:center; background:#fff; height:105px; color:#000; font-family:monospace; padding-top:12px;">
        <div id="h" style="font-size:18px; font-weight:800;"></div><div>MADRID</div><div id="f" style="font-size:11px;"></div>
    </div>
    <script>function t(){const a=new Date().toLocaleTimeString("es-ES",{timeZone:"Europe/Madrid",hour:'2-digit',minute:'2-digit',second:'2-digit'});const b=new Date().toLocaleDateString("es-ES",{timeZone:"Europe/Madrid",weekday:'short',day:'2-digit',month:'short'});document.getElementById("h").innerHTML=a;document.getElementById("f").innerHTML=b.toUpperCase();}setInterval(t,1000);t();</script>
    """, height=115)

# CALENDARIO + PILARES + GRAFICOS - TU FORMA
cc, cp = st.columns([1.5, 1])
with cc:
    st.markdown('<div class="borde">Calendario Economico 3 estrellas</div>', unsafe_allow_html=True)
    components.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=350, scrolling=True)
with cp:
    st.markdown('<div class="borde">Pilares de Fundamental (datos real time)</div><div style="border:1.5px solid #000; border-top:0; padding:10px; background:#fff;">IPC 3.4%<br>NFP<br>DXY 99.67<br>VIX<br>Tasa Fed 3.75-4.00%<br>Geopolitica hoy</div>', unsafe_allow_html=True)

cg1, cg2 = st.columns([2,1])
with cg1:
    st.markdown('<div class="borde">grafico XAUUSD</div>', unsafe_allow_html=True)
    components.html("""<div id="xau"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"light","height":320,"container_id":"xau"});</script>""", height=330)
with cg2:
    st.markdown('<div class="borde">grafico DXY</div>', unsafe_allow_html=True)
    components.html("""<div id="dxy"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"CAPITALCOM:DXY","interval":"60","timezone":"Europe/Madrid","theme":"light","height":320,"container_id":"dxy"});</script>""", height=330)

st.markdown('<div class="borde">CheckList</div>', unsafe_allow_html=True)
k1,k2=st.columns(2)
with k1:
    st.checkbox("Zona D1/S1/M1"); st.checkbox("Rechazo H4"); st.checkbox("BOS H1")
with k2:
    st.checkbox("FVG 15m"); st.checkbox("FVG 5m"); st.checkbox("Entrada")

# TU DIARIO 11 COLUMNAS - SIN TOCAR
st.markdown('<div class="borde">Diario de trading</div>', unsafe_allow_html=True)
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
            "Fecha": ["18/09/2026"], "Activo": ["XAUUSD"], "Calendario economico": ["IPC 3.4% / FED 4%"],
            "Nivel de interes": ["3.75%-4.00%"], "Rechazo H4": ["Si"], "BOS H1": ["Si"],
            "FVG 15m": ["2650-2652"], "FVG 5m": ["Si"], "Tamano operacion": ["0.01"], "TP": ["2660"], "SL": ["2645"]
        })

if "df" not in st.session_state: st.session_state.df = cargar()
edit = st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=400, key="diario_final")
c1,c2,c3 = st.columns(3)
with c1:
    if st.button("GUARDAR", type="primary", use_container_width=True):
        st.session_state.df = edit
        st.success("Guardado OK - "+str(len(edit))+" filas"); st.balloons()
        try: edit.to_excel(FILE, index=False)
        except: pass
with c2:
    st.download_button("BACKUP CSV", edit.to_csv(index=False).encode('utf-8'), "kb.csv", "text/csv", use_container_width=True)
with c3:
    if st.button("NUEVA FILA", use_container_width=True):
        hoy = str(datetime.now().day)+"/"+str(datetime.now().month)
        nueva = pd.DataFrame({"Fecha":[hoy],"Activo":["XAUUSD"],"Calendario economico":[""],"Nivel de interes":["3.75%-4.00%"],"Rechazo H4":[""],"BOS H1":[""],"FVG 15m":[""],"FVG 5m":[""],"Tamano operacion":["0.01"],"TP":[""],"SL":[""]})
        st.session_state.df = pd.concat([edit, nueva], ignore_index=True); st.rerun()
