import streamlit as st
import pandas as pd
import os
from pathlib import Path

st.title("Dados Gerais")

cwd = os.getcwd()
bd_partos_path = Path(cwd, "Dashboard_Streamlit", "BD_PARTOS_original.xlsx")

df = pd.read_excel(bd_partos_path)

gestacoes = df['GESTACOES'].sum()
st.write(f"Nº de Gestações: {gestacoes}")

duracaoINT = df['DURACAO_INT'].mean()
st.write(f"Média de DuraçãoINT: {duracaoINT:.2f}")

mediaPESO = df['PESO_NASCER'].mean()
st.write(f"Média de Peso ao Nascer: {mediaPESO:.2f}")

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


