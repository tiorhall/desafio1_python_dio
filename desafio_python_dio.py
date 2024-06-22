menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"R$ {valor:.2f}")
            print("Depositado com sucesso.\n")
            print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")

        else:
            print("Operação falhou! O valor informado é inválido.\n")
            print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")
            print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.\n")
            print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.\n")
            print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")
            print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")


        else:
            print("Operação falhou! O valor informado é inválido.\n")
            print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================\n")
        print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")
        print("OBRIGADE POR USAR NOSSOS SERViÇOS!!!")
