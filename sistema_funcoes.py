import textwrap


def depositar(saldo, valor, extrato):
    
    if valor < 0:
        print("Operação falhou! Informe um valor valido!")
    
    else:

        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")

    return saldo, extrato


def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saque):
    
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

def filtrar_usuario( cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):

    cpf = input("Informe o CPF(somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios) 

    if usuario:
        print("\n Ja existe um usuario com esse CPF!")
        return
    nome = input("\nInforme o nome completo: ")
    data = input("\nInforme sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco(logradouro, nro - bairro - cidade - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data": data, "cpf": cpf, "endereco": endereco })

    print("==== Usuario cadastrado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios) 

    if usuario:
        print("\n===Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuario não encontrado!")

def listar_contas(contas):

    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("="*100)
        print(textwrap.dedent(linha))

def listar_usuarios(usuarios):

    for usuario in usuarios:
        linha = f"""\
            Nome:\t{usuario['nome']}
            Cpf:\t{usuario['cpf']}
            Endereco:\t{usuario['endereco']}
            Data de nascimento:\t{usuario['data']}
            """
        print("="*100)
        print(textwrap.dedent(linha))

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 3
    usuarios = []
    contas = []
    agencia = "0001"

    while True:
    
        menu = """
======== Menu Bancario ========

1.Depositar
2.Sacar
3.Extrato
4.Criar Usuario
5.Criar Conta
6.Listar Contas
7.Listar usuarios
8.Sair

===============================
=>"""
        
        escolha = int(input(menu))

        if escolha == 1:
            
            valor = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor , extrato)

        elif escolha == 2:

            valor = float(input("Informe o valor do Saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saque = limite_saque,
            )

        elif escolha == 3:
            exibir_extrato(saldo, extrato = extrato)

        elif escolha == 4:
            criar_usuario(usuarios)

        elif escolha == 5:

            numero_conta = len(contas)+1

            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif escolha == 6:
            listar_contas(contas)
        
        elif escolha == 7:
            listar_usuarios(usuarios)
        
        elif escolha == 8:
            False
            break

        else:
            print("Entrada invalida. Digite uma opção disponivel!")



main()
