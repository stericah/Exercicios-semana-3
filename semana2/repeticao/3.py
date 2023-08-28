while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    
    if 0 <= nota <= 10:
        break  
    else:
        print("Valor inválido. A nota deve estar entre zero e dez.")

print("Você digitou uma nota válida:", nota)