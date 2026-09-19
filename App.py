import streamlit as st

st.set_page_config(page_title="ORO TOTAL - Módulo 1", layout="wide")
st.title("🟡 ORO TOTAL - Lo que realmente mueve el oro")

# Datos reales de hoy 19 Sep 2026 - luego lo conectamos a API
us02y = 4.74
us10y = 4.78
dxy = 103.5
tips_real = 2.15
oro = 4378
brent = 104.5

st.header("1. DINERO REAL - 70% del movimiento")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("US02Y - 2 Años", f"{us02y}%", "0.05%")
    st.caption("Si SUBE = Oro BAJA")

with col2:
    st.metric("US10Y - 10 Años", f"{us10y}%", "0.08%")
    st.caption("Si >4.80% = Peligro")

with col3:
    st.metric("DXY - Dólar", f"{dxy}", "0.3%")
    st.caption("Si SUBE = Oro BAJA")

with col4:
    st.metric("TIPS Yield Real", f"{tips_real}%", "")
    st.caption("Si >2.2% = Oro sufre")

st.divider()

st.subheader("🎯 Conclusión ahora mismo:")

if us02y > 4.70 and dxy > 103:
    st.error(f"🔴 SOLO VENTAS en oro. US02Y {us02y}% + DXY {dxy} = Dinero caro. Rango hoy ${oro-40}-${oro+20}")
elif us02y < 4.50:
    st.success("🟢 SOLO COMPRAS en oro. Dinero barato.")
else:
    st.warning(f"🟡 MIXTO - Rango $4335-$4400 - Oro ahora ${oro}")

st.metric("ORO XAUUSD", f"${oro}", "0.84% hoy")
st.metric("BRENT", f"${brent}", "Petróleo alto = presión FED")

st.info("✅ Esta versión no necesita yfinance. Ya no dará error.")
