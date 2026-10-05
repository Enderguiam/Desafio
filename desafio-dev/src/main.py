from pathlib import Path

from desafio1_comissao import executar as executar_comissao
from desafio2_estoque import executar as executar_estoque
from desafio3_juros import executar as executar_juros


ROOT = Path(__file__).resolve().parent.parent
VENDAS_JSON = ROOT / "data" / "vendas.json"
ESTOQUE_JSON = ROOT / "data" / "estoque.json"


def menu():
    print("\n" + "=" * 45)
    print("DESAFIO DEV")
    print("=" * 45)
    print("1 - Calcular comissões")
    print("2 - Movimentar estoque")
    print("3 - Calcular juros")
    print("0 - Sair")
    print("=" * 45)


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            executar_comissao(str(VENDAS_JSON))
        elif opcao == "2":
            executar_estoque(str(ESTOQUE_JSON))
        elif opcao == "3":
            executar_juros()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
