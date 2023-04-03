# Estrutura de Repetição "FOR"

'''for i in range(1, 12, 3):
    print(i)'''

# 1, 12, 3 -> 1 é o primeiro parâmetro do contador, 12 é a quantidade de interações que o Laço fará, 3 é quantidade de incrementos que ele fará


# Obtendo 3 notas e calculando uma média através do FOR

soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}: '))

    soma = soma + nota

print(soma / 3)