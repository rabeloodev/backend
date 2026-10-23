meu_dict = {
    'nome': 'python', 'ano': 1991,
    'tipo': 'linguagem de programação'
}
print(meu_dict)

print(meu_dict['nome'])

meu_dict['ano'] = 2026
print(meu_dict)

print(meu_dict.keys())
print(meu_dict.values())

# Operadores e métodos 

lista = [3, 1, 34, 1, 5]
lista.sort()
print(lista)

# conjuntos 
meu_conjunto = {1, 2, 3, 4, 5}
meu_conjunto.add(6)
print(meu_conjunto)

#dic 

valor = meu_dict.pop('ano')
print(valor)
print(meu_dict)

