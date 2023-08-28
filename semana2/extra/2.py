def calcular_preco_aluguel(km_percorridos, dias_alugados):
    preco_por_dia = 80.00
    preco_por_km = 0.20
    
    total_dias = dias_alugados * preco_por_dia
    total_km = km_percorridos * preco_por_km
    
    preco_total = total_dias + total_km
    return preco_total

km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias alugados: "))

preco_total = calcular_preco_aluguel(km_percorridos, dias_alugados)

print(f"O preço a pagar é: R${preco_total:.2f}")
