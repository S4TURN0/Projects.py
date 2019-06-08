print('Quantidade de numeros primos possiveis')
y = int(input('Digite o numero final: '))
cont2 = 0
for a in range(1, y+1):
    cont = 0
    for x in range(1, a+1):
        resto = a % x
        if resto == 0:
           cont += 1
    if cont == 2:
            print('O numero {} é primo'.format(a))
            cont2 +=1
print('\nExistem {} numeros primos possiveis'.format(cont2))
