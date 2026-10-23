import csv 

with open('dados.csv', 'r') as arquivos_csv:
    leitor = csv.reader(arquivos_csv)
    for linha in leitor:
        print(linha)

# Escrevendo em um arquivo CSV

import csv 

dados = [
    ['Nome', 'Idade'], ['Kauã', 20], ['Maria', 21]
]

with open('dados.csv', 'w', newline='') as arquivos_csv:
    escritor = csv.writer(arquivos_csv)
    escritor.writerows(dados)