def atualizar_saldo(saldo,valor,operacao):
    if operacao == "deposito":
        saldo = saldo + valor
    elif operacao == "saque":
        saldo = saldo - valor

    return saldo


saldo = float(input("Digite seu saldo atual : "))
valor = float(input("Digite seu valor atual : "))
operacao = input("Digite seu deposito ou saque : ")

saldo_novo = atualizar_saldo(saldo, valor, operacao)
print(f"Novo saldo: {saldo_novo: .2f}")