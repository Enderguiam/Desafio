import json
from pathlib import Path


def percentual_comissao(valor: float) -> float:
    if valor < 100:
        return 0.0
    if valor < 500:
        return 0.01
    return 0.05


def calcular_comissoes(caminho_json: str) -> dict[str, float]:
    dados = json.loads(Path(caminho_json).read_text(encoding="utf-8"))
    totais: dict[str, float] = {}

    for venda in dados["vendas"]:
        vendedor = venda["vendedor"]
        valor = float(venda["valor"])
        comissao = valor * percentual_comissao(valor)
        totais[vendedor] = totais.get(vendedor, 0.0) + comissao

    return totais


def executar(caminho_json: str) -> None:
    print("\n=== DESAFIO 1 - COMISSÕES ===")
    totais = calcular_comissoes(caminho_json)

    for vendedor, total in totais.items():
        print(f"{vendedor}: R$ {total:.2f}")

    print("\nComissão calculada individualmente para cada venda e totalizada por vendedor.")
