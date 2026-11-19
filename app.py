import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl

st.title("População livre e população escravizada de 1872")
st.header("mulheres livres, homens livres, mulheres escravizadas, homens escravizados")

df = pd.read_excel("censo_1872.xlsx")
df = df.drop_duplicates()

df.columns = [
    "homens_livres",
    "mulheres_livres",
    "total_livres",
    "homens_escravizados",
    "mulheres_escravizadas",
    "total_escravizados",
    "total"
]

col_homens_livres = "homens_livres"
col_homens_escravizados = "homens_escravizados"
col_mulheres_livres = "mulheres_livres"
col_mulheres_escravizados = "mulheres_escravizadas"

df["Porcentagem Homens Livres (%)"] = (df[col_homens_livres] / (df[col_homens_livres] + df[col_homens_escravizados])) * 100
df["Porcentagem Mulheres Livres (%)"] = (df[col_mulheres_livres] / (df[col_mulheres_livres] + df[col_mulheres_escravizados])) * 100
df["Porcentagem Homens Escravizados (%)"] = (df[col_homens_escravizados] / (df[col_homens_escravizados] + df[col_homens_livres])) * 100
df["Porcentagem Mulheres Escravizados (%)"] = (df[col_mulheres_escravizados] / (df[col_mulheres_escravizados] + df[col_mulheres_livres])) * 100


# Exibindo os KPIs gerais
st.markdown("## 📈 Indicadores-Chave de Desempenho (KPIs)")
st.metric(label="Porcentagem Homens Livres (%)", value=f"{df:.2f}%")
st.metric(label="Porcentagem Mulheres Livres (%)", value=f"{df:,}".replace(",", "."))
st.metric(label="População Total (2022)", value=f"{df:,}".replace(",", "."))

st.dataframe(df)