from transacoes import Transactions
x = Transactions()
op = 0


while op < 4:
    print("Menu")
    print("1- Saldo")
    print("2- Depositar")
    print("3- Sacar")
    print("4- Sair\n")
    op = int(input("Introduza uma opção: "))

    if (op == 1):
        x.consultar()
    elif (op == 2):
        x.depositar()  
    elif (op == 3):
        x.levantar() 