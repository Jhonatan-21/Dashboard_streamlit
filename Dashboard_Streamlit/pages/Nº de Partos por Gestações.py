import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path

st.title("Nº de Partos por Gestações")

cwd = os.getcwd()
bd_partos_path = Path(cwd, "Dashboard_Streamlit", "BD_PARTOS_original.xlsx")

df = pd.read_excel(bd_partos_path)

def categorizar_gestacoes(valor):
    if valor <= 2: return '0 - 2'
    elif valor <= 4: return '3 - 4'
    elif valor <= 6: return '5 - 6'
    else: return '9 - 10'

df['Faixa_Gestacoes'] = df['GESTACOES'].apply(categorizar_gestacoes)

df_grafico = df.groupby('Faixa_Gestacoes')['PARTOS'].sum().reset_index()

fig = px.bar(
    df_grafico, 
    x='PARTOS', 
    y='Faixa_Gestacoes', 
    orientation='h',      # 'h' deixa as barras horizontais
    color_discrete_sequence=['#FF4B2B'] # Cor laranja da sua imagem
)

fig.update_yaxes(categoryorder='category descending')
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


