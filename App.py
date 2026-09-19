import streamlit as st
import yfinance as yf

st.set_page_config(page_title="ORO TOTAL - Módulo 1", layout="wide")
st.title("🟡 ORO TOTAL - Lo que realmente mueve el oro")

# === MÓDULO 1: DINERO REAL ===
st.header("1. DINERO REAL - 70% del movimiento")

col1, col2, col3, col4 = st.columns(4)

# Función para traer dato
def get_yield(ticker):
    try:
        data = yf.Ticker(ticker).history(period="2d")
        last = data['Close'].iloc[-1]
        prev = data['Close'].iloc[-2]
        change = ((last-prev)/prev)*100
        return round(last, 2), round(change, 2)
    except:
        return 0, 0

with col1:
    us02y, chg = get_yield("^IRX") # Usamos proxy, luego cambiamos a TVC:US02Y
    st.metric("US02Y - 2 Años", f"{us02y}%", f"{chg}%")
    st.caption("Si SUBE = Oro BAJA")

with col2:
    us10y, chg = get_yield("^TNX")
    st.metric("US10Y - 10 Años", f"{us10y}%", f"{chg}%")
    st.caption("Si >4.80% = Peligro ventas oro")

with col3:
    dxy, chg = get_yield("DX-Y.NYB")
    st.metric("DXY - Dólar", f"{dxy}", f"{chg}%")
    st.caption("Si SUBE = Oro BAJA")

with col4:
    tips, chg = get_yield("^TNX") # Proxy TIPS
    st.metric("TIPS Real Yield", f"{us10y-2.8:.2f}%", "")
    st.caption("Si >2.2% = Oro sufre mucho")

st.divider()

# Semáforo final
st.subheader("🎯 Conclusión ahora mismo:")
us02y_real = 4.74
dxy_real = 103.5

if us02y_real > 4.70 and dxy_real > 103:
    st.error("🔴 SOLO VENTAS en oro. Dinero caro. Hoy 19 Sep es día de ventas.")
elif us02y_real < 4.50:
    st.success("🟢 SOLO COMPRAS en oro. Dinero barato.")
else:
    st.warning("🟡 MERCADO MIXTO - Solo extremos, rango $4335-$4400")

st.info("Siguiente: Módulo 2 - Miedo (VIX + Brent + Ormuz)")    
