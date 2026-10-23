v = float(input('Informe a velocidade do carro (km/h): '))

if v > 80:
    excesso = v - 80
    multa = excesso * 5 
    print(
        f'Multado! Você excedeu o limite de velocidade em {excesso:.2f}. Valor da multa: R${multa:.2f}'
    )
else:
    print('Tenha um bom dia! Dirija com cuidado.')