import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="KB VINULA TRADING", layout="wide", page_icon="👑")

st.markdown("""
<style>
.stApp { background: #FFFFFF!important; }
h1,h2,h3,h4,h5,h6,p,span,div,label { color: #000000!important; }
.card { background: #F5F5F5; border: 1px solid #CCCCCC; border-radius: 12px; padding: 12px; }
</style>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns([1,2,1])
with c1:
    try:
        st.image("logo.png", width=130)
    except:
        st.markdown("## KB VINULA")
with c2:
    st.markdown("<h1 style='text-align:center; color:#000!important; margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
with c3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>{madrid.strftime('%H:%M:%S')}</b><br>MADRID</div>", unsafe_allow_html=True)

st.divider()

col_cal, col_pilar = st.columns([1.15, 1])

with col_cal:
    st.markdown("#### 📅 CALENDARIO - SOLO 3 ESTRELLAS")
    with st.container(border=True):
        components.html("""<iframe src="https://sslecal2.forexprostools.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=55&lang=12&importance=3" width="100%" height="650" frameborder="0" allowtransparency="true"></iframe>""", height=670)

with col_pilar:
    st.markdown("#### 🏛️ PILARES FUNDAMENTALES")
    with st.container(border=True):
        st.markdown("*1. IPC USA*")
        ipc = st.slider("ipc", 0.0, 8.0, 3.2, 0.1, label_visibility="collapsed")
        if ipc > 4:
            st.error(f"IPC {ipc}% ALTO")
        elif ipc < 2.5:
            st.success(f"IPC {ipc}% BAJO")
        else:
            st.warning(f"IPC {ipc}% NEUTRO")
        st.markdown("*2. NFP*")
        st.selectbox("nfp", ["Fuerte +200k - Oro baja","Medio","Débil <100k - Oro sube"], label_visibility="collapsed")
        st.markdown("*3. TASAS FED*")
        st.selectbox("fed", ["Suben - Oro baja","Mantienen","Bajan - Oro sube"], label_visibility="collapsed")
        st.markdown("*4. GEOPOLITICA*")
        st.selectbox("geo", ["Calma","Tensión media","Guerra - Oro sube"], label_visibility="collapsed")
        st.markdown("*5. SESION*")
        st.info("Killzone 08-11h y 14-17h")

st.divider()
st.markdown("#### 📺 TV NOTICIAS + DXY")

components.html("""<div style="background:#000; border:2px solid #FFD60A; border-radius:8px; padding:10px; color:#FFD60A; font-family:monospace; font-size:14px; overflow:hidden"><marquee scrollamount="7">🔴 EN VIVO | ORO XAUUSD | DXY | KILLZONE 14-17h | SOLO 3 ESTRELLAS |</marquee></div>""", height=60)

col_tv, col_dxy = st.columns([1.2, 1])

with col_tv:
    st.markdown("*TV ECONOMIA 24H*")
    components.html("""
<div class="tradingview-widget-container">
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
{
"feedMode": "market",
"market": "forex",
"colorTheme": "light",
"isTransparent": false,
"displayMode": "regular",
"width": "100%",
"height": 550,
"locale": "es"
}
</script>
</div>
""", height=570)

with col_dxy:
    st.markdown("*📉 DXY - DOLAR INDEX*")
    components.html("""
<div id="dxy_final" style="height:450px"></div>
<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
<script type="text/javascript">
new TradingView.widget({
"container_id": "dxy_final",
"width": "100%",
"height": 450,
"symbol": "TVC:DXY",
"interval": "60",
"timezone": "Europe/Madrid",
"theme": "light",
"style": "1",
"locale": "es",
"allow_symbol_change": true
});
</script>
""", height=470)

st.divider()
st.markdown("#### 📈 XAUUSD - GRAFICO PRINCIPAL")
components.html("""
<div id="xau_final" style="height:550px"></div>
<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
<script type="text/javascript">
new TradingView.widget({
"container_id": "xau_final",
"width": "100%",
"height": 550,
"symbol": "OANDA:XAUUSD",
"interval": "15",
"timezone": "Europe/Madrid",
"theme": "light",
"style": "1",
"locale": "es",
"allow_symbol_change": true
});
</script>
""", height=570)

st.divider()
st.markdown("### 🎯 CHECKLIST 7/7")
with st.container(border=True):
    chk1 = st.checkbox("1. CALENDARIO 3* revisado - No noticia roja en 30min")
    chk2 = st.checkbox("2. DXY analizado - Oro inverso")
    chk3 = st.checkbox("3. 5 PILARES alineados - 4 de 5 a favor")
    chk4 = st.checkbox("4. KILLZONE activa - 08-11h o 14-17h")
    chk5 = st.checkbox("5. Estructura Oro - Tendencia clara M15")
    chk6 = st.checkbox("6. Gestion riesgo - SL < 2%")
    chk7 = st.checkbox("7. Psicologia OK - Sin revenge")
    total = sum([chk1,chk2,chk3,chk4,chk5,chk6,chk7])
    st.progress(total/7, text=f"{total}/7")
    if total == 7:
        st.success("EJECUTA ORDEN")
        st.balloons()
    elif total >= 5:
        st.warning(f"{total}/7 - Casi listo")
    else:
        st.error(f"{total}/7 - ESPERA")

st.divider()
st.markdown("### 📂 DIARIO TRADING")
FILE="trading.xlsx"
def cargar():
    try:
        tmp=pd.read_excel(FILE, header=None)
        f=0
        for i in range(len(tmp)):
            if "Fecha" in str(tmp.iloc[i].values):
                f=i
                break
        df=pd.read_excel(FILE, header=f)
        df=df[[c for c in df.columns if "Unnamed" not in str(c)]].dropna(how='all').fillna("")
        if "Fecha" in df.columns:
            df["Fecha"]=pd.to_datetime(df["Fecha"], errors='coerce').dt.strftime("%d/%m/%Y").replace("NaT","").fillna("")
        return df.replace("0.0","")
    except:
        return pd.DataFrame({"Fecha":[datetime.now().strftime("%d/%m/%Y")],"Activo":["MGC"],"Resultado":[""]})

if "df" not in st.session_state:
    st.session_state.df=cargar()
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=350, key="ed_v48")
st.session_state.df=edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("Guardado!")
