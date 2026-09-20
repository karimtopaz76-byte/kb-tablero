import streamlit as st, yfinance as yf, pandas as pd, os
from datetime import datetime
import pytz

st.set_page_config(page_title="BK TRADING SYSTEM", layout="wide")

# --- PERSISTENCIA DIARIO ---
FILE = "/tmp/diario_bk.csv"
if os.path.exists(FILE):
    df_init = pd.read_csv(FILE)
else:
    df_init = pd.DataFrame(columns=["Fecha","Instrumento","Lot size","Precio entrada","Precio salida","TP","SL"])

if "diario" not in st.session_state:
    st.session_state.diario = df_init

st.markdown("<style>.card{background:#fff;border:1px solid #e5e7eb;padding:14px;border-radius:8px;margin-bottom:10px}.card-title{font-weight:800;font-size:13px;margin-bottom:8px}</style>", unsafe_allow_html=True)

st.markdown("## BK SYSTEM — V7 CUADERNO REAL + GUARDADO")

def get_price(ticker):
    try:
        h = yf.Ticker(ticker).history(period="2d")
        return h.Close.iloc[-1], h.Close.iloc[-2]
    except:
        return 0,0

# 1 y 2
col1,col2 = st.columns([1,1])
with col1:
    st.markdown('<div class="card" style="border-left:4px solid #ff3b30"><div class="card-title">1. ANALISIS FUNDAMENTAL</div>Fed: 90% subida 25pb miercoles<br>CPI 3.1% | NFP viernes<br>VIX 17.5</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card" style="border-left:4px solid #000"><div class="card-title">2. SITUACION GEOPOLITICA ACTUAL</div>USA-Iran Ormuz $99.56<br>Rusia-Ucrania 450 drones Moscú<br>Duma vota hoy</div>', unsafe_allow_html=True)

# DATOS REALES
st.markdown('<div class="card"><div class="card-title">3. DATOS A TIEMPO REAL</div></div>', unsafe_allow_html=True)
c1,c2,c3,c4,c5,c6 = st.columns(6)
tickers = {"VIX":"^VIX","Brent":"BZ=F","Nat Gas":"NG=F","TIPS":"^TNX","US02Y":"^IRX","DXY":"DX-Y.NYB"}
for (name,tick),col in zip(tickers.items(), [c1,c2,c3,c4,c5,c6]):
    p,pp = get_price(tick)
    col.metric(name, f"{p:.2f}", f"{p-pp:+.2f}")

# CALENDARIO
st.markdown('<div class="card" style="border-left:4px solid #ffcc00"><div class="card-title">4. CALENDARIO 3 ESTRELLAS USA</div>Mie 24 Sep 20:00 FED ⭐⭐⭐<br>Jue 25 Sep 14:30 PIB USA ⭐⭐⭐<br>Vie 26 Sep 14:30 NFP + PCE ⭐⭐⭐</div>', unsafe_allow_html=True)

# ANALISIS TECNICO
st.markdown('<div class="card"><div class="card-title">5. ANALISIS TECNICO</div></div>', unsafe_allow_html=True)
cc1,cc2 = st.columns(2)
with cc1:
    st.markdown("**CHECKLIST XAUUSD**")
    x = [st.checkbox(f"{t}", key=f"x{i}") for i,t in enumerate(["Nivel D1,S1,N1","Rechazo H4","BOS H1","Retraso FVG 15m","BOS 5m"])]
    if all(x): st.success("✅ XAUUSD READY")
    else: st.warning(f"{sum(x)}/5")
with cc2:
    st.markdown("**CHECKLIST US02Y**")
    u = [st.checkbox(f"{t} ", key=f"u{i}") for i,t in enumerate(["Nivel D1,S1,N1","Rechazo H4","BOS H1","Retraso FVG 15m","BOS 5m"])]
    if all(u): st.success("✅ US02Y READY")
    else: st.warning(f"{sum(u)}/5")

# DIARIO CON GUARDADO
st.markdown('<div class="card" style="border-left:4px solid #00a86b"><div class="card-title">6. DIARIO TRADING — AUTOGUARDADO</div></div>', unsafe_allow_html=True)
edited = st.data_editor(st.session_state.diario, num_rows="dynamic", use_container_width=True, key="editor")
st.session_state.diario = edited
edited.to_csv(FILE, index=False)

st.download_button("📥 Descargar Excel Diario", edited.to_csv(index=False), "diario_bk.csv", "text/csv")

st.caption(f"Guardado automático activo — {datetime.now(pytz.timezone('Europe/Madrid')).strftime('%H:%M:%S')}")
streamlit as st, yfinance as yf, pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="BK TRADING SYSTEM", layout="wide")
st.markdown("<style>.card{background:#fff;border:1px solid #e5e7eb;padding:14px;border-radius:8px;margin-bottom:10px}.card-title{font-weight:800;font-size:13px;margin-bottom:8px}</style>", unsafe_allow_html=True)

