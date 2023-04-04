# Estrutura Dicionário

# Criação de Dicionários

dicionario = {}

dicionario = dict()

dicionario = { 'nome': 'Daniel', 'idade': 39, 'altura': 1.72 }
 
print(dicionario)
print(dicionario['idade'])


# Adicionando elementos em um Dicionário

dicionario['peso'] = 103.5 # Acrescentando um elemento no objeto
dicionario['altura'] = 1.77 # Substituindo o valor de um elemento do objeto

print(dicionario)

# Iterando sobre um Dicionário

for chave in dicionario:
    print(chave, dicionario[chave]) # Ele vai percorrer o objeto e o valor do elemento

# Testando a existência de um Elemento

print('programador' in dicionario) # Retorna que a chave "programador" não está no Objeto, portanto o resultado será "False"
print('peso' in dicionario) # Retorna que a chave "peso" está no Objeto, portanto o resultado será "True"