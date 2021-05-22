"""
Faça um conversor de centimetros para metros
"""

def centimetro(x):
    i = 1
    if i == 1:
        print("{} Metros ".format(x/100))

x = int(input("Centimentros: "))
centimetro(x)