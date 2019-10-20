#!/usr/bin/python3.7

from veiculo import Veiculo
from carro import Carro

#MAIN
if __name__ == "__main__":
    print("\nVeiculo 1")
    veiculo1 = Veiculo("Rosa",4,"ford",20)
    print("Cor do veiculo: {} ".format(veiculo1.get_Cor()))
    print("Gasolina no tanque: {} Litros ".format(veiculo1.get_Tanque()))
    print("Marca do veiculo: {} ".format(veiculo1.get_Marca()))

    veiculo1.abastercer(40)
    print("Gasolina no tanque: {} Litros ".format(veiculo1.get_Tanque()))

    print("\nVeiculo 2")
    veiculo2 = Veiculo("Azul", 5, "bmw", 50)
    print("Cor do veiculo: {} ".format(veiculo2.get_Cor()))
    print("Gasolina no tanque: {} Litros ".format(veiculo2.get_Tanque()))
    print("Marca do veiculo: {} ".format(veiculo2.get_Marca()))
    veiculo2.abastercer(60)
    print("Gasolina no tanque: {} Litros ".format(veiculo2.get_Tanque()))

    print("\nCarro ")
    carro_verde = Carro("vermelho", "Civic")
    carro_verde.set_Cor("azul")
    print("Cor do carro: {} ".format(carro_verde.get_Cor()))
    carro_verde.set_Marca("Fiesta")
    print("Marca do carro: {}".format(carro_verde.get_Marca()))
    carro_verde.abastercer(51)
    print("Tanque do carro: {}".format(carro_verde.get_Tanque()))
    carro_verde.abastercer(50)
    print("Tanque do carro: {}".format(carro_verde.get_Tanque()))
