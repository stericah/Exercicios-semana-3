def verifica_valores_verdadeiros(dicionario):
    for valor in dicionario.values():
        if not valor:
            return False
    return True

exemplo_dicionario = {
    'chave1': True,
    'chave2': 42,
    'chave3': 'Algum valor',
    'chave4': None,
    'chave5': False
}

resultado = verifica_valores_verdadeiros(exemplo_dicionario)

print(resultado)
