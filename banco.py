menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Quanto quer depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            print("Operação inválida, tente novamente.")

    elif opcao == "2":
        valor = float(input("Quanto quer sacar? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação inválida, você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação inválida, o valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação inválida, você ultrapassou o limite de saques por dia.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação inválida, o valor informado e inválido.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("========== EXTRATO ==========")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, tente novamente.")


