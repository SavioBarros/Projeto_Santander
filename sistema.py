def depositar(saldo,extrato):
    
    valor = float(input("Informe o valor do deposito: "))

    if valor < 0:
        print("Operação falhou! Informe um valor valido!")
    
    else:

        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")

    return saldo, extrato


def sacar(saldo, extrato, limite, numero_saques, limite_saque):
    
    valor = float(input("Informe o valor do saque: "))

    excedeu_saque = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saque:
        print("Operação falhou! Você não tem saldo suficiente!")
    
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite permitido!")

    elif excedeu_saques:
        print("Operação falhou! Limite de saques atingido!")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        
    else:
        print("Operação falhou! O valor informado é invalido!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 3

    while True:
    
        menu = """
======== Menu Bancario ========

1.Depositar
2.Sacar
3.Extrato
4.Sair

================================
=>"""
        
        escolha = int(input(menu))

        if escolha == 1:
            saldo,extrato = depositar(saldo,extrato)

        elif escolha == 2:
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saque = limite_saque,
            )

        elif escolha == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif escolha == 4:
            False
            break

        else:
            print("Entrada invalida. Digite uma opção disponivel!")



main()