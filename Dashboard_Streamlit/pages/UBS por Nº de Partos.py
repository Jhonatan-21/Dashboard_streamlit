import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path

st.title("UBS por Nº de Partos")

cwd = os.getcwd()
bd_partos_path = Path(cwd, "Dashboard_Streamlit", "BD_PARTOS_original.xlsx")

df = pd.read_excel(bd_partos_path)

df_ubs = df.groupby('UBS')['PARTOS'].sum().reset_index()
fig = px.treemap(
    df_ubs, 
    path=['UBS'],      # A categoria (quem são os blocos)
    values='PARTOS',   # O tamanho (baseado no nº de partos)
    color='PARTOS',    # A cor muda conforme o volume
    color_continuous_scale='Reds' # Escala de cores igual à sua foto
)
st.plotly_chart(fig)

#CONECTANDO AO SIDEBAR (FILTROS GLOBAIS)

# Carrega os dados
df = pd.read_excel(bd_partos_path)
df['DT_INTERNACAO'] = pd.to_datetime(df['DT_INTERNACAO'])

# Aplica os filtros do session_state, se existirem
if 'filtros' in st.session_state:
    f = st.session_state['filtros']
    
    # Filtro de Data
    if len(f['periodo']) == 2:
        df = df[(df['DT_INTERNACAO'].dt.date >= f['periodo'][0]) & 
                (df['DT_INTERNACAO'].dt.date <= f['periodo'][1])]
    
    # Filtros de Multiselect
    if f['ig']: df = df[df['IG_OBSTETRA'].isin(f['ig'])]
    if f['bairro']: df = df[df['BAIRRO'].isin(f['bairro'])]
    if f['ubs']: df = df[df['UBS'].isin(f['ubs'])]

# AGORA, use este 'df' filtrado para criar seus gráficos!
st.write(f"Visualizando {len(df)} registros após filtros.")

# ... aqui entra o seu código de gráfico (px.bar, st.area_chart, etc)


