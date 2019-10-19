from veiculo import Veiculo
#HERANÇA
class Carro(Veiculo):
    """
    O objeto carro sempre tem 4 rodas
    Carro inicia com o tanque vazio e chegando a um limite de 50 litros
    """
    def __init__(self, cor, marca):
        Veiculo.__init__(self, cor, 4, marca, 0)

# POLIFORMISMO
    def abastercer(self, litros):
        if self.tanque + litros > 50:
            print("Erro: A quantidade de abastecimento ultrapassa o limite do tank!")
        else:
            self.tanque += litros
            if self.tanque == 50:
                print("Tanque cheio!")