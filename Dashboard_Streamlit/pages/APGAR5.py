import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("APGAR5 por DT_ALTA")

df = pd.read_excel('BD_PARTOS_original.xlsx')

valor_apgar = df['APGAR5'].mean()

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = valor_apgar,
    title = {'text': "Média APGAR 5"},
    gauge = {
        'axis': {'range': [0, 10]}, # Escala de 0 a 10 do APGAR
        'bar': {'color': "#FF4B2B"}, # Cor laranja da sua foto
        'steps': [
            {'range': [0, 7], 'color': "lightgray"},
            {'range': [7, 10], 'color': "gray"}
        ],
    }
))
st.plotly_chart(fig)

#CONECTANDO AO SIDEBAR (FILTROS GLOBAIS)

# Carrega os dados
df = pd.read_excel('BD_PARTOS_original.xlsx')
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