from datetime import date
from decimal import Decimal
import tempfile
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from desafio1_comissao import calcular_comissoes, percentual_comissao
from desafio2_estoque import Estoque, Movimentacao
from desafio3_juros import calcular_juros


def test_comissao():
    assert percentual_comissao(99.99) == 0
    assert percentual_comissao(100) == 0.01
    assert percentual_comissao(499.99) == 0.01
    assert percentual_comissao(500) == 0.05


def test_juros():
    dias, juros, total = calcular_juros(
        Decimal("100"),
        date(2026, 10, 1),
        date(2026, 10, 5),
    )
    assert dias == 4
    assert juros == Decimal("10.000")
    assert total == Decimal("110.000")


def test_estoque():
    data = {"estoque": [{"codigoProduto": 1, "descricaoProduto": "Produto", "estoque": 10}]}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data, f)
        caminho = f.name

    estoque = Estoque(caminho)
    final = estoque.movimentar(Movimentacao(1, 1, "entrada", 5, "Reposição"))
    assert final == 15
    final = estoque.movimentar(Movimentacao(2, 1, "saida", 3, "Venda"))
    assert final == 12


if __name__ == "__main__":
    test_comissao()
    test_juros()
    test_estoque()
    print("Todos os testes passaram.")
