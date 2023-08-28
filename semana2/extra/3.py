def calcular_novo_salario(salario_atual):
    if salario_atual <= 1000:
        novo_salario = salario_atual * 1.20  # 20%
    elif salario_atual <= 2800:
        novo_salario = salario_atual * 1.10  # 10%
    else:
        novo_salario = salario_atual * 1.05  # 5%
    return novo_salario

salario_atual = float(input("Digite o salário atual do funcionário: "))

novo_salario = calcular_novo_salario(salario_atual)

print(f"O novo salário do funcionário é: R${novo_salario:.2f}")