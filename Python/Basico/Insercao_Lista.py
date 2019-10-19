"""
Programa que lê indeterminada quantidade de itens e insere na lista. Ao final das inserções, imprime a quantidade de dados inseridos e o conteudo. 
"""
x = 0
i = []


while True:
    y = input("\nItem a ser inserido: ")
    i.append(y)
    x += 1 
    y = input("\nPara sair, digite 1: ")
    if y == "1":
        break

print ("\nA list tem {} itens inseridos \nSendo eles: {} ".format(x,i))