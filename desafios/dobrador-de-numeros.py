# Dobrador de Números 

entradas = input('Digite os números separados por espaço: ').split()
numeros = [int(x) for x in entradas]

dobrados = [x * 2 for x in numeros]

print('Números dobrados:', dobrados)