# Funções

# Exemplo de Funções já utilizadas até o momento:

'''
print() # Imprime uma mensagem no console
input() # Retorna um dado informado pelo usuário
len()   # Recebe uma lista e retorna o tamanho dessa lista
max()   # Retorna o maior valor de umal ista
'''

# Criação de funções

# Função Inicial

def saudacao(): 
    print('Seja bem vindo')
    print('Olá, é um prazer ter você fazendo parte deste curso')

saudacao()


# Função com Parâmetro

def saudacao(nome, curso): 
    print(f'Seja bem vindo, {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}')

saudacao('Daniel', 'Python')
saudacao('Toalhinha', 'REACT')

# Função com Parâmetro Default

def saudacao(nome, curso='Python'): 
    print(f'Seja bem vindo, {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}')

saudacao('Daniel')

# Função com Retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é: ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20, '-')

print('O resultado é:', resultado)