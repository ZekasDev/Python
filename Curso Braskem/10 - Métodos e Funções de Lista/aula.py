# Métodos de Listas

lista = [1, 3, 12, 8, 2]

# APPEND (adicona elementos no fim da lista)

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# INSERT (escolhe a posição da inserção)

lista.insert(2, 10) # (Posição, Elemento)

print('Depois do insert: ', lista)

# EXTEND (unir duas listas)

lista2 = [1, 2, 3]

lista.extend(lista2) # Concatenação das duas listas

print('Depois do extend: ', lista)

# POP (remoção de elementos do Objeto)

lista.pop() # Se não passar valor, ele elemina somente o último valor
            
print('Lista após o pop: ', lista)

# REMOVE (remoção de elemento específico do Objeto)

lista.remove(3) # Elimina o PRIMEIRO elemento de valor 3 dentro do Objeto

print('Lista após o remove:' , lista)

# COUNT (quantifica os elementos do objeto com os mesmos valores)

print(lista, 'Quantidade de 2 na Lista: ' , lista.count(2))

# INDEX (diz a posição do elemento dentro do Objeto)

print('Índice do elemento 12: ', lista.index(12))

# SORT (organiza o Objeto)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# FUNÇÕES PARA LISTAS

# LEN

print(len(lista)) # Quantidade de Elementos no Objeto

# SUM

print(sum(lista)) # Soma todos os Elementos no Objeto

# MAX 

print('Maior Elemento da lista: ', max(lista)) # Imprime o maior elemento

# MIN

print('Menor Elemento da lista: ', min(lista)) # Imprime o menor elemento