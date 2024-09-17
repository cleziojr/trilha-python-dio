menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
def operacoes(valor_inicial):
    QUANTIDADE_DE_SAQUES = 0
    while True:
        print("\nOlá! Seja bem-vindo ao Banco Virtual\nAbaixo, você pode visualizar o menu de serviços oferecidos.\n")
        print(menu)
        opcao = input("Selecione o serviço desejado digitando o caractere inicial. Por exemplo: 'd' para efetuar um depósito. Digite: ")
        if opcao == 'd':
            valor_depositado = float(input("\nInforme a seguir o valor, em reais, que você deseja depositar: "))
            if valor_depositado <= 0.00:
                print("\nValor inválido! \n Operação cancelada. \n")
            else:
                valor_inicial += valor_depositado
                print("\nOperação efetuada com sucesso.\n")
        elif opcao == 's':
            if QUANTIDADE_DE_SAQUES > 3:
                print("\nO limite diário de operações de saque foi atingido.\nOperação cancelada.\n")
            else:
                valor_de_saque = float(input("\nInforme a seguir o valor, em reais, que você deseja sacar: "))
                if valor_de_saque <= 0.00:
                    print("\nValor inválido! \n Operação cancelada. \n")
                elif (valor_de_saque > valor_inicial):
                    print("\nO valor de saque solicitado é superior ao saldo atual!\n Operação cancelada. \n")
                elif valor_de_saque > 500.00:
                    print("\nO valor de saque solicitado é superior ao limite permitido para cada operação de saque!\n Operação cancelada. \n")
                else:
                    valor_inicial -= valor_de_saque
                    QUANTIDADE_DE_SAQUES += 1
                    print("\nOperação efetuada com sucesso.\n")
        elif opcao == 'e':
            print(f"\n\nO saldo atual corresponde à R${valor_inicial:.2f}\n\n")
        elif opcao == 'q':
            print("\nObrigado por utilizar os serviços do Banco Virtual. Volte sempre!\n")
            break
        else:
            print("\nOperação inválida. Por favor solicite uma operação existente por meio do caractere correspondente\n")

valor_inicial = 500.00
operacoes(valor_inicial)
    


