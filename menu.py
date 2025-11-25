import datetime

def calcular_idade():
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        ano_atual = datetime.date.today().year
        idade = ano_atual - ano_nascimento
        print(f"\nSua idade é de aproximadamente {idade} anos.\n")

def calcular_preco_compra():
    total = 0
    while True:
            preco_item = float(input("Digite o preço do item (ou 0 para finalizar): R$ "))
            if preco_item == 0:
                break
            total += preco_item
            print("Preço inválido. Tente novamente.")
    print(f"\nO preço total da compra é de R$ {total:.2f}.\n")



def menu_principal():
    while True:
        print("===============================")
        print("|     PROGRAMA-COM-MENU       |")
        print("===============================")
        print("1 - Calcular idade")
        print("2 - Calcular preço da compra")
        print("3 - Sair")
        print("===============================")

        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == '1':
            calcular_idade()
        elif opcao == '2':
            calcular_preco_compra()
        elif opcao == '3':
            print("Saindo do programa. Obrigado por usar!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.\n")


if __name__ == "__main__":
    menu_principal()
