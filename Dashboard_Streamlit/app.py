import streamlit as st
import pandas as pd

st.set_page_config(
        page_title = "Seja bem-vindo!",
        page_icon = ":earth:"
)

st.sidebar.success("Escolha uma das opções!")
st.title("Início")

df = pd.read_excel('BD_PARTOS_original.xlsx')
st.dataframe(df)

#FILTROS PARA AS DEMAIS PÁGINAS

st.sidebar.header("Filtros Globais")

df['DT_INTERNACAO'] = pd.to_datetime(df['DT_INTERNACAO']) #PERÍODO
min_date = df['DT_INTERNACAO'].min()
max_date = df['DT_INTERNACAO'].max()
periodo = st.sidebar.date_input("Selecionar período", [min_date, max_date])

ig_list = st.sidebar.multiselect("IG do Obstetra", df['IG_OBSTETRA'].unique()) #IG_OBSTETRA
bairro_list = st.sidebar.multiselect("Nome do Bairro", df['BAIRRO'].unique()) #BAIRRO
ubs_list = st.sidebar.multiselect("Nº da UBS", df['UBS'].unique()) #UBS

# Salvando no session_state para todas as páginas acessarem
st.session_state['filtros'] = {
    'periodo': periodo,
    'ig': ig_list,
    'bairro': bairro_list,
    'ubs': ubs_list
}