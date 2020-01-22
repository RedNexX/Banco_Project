import time

class Transactions(object):
    def __init__(self):
        self.saldo = 250

    def vefDeposit(self, valor):
        if valor >= 0:
            return True
        else:
            return False
        exit   

    def consultar(self):
        print("Saldo Atual: ", self.saldo)
        self.vef = False

    def depositar(self):
        quantidade = int(input("Quanto pretende depositar? "))
        print("A depositar...")
        valor = self.saldo + quantidade
        if Transactions.vefDeposit(self, valor) == True:
            self.saldo += quantidade
            print("Depósito efetuado com sucesso :)")
        else:
            print("Não tens dinheiro Suficiente :(") 
        time.sleep(2)

        print("Saldo Atual: ", self.saldo)

    def levantar(self):
        quantidade = int(input("Quanto pretende levantar? "))
        print("A retirar...")
        time.sleep(2)
        valor = self.saldo - quantidade
        if Transactions.vefDeposit(self, valor) == True:
            self.saldo -= quantidade
            print("Levantamento efetuado com sucesso :)")
        else:
            print("Não tens dinheiro Suficiente :(") 

        print("Saldo Atual: ", self.saldo)