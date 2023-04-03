# Estrutura de Laço Condicional

# Jogo de Adivinhar um Número:

num_picked = 17

num_choosed = int(input('Informe um número entre 1 e 20: '))

while num_choosed != num_picked:
    print('Você errou, tente novamente.')
    num_choosed = int(input('Informe um número entre 1 e 20: '))

print('Parabéns, você acertou o número.')

# Contador

cont = 0

while cont < 5:
    print(cont)
    
    cont = cont + 1

# Vai realizar 5 interações, 0, 1, 2, 3 e 4 (cont < 5)