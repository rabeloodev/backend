n1 = int(input('informe sua nota: '))

if n1 == 10:
    print('Parabéns, você tirou nota máxima!')
elif n1 >= 5:
    print('Você foi aprovado!')
elif n1 >= 4:
    print('Você está de recuperação!')
else:
    print('Você foi reprovado!')