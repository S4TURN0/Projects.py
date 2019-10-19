#!/usr/bin/python3.7
from Conta import Iconta
"""
Software de gerenciamento bancário. Esse software poderá ser caraz de criar clientes e contas.
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e saldo.
"""

Client1 = Iconta("Rick", "123.456.789-10", 22)
print(Client1.get_Status())
print(Client1.get_Saldo())
Client1.depositar(100)
Client1.depositar(200)
Client1.depositar(500)
Client1.sacar(1000)
Client1.sacar(800)
print(Client1.get_Saldo())
print(Client1.get_Status())
Client1.dados()

Client2 = Iconta("Morty", "109.876.543-21", 44)

Client2.dados()