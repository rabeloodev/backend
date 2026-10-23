import random 

secreto = random.randint(1, 100)
palpite = 0

while palpite != secreto:
    palpite = int(input('Adivinhe o número entre 1 e 100: '))
    if palpite < secreto:
        print('Tente um número maior.')
    elif palpite > secreto:
        print('Tente um número menor.')

print(f'Parabéns! Você acertou o número secreto: {secreto}.')