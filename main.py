menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do Deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}"

        else:
            print("Operação falhou! o valor informado é invalido.")



    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))

        excendeu_saldo = valor > saldo
        excendeu_limite = valor > limite

        excendeu_saque = numero_saques >= LIMITE_SAQUES


        if excendeu_saldo:
            print("Operação falhou! você não tem saldo suficiente.")

        elif excendeu_limite:
            print("Operação Falhou! o valor do saque excede o limite.")

        elif excendeu_saque:
            print("Operação Falhou! Número máximo de saque excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques += 1


        else:
            print("Operação falhou! o valor informado é inválido.")



    elif opcao == "e":
        print("\n =============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

