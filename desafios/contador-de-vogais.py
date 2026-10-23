# Contador de Vogais 
def contar_vogais(palavra):
    vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛ'
    return sum(1 for letra in palavra.lower() if letra in vogais)

print(contar_vogais(input('Digite uma palavra: ')))