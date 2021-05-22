"""
Faça um programa simples de soma e subtração que utilize "argv" como entrada de dados
"""

import sys

argumentos = []

if len(sys.argv) >= 3:
    argumentos.append(sys.argv[1])  #Primeiro parametro adicionado a posicao [0] da lista
    argumentos.append(sys.argv[2])  #Segundo parametro adicionado a posicao [1] da lista
    argumentos.append(sys.argv[3])  #Terceiro argumento adicionado a posicao [2] da lista

def soma(n1, n2):
    return n1 + n2

def sub(n1,n2):
    if n1 < n2:
        return n2 - n1
    return n1 - n2

if argumentos[0] == "soma":
    resp = soma(float(argumentos[1]), float(argumentos[2]))
    print(resp)
elif argumentos[0] == "sub":
    resp = sub(float(argumentos[1]), float(argumentos[2]))
    print(resp)

print(pow(3,3,3))
