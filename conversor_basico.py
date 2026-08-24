def converter(valor, taxa):
    return valor * taxa

def main():
    taxas = {
        "USD": 5.40, 
        "EUR": 5.85,
        "GBP": 6.80, 
    }

    print("conversor de Moedas")
    print("moedas disponíveís:", ", ".join(taxas.keys()))

    moeda = input("Digite a moeda de origem: ").upper()
    if moeda not in taxas: 
        print("moeda não encontrada.")
        return

    valor = float(input(f"digite o valor em {moeda}: "))
    resultado = converter(valor, taxas[moeda])
    print(f"{valor} {moeda} = {resultado:.2f} BRL")

if __name__ == "__main__":
    main()