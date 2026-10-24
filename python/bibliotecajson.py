import json

dados = {
    'nome': 'Kaua',
    'cidade': 'Cumbe'
}

with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo)

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados_lidos = json.load(arquivo)
    print(dados_lidos)