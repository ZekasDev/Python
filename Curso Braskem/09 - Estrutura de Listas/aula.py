# Listas

# Ao invés de criar 3 variáveis para armazenar notas
# n1 = 7.9, n2 = 9.2, n3 = 8.2
# Podemos criar na seguinte nomenclatura:

# notas = [7.9, 9.7, 8.2]

# Criando Listas:

# lista = [] -> Lista Vazia
# lista = list() -> Lista em Função
# lista = [39, 'Dourado', True] -> Lista de Elementos Variados
# lista_lista = [19, [1, 3, 5]] -> Lista de Elementos com Objetos

# Indexação: Acessando um Elemento através de um Índice

lista = [10, 'Zekas', 3.15, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# print(lista[-1]) -> Neste caso ele vai buscar o último Elemento da Lista

# Slices

lista = [10, 20, 30, 40, 50, 60, 5]

print(lista[0:3]) # Vai printar somente os 3 primeiros Objetos do Elemento

# Percorrendo uma Lista

for elemento in lista:
    print(elemento)

print('Comprimento da Lista: ', len(lista))

for i in range(len(lista)): 
    print(lista[i])