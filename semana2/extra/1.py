dólarAmericano: 4.91
pesoArgentino: 0.02
dólarAustraliano: 3.18
dólarCanadense: 3.64
francoSuico: 0.42
euro: 5.36
libraesterlina: 6.21

def calcular_conversao(valor_em_reais, taxa_de_conversao):
    valor_em_moeda = valor_em_reais / taxa_de_conversao
    return valor_em_moeda

taxas_de_conversao = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

valor_em_reais = float(input("Digite a quantidade de dinheiro em reais na sua carteira: "))

print("\nQuantidade que você poderia comprar em cada moeda estrangeira:")

for moeda, taxa in taxas_de_conversao.items():
    valor_em_moeda = calcular_conversao(valor_em_reais, taxa)
    print(f"{moeda}: {valor_em_moeda:.2f}")
