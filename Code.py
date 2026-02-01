import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import streamlit as st

st.header('Gráfico interactivo de precios ajustados del último año de Apple (AAPL)')

# -----------------------------
# Descargar datos
# -----------------------------
end = datetime.now()
start = end - timedelta(days=365)

df_apple = yf.download(
    "AAPL",
    start=start,
    end=end,
    progress=False,
    auto_adjust=False
)

# Reset index
df_apple = df_apple.reset_index()

# 🔧 Aplanar columnas si vienen como MultiIndex
if isinstance(df_apple.columns, pd.MultiIndex):
    df_apple.columns = df_apple.columns.get_level_values(0)

# Selección segura de columnas
DF = df_apple[["Date", "Adj Close"]].copy()

# -----------------------------
# Gráfica interactiva
# -----------------------------
fig = px.line(
    DF,
    x="Date",
    y="Adj Close",
    title="Apple (AAPL) – Adjusted Close Price (Último año)",
    labels={
        "Date": "Fecha",
        "Adj Close": "Precio Ajustado (USD)"
    }
)

fig.update_layout(
    template="plotly_dark",
    hovermode="x unified",
    title_x=0.5
)

fig.update_traces(
    line=dict(width=3),
    hovertemplate="Fecha: %{x}<br>Precio: $%{y:.2f}<extra></extra>"
)

# 🔥 ESTA ES LA LÍNEA CORRECTA PARA STREAMLIT
st.plotly_chart(fig, use_container_width=True)