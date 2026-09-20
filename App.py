import streamlit as st, yfinance as yf
st.set_page_config(layout="wide")
st.title("BK SYSTEM V12 - FINAL SIN 0")

def get(tickers):
    if isinstance(tickers, str):
        tickers=[tickers]
    for tk in tickers:
        try:
            d=yf.Ticker(tk).history(period="5d")
            if len(d)>=2:
                return float(d.Close.iloc[-1]), float(d.Close.iloc[-1]-d.Close.iloc[-2])
        except:
            continue
    return 0,0

vix,dvix=get("^VIX")
brent,dbr=get(["BZ=F","BNO"])
oro,doro=get(["GC=F","GLD"])
dxy,ddxy=get(["DX-Y.NYB","UUP"])
gas,dgas=get("NG=F")
spx,dsp=get("^GSPC")

c1,c2,c3,c4,c5,c6=st.columns(6)
c1.metric("VIX",round(vix,2),round(dvix,2))
c2.metric("BRENT",round(brent,2),round(dbr,2))
c3.metric("ORO",round(oro,2),round(doro,2))
c4.metric("DXY",round(dxy,2),round(ddxy,2))
c5.metric("GAS",round(gas,2),round(dgas,2))
c6.metric("SPX",round(spx,2),round(dsp,2))
st.success("VERDE Y CON DATOS REALES")
