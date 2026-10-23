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
    elif (
        (usuario == 'pedra' and pc == 'tesoura')
        or (usuario == 'papel' and pc == 'pedra')
        or (usuario == 'tesoura' and pc == 'papel')
    ):
        print('Você ganhou esta rodada')
        v_usuario += 1
    else:
        print('Computador ganhou esta rodada')
        v_pc += 1

    print(f'Placar: Você {v_usuario} x Computador: {v_pc}\n')

print(f'Fim de jogo! Placar final: Você {v_usuario} x Computador: {v_pc}')