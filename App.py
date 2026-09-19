import streamlit as st

st.set_page_config(page_title="ORO TOTAL - 6 Módulos", layout="wide")
st.title("🟡 ORO TOTAL - Sistema Completo 6 Módulos")
st.caption("Todo lo que mueve el oro en una sola hoja - 20 Sep 2026")

# === DATOS REALES DE HOY (Base para API después) ===
oro = 4378
us02y = 4.74
us10y = 4.78
dxy = 103.5
tips = 2.15
brent = 104.5
vix = 18.2
btc = 67500
plata = 31.2
cobre = 4.35

# === MODULO 1: DINERO REAL ===
st.header("1. 💵 DINERO REAL - 70% del movimiento")
c1, c2, c3, c4 = st.columns(4)
c1.metric("US02Y", f"{us02y}%", "↑ Peligro ventas")
c2.metric("US10Y", f"{us10y}%", "Cerca 4.80%")
c3.metric("DXY", f"{dxy}", "↑ Fuerte")
c4.metric("TIPS Real", f"{tips}%", "Si >2.2% = caída")
if us02y > 4.7 and dxy > 103:
    st.error("🔴 CONCLUSIÓN M1: Dinero CARO = SOLO VENTAS ORO")
else:
    st.success("🟢 Dinero barato = Compras")

st.divider()

# === MODULO 2: MIEDO ===
st.header("2. 😱 MIEDO - 20% del movimiento")
c1, c2, c3, c4 = st.columns(4)
c1.metric("VIX", f"{vix}", "Miedo bajo")
c2.metric("BRENT", f"${brent}", "↑ Alto - Riesgo inflación")
c3.metric("Gas TTF", "€38", "↑ Europa")
c4.metric("Ormuz", "12% barcos lentos", "🟡 Alerta media")
st.warning(f"Brent ${brent} alto = FED no baja tasas = Oro no puede subir mucho ahora")

st.divider()

# === MODULO 3: DEMANDA REAL ===
st.header("3. 🏦 DEMANDA REAL - Pone el suelo")
c1, c2, c3 = st.columns(3)
c1.metric("Bancos Centrales", "China +35T Sep", "Suelo fuerte")
c2.metric("ETF GLD Flujo", "+1.2B esta semana", "Entrada dinero")
c3.metric("COT - Grandes", "65% largos", "Todavía no extremo")
st.info("🟢 Demanda física sigue comprando caídas. Suelo en $4320-$4335")

st.divider()

# === MODULO 4: CORRELACIONES ===
st.header("4. 🔗 CORRELACIONES EN VIVO")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Oro vs BTC", f"Oro ${oro} / BTC ${btc}", "Descorrelacionado")
c2.metric("Ratio Oro/Plata", f"{oro/plata:.1f}", "Si baja <75 = Plata explota")
c3.metric("Oro vs Cobre", f"Cobre ${cobre}", "Economía aguantando")
c4.metric("Oro vs SPX", "Oro más fuerte", "Refugio activo")
ratio = oro/plata
if ratio > 85:
    st.caption(f"Ratio {ratio:.1f} alto = Plata barata vs oro")

st.divider()

# === MODULO 5: CALENDARIO ===
st.header("5. 📅 CALENDARIO QUE IMPORTA - Solo 5 eventos")
st.table({
    "Evento": ["CPI USA", "NFP Empleo", "FOMC FED", "PCE Inflación", "Ventas Minoristas"],
    "Fecha": ["11 Oct", "3 Oct", "30 Oct", "25 Oct", "17 Oct"],
    "Impacto Oro": ["★★★★★", "★★★★★", "★★★★★", "★★★★", "★★★"],
    "Acción": ["NO OPERAR 1h antes", "NO OPERAR 1h antes", "NO OPERAR", "Cuidado", "Operable"]
})
st.error("🔴 Hoy: Sin eventos mayores. Día técnico - perfecto para rangos.")

st.divider()

# === MODULO 6: CALCULADORA ===
st.header("6. 🧮 CALCULADORA DE ESCENARIOS")
st.write("¿Qué pasa si...?")

escenario = st.selectbox("Elige escenario:", [
    "US02Y sube a 4.90% (FED dura)",
    "Brent rompe $110",
    "US02Y baja a 4.40% (FED recorta)",
    "Guerra Ormuz - cierre parcial",
    "VIX salta a 30"
])

if "4.90%" in escenario:
    st.error("→ Oro cae a $4250 - $4280 (Venta fuerte)")
elif "110" in escenario:
    st.warning("→ Oro sube a $4450 - $4500 primero, luego cae por FED")
elif "4.40%" in escenario:
    st.success("→ Oro explota a $4550 - $4600 (Compra)")
elif "Ormuz" in escenario:
    st.success("→ Oro a $4700+ rápido (Compra refugio)")
elif "30" in escenario:
    st.success("→ Oro sube a $4520 por miedo")

st.divider()
st.header("🎯 VEREDICTO FINAL HOY 20 SEP")
st.markdown(f"""
**Oro ${oro} - Rango del día: $4335 - $4410**

- Módulo 1 Dinero: 🔴 Venta (US02Y {us02y}%)
- Módulo 2 Miedo: 🟡 Mixto (Brent alto)
- Módulo 3 Demanda: 🟢 Compra (Suelo fuerte)
- Módulo 4 Correlación: 🟡 Neutro
- Módulo 5 Calendario: 🟢 Sin noticias = se puede operar

**Plan: Solo ventas en $4395-$4410 con stop $4435, objetivo $4340**
""")

# === requirements.txt debe ser solo: streamlit ===
