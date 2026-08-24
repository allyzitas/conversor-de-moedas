import requests

def buscar_taxas(moeda_base):
    url = f"https://open.er-api.com/v6/latest/{moeda_base}"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados["rates"] 

def converter(valor, taxa):
    return valor * taxa

def main():
    print("Conversor de Moedas (taxas em tempo real)")

    moeda_origem = input("Moeda de origem: ").upper()
    moeda_destino = input("Moeda de destino: ").upper()

    taxas = buscar_taxas(moeda_origem)

    if moeda_destino not in taxas:
        print("moeda de destino não encontrada.")
        return

    valor = float(input(f"valor em {moeda_origem}: "))
    taxa = taxas[moeda_destino]
    resultado = converter(valor, taxa)

    print(f"{valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")

if __name__ == "__main__":
    main()

