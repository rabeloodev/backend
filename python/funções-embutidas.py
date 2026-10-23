# Funções Embutidas

#map 
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)

#filter
numeross = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeross))
print(pares)

#zip 
nomes = ['kaua', 'fulano', 'maria']
idades =[20, 30, 50]
combinados = list(zip(nomes, idades))
print(combinados)