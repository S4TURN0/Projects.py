class Iconta:
    
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.status = True
        self.saldo = 0
        self.limite = 1000
        
    def depositar(self, valor):
            if (self.saldo + valor) <= self.limite:
                self.saldo += valor
                print("Deposito de {} Realizado com sucesso!".format(valor))
                self.status = True
            else:
                print("O valor a ser depositado ultrapassa ao limite da conta!")
    
    def sacar(self, valor):
        if self.status:
            if self.saldo >= valor:
                if self.saldo >= (self.saldo - valor):
                    self.saldo = self.saldo - valor
                    print("Saque de {} reais, realizado com sucesso!".format(valor))
                    if self.saldo == 0:
                        self.set_Status(False)        
                else:
                    print("Valor de saque superior ao saldo atual na conta")
            else:
                print("Valor de saque superior ao saldo atual na conta!")
        else:
            print("Não é possivel sacar com uma conta fechada")
                
    def get_Saldo(self):
        return 'Seu saldo atual é: {} '.format(self.saldo)
   
    def set_Saldo(self, valor):
        self.saldo += valor
        
    def dados(self):
        print("\nDados do Cliente")
        print(self.get_Nome())
        print(self.get_Cpf())
        print(self.get_Idade())
        print(self.get_Saldo())
        print(self.get_Limite())
        
    def get_Nome(self):
        return 'Nome do cliente: {}'.format(self.nome)
    def get_Cpf(self):
        return 'CPF do cliente: {}'.format(self.cpf)
    
    def get_Idade(self):
        return 'Idade do cliente: {} anos'.format(self.idade)
    
    def get_Limite(self):
        return 'Limite da conta: {}'.format(self.limite)
    def set_Limite(self, limite):
        self.limite = limite
        
    def get_Status(self):
        return 'A conta está ativa: {}'.format(self.status)
    def set_Status(self, status):
        self.status = status