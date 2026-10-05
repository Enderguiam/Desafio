from datetime import date, datetime
from decimal import Decimal


TAXA_DIARIA = Decimal("0.025")


def calcular_juros(valor: Decimal, vencimento: date, hoje: date | None = None):
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")

    hoje = hoje or date.today()
    dias_atraso = max((hoje - vencimento).days, 0)
    juros = valor * TAXA_DIARIA * dias_atraso
    total = valor + juros

    return dias_atraso, juros, total


def executar() -> None:
    print("\n=== DESAFIO 3 - JUROS POR ATRASO ===")

    try:
        valor = Decimal(input("Valor original (R$): ").replace(",", "."))
        data_texto = input("Data de vencimento (DD/MM/AAAA): ")
        vencimento = datetime.strptime(data_texto, "%d/%m/%Y").date()

        dias, juros, total = calcular_juros(valor, vencimento)

        print(f"\nData de hoje: {date.today().strftime('%d/%m/%Y')}")
        print(f"Dias de atraso: {dias}")
        print(f"Juros: R$ {juros:.2f}")
        print(f"Valor atualizado: R$ {total:.2f}")

    except (ValueError, ArithmeticError) as erro:
        print(f"Erro: {erro}")
