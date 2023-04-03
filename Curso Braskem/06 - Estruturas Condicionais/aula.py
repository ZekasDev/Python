# Estrutura de Controle de Fluxos de Execuções

idade = 18
if idade >= 18: 
    print('Você é maior de idade.')
else: 
    print('Você é menor de idade.')

''' 
Imprima "Aprovado" caso o estudante tenha uma média superior ou igual a 7
 e reprovado caso a média seja inferior a 7.
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media >= 7:
    print('Sua média é: ',media, 'Você foi Aprovado por média.')
elif media >=5:
    print('Sua média é: ',media, 'Você está em Recuperação')
else: 
    print('Sua média é: ',media, 'Você foi reprovado.')

# Operadores de Condicionamento Conjuntos

media = 10
presenca = 100

if media >= 7 and presenca >= 70: # O Operador AND vai sinalizar que ambas as condições sejam satisfeitas para que a condição seja True.
    print('Você foi aprovado')    # Caso ao invés de AND fosse utilizado o Operador OR, somente uma das condições precisa ser satisfeita para ser True
else: 
    print('Reprovado')
