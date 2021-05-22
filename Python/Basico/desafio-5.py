"""
Faça um programa que ao receber uma lista de nomes, chame uma função que retorne a quantidade de letras de cada palavra
"""

def contador_Letras(lista_de_palavras):
    contador = []
    for x in lista_de_palavras:
        letras = len(x)
        contador.append(letras)
    return contador
        
if __name__ == "__main__":
    lista = ["josh", "python", "linux", "POO"]
    print(contador_Letras(lista))