st.markdown("## BK SYSTEM — CUADERNO REAL")

# --- FUNCION DATOS REALES ---
def get_price(ticker):
    try:
        h = yf.Ticker(ticker).history(period="2d")
        return h.Close.iloc[-1], h.Close.iloc[-2]
    except:
        return 0,0

# 1 ANALISIS FUNDAMENTAL
col1,col2 = st.columns([1,1])
with col1:
    st.markdown('<div class="card" style="border-left:4px solid #ff3b30"><div class="card-title">ANALISIS FUNDAMENTAL</div>Fed: 90% subida 25pb miercoles<br>CPI: 3.1% > objetivo 2%<br>NFP: viernes clave<br>VIX: 17.5 riesgo</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card" style="border-left:4px solid #000"><div class="card-title">SITUACION GEOPOLITICA ACTUAL — HOY</div> - Conflicto USA-Iran: ataque en Ormuz, refineria Kapotnia en llamas<br>- Estrecho Ormuz: Brent $99.56, riesgo cierre<br>- Rusia vs Ucrania: 450 drones sobre Moscú, Duma vota<br>- ONU: 130 lideres martes, sin foro Iran</div>', unsafe_allow_html=True)

# 2 DATOS TIEMPO REAL
st.markdown('<div class="card"><div class="card-title">DATOS A TIEMPO REAL</div></div>', unsafe_allow_html=True)
c1,c2,c3,c4,c5,c6 = st.columns(6)
tickers = {"VIX":"^VIX","Brent":"BZ=F","Nat Gas":"NG=F","TIPS":"^TNX","US02Y":"^IRX","DXY":"DX-Y.NYB"}
cols=[c1,c2,c3,c4,c5,c6]
for (name,tick),col in zip(tickers.items(), cols):
    p,pp = get_price(tick)
    ch = p-pp
    col.metric(name, f"{p:.2f}", f"{ch:+.2f}")

# 3 CALENDARIO
st.markdown('<div class="card" style="border-left:4px solid #ffcc00"><div class="card-title">CALENDARIO ECONOMICO 3 ESTRELLAS USA</div> - Miercoles 24 Sep 14:00: Decision tipos FED ⭐⭐⭐<br>- Jueves 25 Sep 08:30: PIB USA Q2 ⭐⭐⭐<br>- Viernes 26 Sep 08:30: NFP + PCE ⭐⭐⭐<br>- Viernes 26 Sep: Vencimiento opciones oro $4.5B</div>', unsafe_allow_html=True)

# 4 ANALISIS TECNICO - TU CHECKLIST
st.markdown('<div class="card"><div class="card-title">ANALISIS TECNICO</div></div>', unsafe_allow_html=True)
cc1,cc2 = st.columns(2)
with cc1:
    st.markdown("**CHECKLIST XAUUSD**")
    x1=st.checkbox("Nivel de interes D1,S1,N1", key="x1")
    x2=st.checkbox("Rechazo H4", key="x2")
    x3=st.checkbox("BOS H1", key="x3")
    x4=st.checkbox("Retraso a FVG 15m", key="x4")
    x5=st.checkbox("BOS 5m", key="x5")
    if all([x1,x2,x3,x4,x5]): st.success("✅ XAUUSD READY — EJECUTAR")
    else: st.warning(f"{sum([x1,x2,x3,x4,x5])}/5")
with cc2:
    st.markdown("**CHECKLIST US02Y**")
    u1=st.checkbox("Nivel de interes D1,S1,N1", key="u1")
    u2=st.checkbox("Rechazo H4 ", key="u2")
    u3=st.checkbox("BOS H1 ", key="u3")
    u4=st.checkbox("Retraso a FVG 15m ", key="u4")
    u5=st.checkbox("BOS 5m ", key="u5")
    if all([u1,u2,u3,u4,u5]): st.success("✅ US02Y READY")
    else: st.warning(f"{sum([u1,u2,u3,u4,u5])}/5")

# 5 DIARIO TRADING
st.markdown('<div class="card" style="border-left:4px solid #00a86b"><div class="card-title">DIARIO TRADING</div></div>', unsafe_allow_html=True)
if "diario" not in st.session_state:
    st.session_state.diario = pd.DataFrame(columns=["Fecha","Instrumento","Lot size","Precio entrada","Precio salida","TP","SL"])

edited = st.data_editor(st.session_state.diario, num_rows="dynamic", use_container_width=True)
st.session_state.diario = edited

st.caption(f"Actualizado: {datetime.now(pytz.timezone('Europe/Madrid')).strftime('%H:%M:%S')} — El Ejido")
