# Conversão de Tipos

idade = '39'
numero1 = '10'
numero2 = '20'

#print(numero1 + numero2) Nesta situação ele vai concatenar as duas variáveis, resultando a string 1020 (numero1 ao lado de numero2)

print(idade, type(idade))

idade_inteira = int(idade) # Conversão Explícita

print(idade_inteira, type(idade_inteira)) 

# int()
# str()
# float()
# bool()

altura = input('Informe sua altura: ')
print(altura, type(altura)) # Resultado será dado como tipo String

peso = float(input('Informe seu peso: '))
print(peso, type(peso)) # Resultado será um Número Real (float)

