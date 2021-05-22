class Televisao(object):
    def __init__(self):
        self.ligada = False
        self.canal = 0

    def botao_power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1    
        else:
            print("Não é possivel aumentar canais com a televisão desligada")
    
    def diminui_canal(self):
        if self.ligada == True:
            
            if self.canal > 0:
                self.canal -= 1
            else:
                print("Não é possivel diminuir mais canais")
        else:
            print("Não é possivel diminuir canais com a televisão desligada")

a = Televisao()
a.botao_power()
a.aumenta_canal()
print("Televisão ligada: {}".format(a.ligada))
a.aumenta_canal()
print("Canal: {}".format(a.canal))
a.diminui_canal()
print("Canal: {}".format(a.canal))
a.botao_power()
a.diminui_canal()
print("Canal: {}".format(a.canal))