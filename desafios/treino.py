# Nota escolar 
print('Vamos verificar sua nota escolar.')
n1 = int(input('informe sua nota: '))

if n1 == 10:
    print('Parabéns, você tirou nota máxima!')
elif n1 >= 5:
    print('Você foi aprovado!')
elif n1 >= 4:
    print('Você está de recuperação!')
else:
    print('Você foi reprovado!')

# Número par ou ímpar 
print('Vamos verificar se o número é par ou ímpar.')
numero = float(input('Informe um número: '))

if numero % 2 == 0:
    print(f'o número {numero} é par. ')
else:
    print(f'o número {numero} é ímpar. ')

