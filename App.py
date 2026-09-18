# PEGA ESTO EN APP.PY - V54 LIMPIO
import streamlit as st, pandas as pd
from datetime import datetime
import pytz, streamlit.components.v1 as components
st.set_page_config(layout="wide")
madrid=datetime.now(pytz.timezone('Europe/Madrid'))
st.title("KB VINULA TRADING")
st.write(madrid.strftime("%d/%m/%Y %H:%M")+" MADRID")
FILE="trading.xlsx"
def cargar():
 try:
  df=pd.read_excel(FILE)
  return df
 except:
  return pd.DataFrame({"Fecha":[datetime.now().strftime("%d/%m/%Y")],"Activo":["XAUUSD"],"Calendario economico":["IPC 3.4% / FED 4%"],"Nivel de interes":["3.75%-4.00%"],"Rechazo H4":["Si"],"BOS H1":["Si alcista"],"FVG 15m":["2650"],"FVG 5m":["Si"],"Tamano operacion":["0.01"],"TP":["2660"],"SL":["2645"]})
if "df" not in st.session_state:
 st.session_state.df=cargar()
edit=st.data_editor(st.session_state.df, num_rows="dynamic", use_container_width=True, height=400)
if st.button("💾 GUARDAR"):
 st.session_state.df=edit
 edit.to_excel(FILE, index=False)
 st.success("Guardado!")
csv=edit.to_csv(index=False).encode('utf-8')
st.download_button("📥 BACKUP",csv,"kb.csv","text/csv")
