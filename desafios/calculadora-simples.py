# Calculadora Simples 

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b if b != 0 else 'Erro: Divisão por zero'

def calculadora():
    n1 = float(input("Digite o primeiro número: "))
    op = input("Digite a operação (+, -, *, /): ")
    n2 = float(input("Digite o segundo número: "))

    if op == '+':
        resultado = somar(n1, n2)
    elif op == '-':
        resultado = subtrair(n1, n2)
    elif op == '*':
        resultado = multiplicar(n1, n2)
    elif op == '/':
        resultado = dividir(n1, n2)
    else:
        resultado = 'Operação inválida'
    print(f"Resultado: {resultado :.2f}")   

calculadora()