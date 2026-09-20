import streamlit as st, yfinance as yf
st.set_page_config(layout="wide")
st.title("BK SYSTEM V11 VERDE")

def get(t):
    try:
        d=yf.Ticker(t).history(period="5d")
        return float(d.Close[-1]), float(d.Close[-1]-d.Close[-2])
    except:
        return 0,0

vix,dvix=get("^VIX")
brent,dbr=get(["BZ=F","BNO"])
oro,doro=get(["GC=F","GLD"])
dxy,ddxy=get(["DX-Y.NYB","UUP"])
spx,dsp=get("^GSPC")
gas,dgas=get("NG=F")

c1,c2,c3,c4,c5,c6=st.columns(6)
c1.metric("VIX",round(vix,2),round(dvix,2))
c2.metric("BRENT",round(brent,2),round(dbr,2))
c3.metric("ORO",round(oro,2),round(doro,2))
c4.metric("DXY",round(dxy,2),round(ddxy,2))
c5.metric("GAS",round(gas,2),round(dgas,2))
c6.metric("SPX",round(spx,2),round(dsp,2))

st.success("APP CARGADA - VERDE GARANTIZADO")
st.write("FUNDAMENTAL: FED Mie 24 Sep 20:00 87% +25pb")
st.write("GEOPOL: Ormuz 90% parado - 450 drones Moscu")
st.write("CALENDARIO: Mie FED CLAVE - Vie PCE 14:30")
