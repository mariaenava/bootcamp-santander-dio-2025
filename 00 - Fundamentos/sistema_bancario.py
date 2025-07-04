import sys

conta = {'nome': 'Maria Eduarda Nava',
         'apelido': 'Maria',
         'saldo' : 100.00,
         'limite': 500.00}

extrato = []
LIMITE_SAQUES = 3


def main():
    print(f"\nBem vindo(a), {conta['apelido']}!\n")
    menu()


def menu():
    while True:
        print(" MENU ".center(30, "="))
        opcao = input("\nO que deseja fazer hoje?\n[1] Depósito\n[2] Saque\n[3] Extrato\n[4] Sair\n---> Opção escolhida: ").strip().upper()
        print()
        if opcao == '1':
            depositos()
        elif opcao == '2':
            saques()
        elif opcao == '3':
            extratos()
        elif opcao == '4':
            sys.exit("Você saiu do sistema. Até a próxima!")
        else:
            print('Opção inválida! Por favor, selecione novamente a opção desejada.\n')


def depositos():
    print(" DEPÓSITOS ".center(30, "="), end='\n'*2)
    while True:
        movimentacao = {}
        confirmacao = input("Deseja fazer um depósito?\n[S] Sim\n[N] Não\n---> Opção escolhida: ").strip().upper()
        if confirmacao == 'S':
            try:
                valor = float(input("\nValor do depósito: ").strip())
            except Exception:
                print("Insira um valor válido.\n")
                continue
            else:
                if valor > 0:
                    conta['saldo'] += valor
                    movimentacao['operação'] = "Depósito"
                    movimentacao['valor'] = valor
                    extrato.append(movimentacao)
                    print(f"Depósito de R${valor:.2f} concluído.\n")
                else:
                    print("Operação inválida! O valor do depósito deve ser positivo.\n")
        elif confirmacao == 'N':
            break
        else:
            print('Opção inválida! Por favor, selecione novamente a opção desejada.\n')


def saques():
    print(" SAQUES ".center(30, "="), end='\n'*2)
    qtd_saques = 0
    while True:
        movimentacao = {}
        confirmacao = input("Deseja fazer um saque?\n[S] Sim\n[N] Não\n---> Opção escolhida: ").strip().upper()
        if qtd_saques >= LIMITE_SAQUES:
            print("Operação inválida! Número máximo de saques excedido.\n")
            break
        elif confirmacao == 'S':
            try:
                valor = float(input("\nValor do saque: ").strip())
            except Exception:
                print("Insira um valor válido.\n")
                continue
            else:
                if valor > 0:
                    if valor > conta['limite']:
                        print("Operação inválida! O valor de saque ultrapassa o limite.\n")
                        continue
                    elif valor > conta['saldo']:
                        print("Operação inválida! Você não tem saldo suficiente.\n")
                        continue
                    else:
                        conta['saldo'] -= valor
                        qtd_saques += 1
                        movimentacao['operação'] = "Saque"
                        movimentacao['valor'] = valor
                        extrato.append(movimentacao)
                        print(f"Saque de R${valor:.2f} concluído.\n")
                else:
                    print("Operação inválida! O valor do depósito deve ser positivo.\n")
        elif confirmacao == 'N':
            break
        else:
            print('Opção inválida! Por favor, selecione novamente a opção desejada.\n')

def extratos():
    print(" EXTRATO ".center(30, "="), end='\n'*2)
    if extrato:
        for movim in extrato:
            print(f"{movim['operação']}: R$ {movim['valor']:.2f}")
    else:
        print(f'Não foram feitas movimentações financeiras.\n')
    print(f"\nSaldo atual: R${conta['saldo']:.2f}\n")

    
if __name__ == "__main__":
    main()
