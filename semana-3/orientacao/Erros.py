def calcular_media(valores):
    tamanho = len(valores)
    soma = 0.0
    for valor in valores:
        soma += valor
    media = soma / tamanho
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular um novo valor:')
    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(float(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}.'.format(valores, media))



#correções feitas:
#na linha 1/2 foi adicionada a função len para corrigir a variável tamanho dentro da função calcular_media
# #na linha 4 foi removida a variavel i, sem função alguma no código, e corrigido o erro em for
# #foi adicionada a função return para retornar a média calculada através do calcular_media
#no loop while, linha 11,  foi adicionado else com função de adicionar o valor digitado para a lista de valores 
#na última linha foi corrigida a formatação da string 