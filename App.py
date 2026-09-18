import streamlit as st, pandas as pd
from datetime import datetime
import pytz
import streamlit.components.v1 as components
st.set_page_config(page_title="KB VINULA TRADING", layout="wide")
st.markdown("""<style>.stApp{background:#fff !important; color:#000 !important;} h1,h2,h3,p,div,span,label{color:#000 !important;} .borde{border:1.5px solid #000; padding:8px; background:#fff;}</style>""", unsafe_allow_html=True)
col_logo, col_title, col_reloj = st.columns([1, 2.2, 1])
with col_logo:
    try: st.image("logo.png", width=120)
    except: st.markdown("**LOGO**")
with col_title:
    st.markdown('<div style="border:1.5px solid #000; padding:10px; text-align:center; background:#fff; height:110px;"><div style="font-size:22px; font-weight:800;">KB VIÑULA TRADING</div><div style="font-size:14px;">FRANCOTIRADOR ORO/DXY</div></div>', unsafe_allow_html=True)
with col_reloj:
    components.html("""<div style="border:1.5px solid #000; padding:10px; text-align:center; background:#fff; height:110px; color:#000; font-family:monospace;"><div id="hora" style="font-size:18px; font-weight:800;"></div><div style="font-size:14px; font-weight:700;">MADRID</div><div id="fecha" style="font-size:12px;"></div></div><script>function tick(){const h=new Date().toLocaleTimeString("es-ES",{timeZone:"Europe/Madrid",hour:'2-digit',minute:'2-digit',second:'2-digit'});const f=new Date().toLocaleDateString("es-ES",{timeZone:"Europe/Madrid",weekday:'short',day:'2-digit',month:'short'});document.getElementById("hora").innerHTML=h;document.getElementById("fecha").innerHTML=f.toUpperCase();}setInterval(tick,1000);tick();</script>""", height=120)
c_cal, c_pilar = st.columns([1.6, 1])
with c_cal:
    st.markdown('<div class="borde"><b>Calendario Economico 3 estrellas</b></div>', unsafe_allow_html=True)
    components.iframe("https://sslecal2.investing.com?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=95&lang=12", height=380, scrolling=True)
with c_pilar:
    st.markdown('<div style="border:1.5px solid #000; padding:12px; background:#fff;"><b>Pilares de Fundamental (datos real time)</b><br><br><b>IPC:</b> 3.4% Agosto<br><b>NFP:</b> >200k DXY FUERTE / VENTA ORO<br><b>DXY:</b> 99.67<br><b>VIX:</b> 14.8<br><b>Tasa Fed:</b> 3.75%-4.00% (17 Sep)<br><b>Geopolitica hoy:</b> Tension Medio Oriente = Soporte ORO</div>', unsafe_allow_html=True)
c_xau, c_dxy = st.columns([2, 1])
with c_xau:
    st.markdown('<div class="borde"><b>grafico XAUUSD</b></div>', unsafe_allow_html=True)
    components.html("""<div id="tv_xau"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es","height":350,"container_id":"tv_xau"});</script>""", height=360)
with c_dxy:
    st.markdown('<div class="borde"><b>grafico DXY</b></div>', unsafe_allow_html=True)
    components.html("""<div id="tv_dxy"></div><script src="https://s3.tradingview.com/tv.js"></script><script>new TradingView.widget({"autosize":true,"symbol":"CAPITALCOM:DXY","interval":"60","timezone":"Europe/Madrid","theme":"light","style":"1","locale":"es","height":350,"container_id":"tv_dxy"});</script>""", height=360)
st.markdown('<div class="borde"><b>CheckList</b></div>', unsafe_allow_html=True)
a,b = st.columns(2)
with a:
    z1=st.checkbox("Zona de interes D1/S1/M1"); z2=st.checkbox("Rechazo Vela H4"); z3=st.checkbox("BOS H1")
with b:
    z4=st.checkbox("Retroceso FVG 15m"); z5=st.checkbox("BoS 5m"); z6=st.checkbox("Entrada")
st.markdown('<div class="borde"><b>Diario de trading</b></div>', unsafe_allow_html=True)
if "diario" not in st.session_state: st.session_state.diario=[]
with st.form("d"):
    f1,f2,f3,f4 = st.columns(4)
    with f1: ficha=st.text_input("Ficha"); inst=st.selectbox("Instrumento",["XAUUSD","DXY"])
    with f2: fund=st.selectbox("Fundamento",["NFP","IPC","VIX","FED","Geo"]); tec=st.text_input("Tecnico")
    with f3: ent=st.number_input("Entrada",0.0); sal=st.number_input("Salida",0.0); tp=st.number_input("TP",0.0); sl=st.number_input("SL",0.0)
    with f4: res=st.selectbox("Res",["TP","SL","BE"]); obs=st.text_input("Obs")
    if st.form_submit_button("Guardar"):
        st.session_state.diario.append({"Ficha":ficha,"Inst":inst,"Fund":fund,"Tec":tec,"Ent":ent,"Sal":sal,"TP":tp,"SL":sl,"Res":res,"Obs":obs})
if st.session_state.diario:
    df=pd.DataFrame(st.session_state.diario); st.dataframe(df, use_container_width=True)
