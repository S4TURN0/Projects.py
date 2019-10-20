def contador_Letras(lista_de_palavras):
    contador = []
    for x in lista_de_palavras:
        letras = len(x)
        contador.append(letras)
    return contador
        
if __name__ == "__main__":
    lista = ["josh", "python", "linux", "POO"]
    print(contador_Letras(lista))