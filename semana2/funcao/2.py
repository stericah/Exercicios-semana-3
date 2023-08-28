def reverso_numero(numero):
    reverso = 0
    while numero > 0:
        digito = numero % 10
        reverso = reverso * 10 + digito
        numero //= 10
    return reverso

numero_original = int(input("Digite um número inteiro: "))
reverso = reverso_numero(numero_original)
print("O reverso do número é:", reverso)
