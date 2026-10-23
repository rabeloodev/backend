import random

opcoes = ['pedra', 'papel', 'tesoura']
v_usuario = 0
v_pc = 0

while True:
    usuario = input(
        'Escolha pedra, papel ou tesoura (ou digite "sair" para encerrar): '
    ).lower()
    if usuario == 'sair':
        break
    if usuario not in opcoes:
        print('Opção inválida. Tente novamente.')
        continue   

    pc = random.choice(opcoes)
    print(f'Computador escolheu: {pc}') 

    if usuario == pc:
        print('Empate!')
    
    