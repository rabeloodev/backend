try:
    numero = int(input('informe um valor: '))
    resultado = 10 / numero
    print(resultado)
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except ValueError:
    print('Por favor, informe um número válido.') 

# Usando else 
try: 
    numero = int(input('informe um valor: '))
    resultado = 10 / numero
    print(resultado)
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
else:
    print('A operação foi realizada com sucesso.', resultado)

# Usando finally
try:
    numero = int(input('informe um valor: '))
    resultado = 10 / numero
    print(resultado)
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except ValueError:
    print('Por favor, informe um número válido.')
finally:
    print('Fim do programa.')