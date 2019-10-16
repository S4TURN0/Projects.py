class Veiculo:
    
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
    
    def abastercer(self, litros):
        self.tanque += litros
        print("Carro abastecido com sucesso!")

#Getter's and Setter's
    def get_Cor(self):
        return self.cor

    def set_Cor(self, cor):
        self.cor = cor

    def get_Rodas(self):
        return self.rodas
 
    def set_Rodas(self, rodas):
        self.rodas = rodas

    def get_Marca(self):
        return self.marca
    def set_Marca(self, marca):
        self.marca = marca
    
    def get_Tanque(self):
        return self.tanque