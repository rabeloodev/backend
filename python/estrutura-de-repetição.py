# Estruturas de repetição(for e while)
# Controle de fluxo
nomes = ['Kaua', 'Rabelo', 'Maria']
for nome in nomes:
    print('Olá, ', nome)

# Função range 
for i in range(5):
    print(i)

# Estrutura while
contador = 0
while contador < 5:
    print('Contagem: ', contador)
    contador += 1

# Controle de loops (break e continue)
#Break
for numero in range(10):
    if numero == 5:
        break
    print('Número: ', numero)

#continue
for n in range(5):
    if n == 2:
        continue
    print(n)

# Compreensão de listas 
numero = [x for x in range(5)]
print(numero)

# Compreensão de listas com condições
pares = [x for x in range(10) if x % 2 == 0]
print(pares)