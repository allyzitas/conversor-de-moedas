import requests

def moeda_valida(codigo):
    return codigo.isalpha() and len(codigo) == 3

def buscar_taxas(moeda_base):
    try:
        resposta = requests.get(f"https://open.er-api.com/v6/latest/{moeda_base}", timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.exceptions.RequestException:
        print("Erro: moeda de origem inválida ou API indisponível.")
        return None

    dados = resposta.json()

    if dados.get("result") != "success":
        print("Erro: moeda de origem inválida ou API indisponível.")
        return None

    return dados["rates"]

def converter(valor, taxa):
    return valor * taxa

def fazer_conversao():
    moeda_origem = input("Moeda de origem (ex: USD): ").upper()
    taxas = buscar_taxas(moeda_origem)

    if taxas is None:
        return

    moeda_destino = input("Moeda de destino (ex: BRL): ").upper()
    if moeda_destino not in taxas:
        print("Moeda de destino não encontrada.")
        return

    try:
        valor = float(input(f"Valor em {moeda_origem}: "))
    except ValueError:
        print("Erro: digite um número válido.")
        return

    taxa = taxas[moeda_destino]
    resultado = converter(valor, taxa)
    print(f"{valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")

def main():
    print("Conversor de Moedas $$$")

    while True:
        fazer_conversao()
        continuar = input("\nFazer outra conversão? (s/n): ").lower()
        if continuar != "s":
            print("Programa encerrado!")
            break
        print()

if __name__ == "__main__":
    main()