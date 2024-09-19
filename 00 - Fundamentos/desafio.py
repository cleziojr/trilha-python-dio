from datetime import datetime, date

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

lista_operacoes_realizadas = []
data_horario_atual = str(datetime.now())
operacao_escolhida = None

def verifica_limite_de_transacoes(lista_operacoes_realizadas):
    contador = 0
    data_atual = str(date.today())
    for item in lista_operacoes_realizadas:
        if data_atual in data_horario_atual:
            contador += 1
        else:
            continue
    if contador >= 10:
        print("\nVocê atingiu o limite diário de transações financeiras. Por favor, retorne amanhã se deseja efetuar novas transações.\n")
        return False
    else:
        print(f"\nQuantidade de transações financeiras disponíveis: {10-contador}\n")
        return True

def operacoes(valor_inicial):
    quantidade_de_saques = 0
    while True:
        print("\nOlá! Seja bem-vindo ao Banco Virtual\nAbaixo, você pode visualizar o menu de serviços oferecidos.\n")
        print(menu)
        opcao = input("Selecione o serviço desejado digitando o caractere inicial. Por exemplo: 'd' para efetuar um depósito. Digite: ")
        if opcao == 'd':
            if (verifica_limite_de_transacoes(lista_operacoes_realizadas) == False):
                continue
            else:
                valor_depositado = float(input("\nInforme a seguir o valor, em reais, que você deseja depositar: "))
                if valor_depositado <= 0.00:
                    print("\nValor inválido! \n Operação cancelada. \n")
                else:
                    operacao_escolhida = 'DEPÓSITO'
                    valor_inicial += valor_depositado
                    lista_operacoes_realizadas.append(str(data_horario_atual) + f" - {operacao_escolhida}")
                    print("\nOperação efetuada com sucesso.\n")
                    verifica_limite_de_transacoes(lista_operacoes_realizadas)
        elif opcao == 's':
            if quantidade_de_saques > 3:
                print("\nO limite diário de operações de saque foi atingido.\nOperação cancelada.\n")
            elif (verifica_limite_de_transacoes(lista_operacoes_realizadas) == False):
                verifica_limite_de_transacoes(lista_operacoes_realizadas)
            else:
                valor_de_saque = float(input("\nInforme a seguir o valor, em reais, que você deseja sacar: "))
                if valor_de_saque <= 0.00:
                    print("\nValor inválido! \n Operação cancelada. \n")
                elif (valor_de_saque > valor_inicial):
                    print("\nO valor de saque solicitado é superior ao saldo atual!\n Operação cancelada. \n")
                elif valor_de_saque > 500.00:
                    print("\nO valor de saque solicitado é superior ao limite permitido para cada operação de saque!\n Operação cancelada. \n")
                else:
                    operacao_escolhida = 'SAQUE'
                    valor_inicial -= valor_de_saque
                    lista_operacoes_realizadas.append(str(data_horario_atual) + f" - {operacao_escolhida}")
                    print("\nOperação efetuada com sucesso.\n")
                    verifica_limite_de_transacoes(lista_operacoes_realizadas)
        elif opcao == 'e':
            print(f"\n\nO saldo atual corresponde à R${valor_inicial:.2f}\n\n")
            print("\nHistórico de operações:\n")
            for item in lista_operacoes_realizadas:
                print("\n")
                print(item)
        elif opcao == 'q':
            print("\nObrigado por utilizar os serviços do Banco Virtual. Volte sempre!\n")
            break
        else:
            print("\nOperação inválida. Por favor solicite uma operação existente por meio do caractere correspondente\n")

valor_inicial = 500.00
operacoes(valor_inicial)



