perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(pergunta + " (S-sim ou N-não): ").upper()
    while resposta != "S" and resposta != "N":
        print("Resposta inválida. Responda com 'S' para sim ou 'N' para não.")
        resposta = input(pergunta + " (S-sim ou N-não): ").upper()
    respostas.append(resposta)

positivas = respostas.count("S")

if positivas == 2:
    print("Suspeita")
elif 3 <= positivas <= 4:
    print("Cúmplice")
elif positivas == 5:
    print("Assassino")
else:
    print("Inocente")