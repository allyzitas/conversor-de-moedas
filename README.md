# Conversor de Moedas

Conversor de moedas em Python com cotações em tempo real, via API pública.

## Funcionalidades

- Conversão entre qualquer par de moedas suportado pela API
- Cotações atualizadas em tempo real
- Validação de entrada (código de moeda e valores)
- Tratamento de erros de conexão e digitação
- Loop de conversões contínuas, sem precisar reiniciar o programa

## Tecnologias utilizadas

- Python 3
- [Requests](https://docs.python-requests.org/) — para consumo da API
- [ExchangeRate API](https://www.exchangerate-api.com/) — fonte das cotações

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/allyzitas/conversor-de-moedas.git
cd conversor-de-moedas
```

2. Instale as dependências:

```bash
pip install requests
```

3. Execute o programa:

```bash
python conversor.py
```

## Demonstração
```
Conversor de Moedas (taxas em tempo real)
Moeda de origem (ex: USD): usd
Moeda de destino (ex: BRL): brl
Valor em USD: 100
100.0 USD = 540.00 BRL
```

Desenvolvido por Alanis como projeto de estudo em Python.
