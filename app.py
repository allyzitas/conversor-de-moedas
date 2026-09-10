import streamlit as st
import requests

def moeda_valida(codigo):
    return codigo.isalpha() and len(codigo) == 3

def buscar_taxas(moeda_base):
    try:
        resposta = requests.get(f"https://open.er-api.com/v6/latest/{moeda_base}", timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.exceptions.RequestException:
        return None

    if dados.get("result") != "success":
        return None

    return dados["rates"]

st.title("Conversor de Moedas")
st.write("Cotações em tempo real via API pública.")

col1, col2 = st.columns(2)
with col1:
    moeda_origem = st.text_input("Moeda de origem (ex: USD)", "USD").upper()
with col2:
    moeda_destino = st.text_input("Moeda de destino (ex: BRL)", "BRL").upper()

valor = st.number_input("Valor a converter", min_value=0.0, value=100.0, step=1.0)

if st.button("Converter"):
    if not moeda_valida(moeda_origem) or not moeda_valida(moeda_destino):
        st.error("Digite códigos de moeda válidos, com 3 letras (ex: USD, BRL).")
    else:
        taxas = buscar_taxas(moeda_origem)
        if taxas is None or moeda_destino not in taxas:
            st.error("Não foi possível encontrar essa cotação. Verifique os códigos digitados.")
        else:
            resultado = valor * taxas[moeda_destino]
            st.success(f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")
            