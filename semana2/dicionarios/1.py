medias_alunos = []

for aluno in range(1, 11):  # Vai de 1 a 10 (10 alunos)
    print(f"Notas do Aluno {aluno}:")
    notas = []
    
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")