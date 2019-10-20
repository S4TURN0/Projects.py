contador_Letras = lambda lista : [len(x) for x in lista]

calculadora = {
    'soma': lambda a,b:a+b,
    'sub': lambda a,b: a - b,
    'mult': lambda a,b: a * b,
    'div' : lambda a,b: a/b
}


if __name__ == "__main__":
    lista_animais = ["gato", "cachorro", "porco", "rinoceronte"]
    print(contador_Letras(lista_animais))
    
    soma = calculadora['soma']
    sub = calculadora['sub']
    mult = calculadora['mult']
    div = calculadora['div']
    print('\nA soma é: {}'.format(soma(50,10)))
    print('A subtração é: {}'.format(sub(50,10)))
    print('A multiplicação é: {}'.format(mult(50,10)))
    print('A divisão é: {}'.format(div(50,10)))