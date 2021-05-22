"""
Faça uma calculadora simples que utilize funções para chamar cada operação
"""

def soma():
    x = float(input("\nPrimeiro numero: "))
    y = float(input("Segundo numero: "))
    print("\nResultado da soma: ",x+y)
    
def sub():
    x = float(input("\nPrimeiro numero: "))
    y = float(input("Segundo numero: "))
    if (x <= y):
        print ("\nResultado da subtração:", y-x)
    else:
        print("\nResultado da subtração:",x-y)

def mult():
    x = float(input("\nPrimeiro numero: "))
    y = float(input("Segundo numero: "))
    print ("\nResultado da multiplicação:", x*y)

def div():
    try:
        x = float(input("\nPrimeiro numero: "))
        y = float(input("Segundo numero: "))
        print ("\nResultado da divisão: {:.3f} ".format(x/y)) #O resultado só irá aparecer ate 3 casas decimais
    except ZeroDivisionError as e:
        print("Não é possivel realizar divisão por zero, erro: ", e)

opcao = True
while opcao:
    print("\nCalculadora Basica")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    i = int(input("Digite sua opção: "))
    if i == 1: 
        soma()
    elif i == 2:
        sub()
    elif i== 3:
        mult()

    elif i==4:
        div()

    elif i==0:
        break
    else:
        print("Entrada Invalida")