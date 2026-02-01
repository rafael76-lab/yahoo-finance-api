import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import streamlit as st
st.markdown(
    "<h2 style='color:#00eaff; text-align:center; margin-top:0;'>Apple (AAPL) – Precio Ajustado</h2>",
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        body {
            background-color: #000000;
        }
        .stApp {
            background-color: #000000;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #00eaff !important;
        }
    </style>
""", unsafe_allow_html=True)
end = datetime.now()
start = end - timedelta(days=365)

df_apple = yf.download(
    "AAPL",
    start=start,
    end=end,
    progress=False,
    auto_adjust=False
)

df_apple = df_apple.reset_index()

if isinstance(df_apple.columns, pd.MultiIndex):
    df_apple.columns = df_apple.columns.get_level_values(0)

DF = df_apple[["Date", "Adj Close"]].copy()
fig = px.line(
    DF,
    x="Date",
    y="Adj Close",
    title="Apple (AAPL) – Precio Ajustado",
    labels={
        "Date": "Fecha",
        "Adj Close": "Precio Ajustado"
    }
)

fig.update_layout(
    template="plotly_dark",
    hovermode="x unified",
    title_x=0.5,
    plot_bgcolor"#000000",
    paper_bgcolor"#000000",
    font=dict(color"#00eaff", size=14),
    title_font=dict(color"#00eaff", size=22),
    xaxis=dict(
        gridcolor"#222222",
        zerolinecolor"#333333"
    ),
    yaxis=dict(
        gridcolor"#222222",
        zerolinecolor"#333333"
    )
)

fig.update_traces(
    line=dict(width=4, color"#00eaff"),
    hovertemplate="Fecha: %{x}<br>Precio: $%{y:.2f}<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)