"""
Função que recebe um objeto de coleção e retornando o valor do maior numero dentro da coleção 
E outra na qual retorna o menor numero
"""

def max(colecao):
    maior = colecao[0]
    for item in colecao:
        if item > maior:
            maior = item
        
    return maior
def min(colecao):
    menor = colecao[0]
    for item in colecao:
        if item < menor:
            menor = item
    return menor

print(max([1,2,3,4,5,6,7.223123312,8,9,0,123,312,4,231231.7,312,312,31,3,12,323,12,1,212,]))

print(min([1,123,1,32,123,1,12312,3122334543,543,43,534,5,3,32,3,123,3139,0,0.123123123]))