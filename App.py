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
.live-box { background: #000000; color: #FFD60A!important; border-radius: 10px; padding: 12px; border: 2px solid #FFD60A; }
.live-box b,.live-box span,.live-box div { color: #FFD60A!important; }
</style>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns([1,2,1])
with c1:
    try:
        st.image("logo.png", width=130)
    except:
        st.markdown("## 👑 KB VINULA")
with c2:
    st.markdown("<h1 style='text-align:center; color:#000!important; margin:0'>KB VINULA TRADING</h1>", unsafe_allow_html=True)
with c3:
    madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    st.markdown(f"<div class='card' style='text-align:center'><b>{madrid.strftime('%d/%m/%Y %H:%M:%S')}</b><br>MADRID</div>", unsafe_allow_html=True)

st.divider()

col_cal, col_pilar = st.columns([1.15, 1])

with col_cal:
    st.markdown("#### 📅 CALENDARIO - SOLO 3 ESTRELLAS")
    with st.container(border=True):
        components.html("""<iframe src="https://sslecal2.forexprostools.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=25,32,6,37,72,22,17,39,14,10,35,43,56,36,110,11,26,12,4,5&calType=week&timeZone=55&lang=12&importance=3" width="100%" height="650" frameborder="0" allowtransparency="true"></iframe>""", height=670)

with col_pilar:
    st.markdown("#### 🏛️ PILARES FUNDAMENTALES - DATOS DE HOY")

    with st.container(border=True):
        st.markdown('<div class="live-box"><b>🔴 PILAR 1 - IPC USA EN VIVO - HOY 18/09/2026</b><br><br>Ultimo dato: <b>3.4% Agosto</b> (Igual que Julio)<br>Subyacente: <b>2.4%</b> (bajó de 2.5%)<br>Proximo IPC: <b>11 Octubre 2026 - 14:30 Madrid</b><br>FED: 15-16 Sept sube tasas 85% prob.<br><br>👉 Si IPC >4% = DXY SUBE / ORO BAJA<br>👉 Si IPC <2.5% = DXY BAJA / ORO SUBE</div>', unsafe_allow_html=True)

        ipc = st.slider("Ajusta tu expectativa IPC hoy", 0.0, 8.0, 3.4, 0.1)
        if ipc >= 4.0:
            st.error(f"IPC {ipc}% ALTO = VENTA ORO")
        elif ipc <= 2.5:
            st.success(f"IPC {ipc}% BAJO = COMPRA ORO")
        else:
            st.warning(f"IPC {ipc}% NEUTRO = ESPERA DATO")

        st.divider()
        st.markdown("**2. NFP**")
        st.selectbox("nfp", ["Fuerte +200k - Oro baja","Medio","Débil <100k - Oro sube"], label_visibility="collapsed")
        st.markdown("**3. TASAS FED**")
        st.selectbox("fed", ["Suben - Oro baja","Mantienen","Bajan - Oro sube"], label_visibility="collapsed", index=0)
        st.markdown("**4. GEOPOLITICA**")
        st.selectbox("geo", ["Calma","Tensión media","Guerra - Oro sube"], label_visibility="collapsed")
        st.markdown("**5. SESION**")
        st.info("Killzone 08-11h y 14-17h Madrid")

st.divider()
st.markdown("#### 📺 NOTICIAS + DXY")

components.html("""<div style="background:#000; border:2px solid #FFD60A; border-radius:8px; padding:10px; color:#FFD60A; font-family:monospace; overflow:hidden"><marquee scrollamount="7">🔴 IPC USA 3.4% | PROXIMO 11 OCT 14:30 | FED 15-16 SEP | KILLZONE 14-17h | DXY INVERSO ORO |</marquee></div>""", height=60)

col_tv, col_dxy = st.columns([1, 1])

with col_tv:
    st.markdown("**TV NOTICIAS - ABRE FUERA (no rompe app)**")
    with st.container(border=True):
        st.link_button("📈 FOREX NEWS - INVESTING", "https://www.investing.com/news/forex-news", use_container_width=True)
        st.link_button("📉 BLOOMBERG LIVE", "https://www.bloomberg.com/live", use_container_width=True)
        st.link_button("📊 CALENDARIO IPC USA DETALLE", "https://www.investing.com/economic-calendar/cpi-733", use_container_width=True)

with col_dxy:
    st.markdown("**📉 DXY - DOLAR INDEX (inverso ORO)**")
    components.html("""
<div id="dxy_v51" style="height:450px"></div>
<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
<script type="text/javascript">
new TradingView.widget({
"container_id": "dxy_v51",
"width": "100%",
"height": 450,
"symbol": "TVC:DXY",
"interval": "60",
"timezone": "Europe/Madrid",
"theme": "light",
"style": "1",
"locale": "es"
});
</script>
""", height=470)

st.divider()
st.markdown("#### 📈 XAUUSD - GRAFICO PRINCIPAL")
components.html("""
<div id="xau_v51" style="height:550px"></div>
<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
<script type="text/javascript">
new TradingView.widget({
"container_id": "xau_v51",
"width": "100%",
"height": 550,
"symbol": "OANDA:XAUUSD",
"interval": "15",
"timezone": "Europe/Madrid",
"theme": "light",
"style": "1",
"locale": "es"
});
</script>
""", height=570)

st.divider()
st.markdown("### 🎯 CHECKLIST 7/7")
with st.container(border=True):
    chk1 = st.checkbox("1. IPC 3.4% revisado hoy")
    chk2 = st.checkbox("2. DXY analizado")
    chk3 = st.checkbox("3. 5 PILARES alineados")
    chk4 = st.checkbox("4. KILLZONE activa")
    chk5 = st.checkbox("5. Estructura M15")
    chk6 = st.checkbox("6. Riesgo <2%")
    chk7 = st.checkbox("7. Psicologia OK")
    total = sum([chk1,chk2,chk3,chk4,chk5,chk6,chk7])
    st.progress(total/7, text=f"{total}/7")
    if total == 7:
        st.success("EJECUTA ORDEN")
        st.balloons()

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
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=350, key="ed_v51")
st.session_state.df=edit
if st.button("💾 GUARDAR TODO", type="primary", use_container_width=True):
    edit.to_excel(FILE, index=False)
    st.success("Guardado!")
