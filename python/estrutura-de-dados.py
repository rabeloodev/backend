# Listas 

lista = [1, 2, 3, 'python', True]
print(lista)

print(lista[0]) # Acessando o primeiro elemento da lista
print(lista[3]) # Acessando o quarto elemento da lista

lista.append('novo elemento')
print(lista)

lista.remove('python')
print(lista)

lista.pop(0)
print(lista)

for item in lista:
    print(item)