turno = input("Em que turno você estuda? (M-matutino, V-vespertino, N-noturno): ")

turno = turno.upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")