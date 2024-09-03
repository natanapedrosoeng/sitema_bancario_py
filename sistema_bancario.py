menu = """

Informe o número da opção que deseja realizar:

[1] Depositar
[2] Sacar
[3] Solicitar Extrato
[4] Finalizar Operação

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    selecao = input(menu)

    if selecao == "1":
        valor = float(input("Informe o valor que você quer depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif selecao == "2":
        valor = float(input("Informe o valor que você quer sacar: "))

        ultrapassou_saldo = valor > saldo

        ultrapassou_limite = valor > limite

        ultrapassou_saques = numero_saques >= limite_saques

        if ultrapassou_saldo:
            print("Falha na operação! Você não tem saldo suficiente.")

        elif ultrapassou_limite:
            print("Falha na operação! O valor do saque excede o limite.")

        elif ultrapassou_saques:
            print("Falha na operação! Você excedeu o número de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif selecao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif selecao == "4":
        break

    else:
        print("Esta operação é inválida, por favor selecione novamente a operação desejada.")
