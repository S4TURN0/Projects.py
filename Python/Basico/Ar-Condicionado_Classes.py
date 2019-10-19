class ArCondicionado(object):
    def __init__(self):
        self.ligado = False
        self.temperatura = 20
    
    def power(self):
        if self.ligado:
            self.ligado = False
            print("Ar Condicionado, desligado")
        else:
            self.ligado = True
            print("Ar Condicionado, ligado")

    def aumentar_temperatura(self):
        if self.ligado:
            if self.temperatura >= 16 and self.temperatura < 30:
                self.temperatura += 1
        else:
            print("Não é possivel aumentar ou diminuir temperatura com o ar desligado")            
    
    def diminuir_temperatura(self):
        if self.ligado:
            if self.temperatura <= 30 and self.temperatura > 16: 
                self.temperatura -= 1
        else:
            print("Não é possivel aumentar ou diminuir temperatura com o ar desligado")   

a = ArCondicionado()
a.power()
print(a.temperatura)
a.aumentar_temperatura()
a.aumentar_temperatura()
a.aumentar_temperatura()
print(a.temperatura)
a.diminuir_temperatura()
print(a.temperatura)
a.power()
a.diminuir_temperatura()
print(a.temperatura)