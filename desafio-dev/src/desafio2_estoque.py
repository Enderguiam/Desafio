import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Movimentacao:
    identificador: int
    codigo_produto: int
    tipo: str
    quantidade: int
    descricao: str


class Estoque:
    def __init__(self, caminho_json: str):
        dados = json.loads(Path(caminho_json).read_text(encoding="utf-8"))
        self.produtos = {
            item["codigoProduto"]: {
                "descricao": item["descricaoProduto"],
                "estoque": int(item["estoque"]),
            }
            for item in dados["estoque"]
        }
        self.movimentacoes: dict[int, Movimentacao] = {}

    def movimentar(self, movimentacao: Movimentacao) -> int:
        if movimentacao.identificador in self.movimentacoes:
            raise ValueError("O identificador da movimentação já existe.")

        if movimentacao.codigo_produto not in self.produtos:
            raise ValueError("Produto não encontrado.")

        if movimentacao.tipo not in {"entrada", "saida"}:
            raise ValueError("Tipo inválido. Use 'entrada' ou 'saida'.")

        if movimentacao.quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        produto = self.produtos[movimentacao.codigo_produto]

        if movimentacao.tipo == "saida":
            if movimentacao.quantidade > produto["estoque"]:
                raise ValueError("Estoque insuficiente para realizar a saída.")
            produto["estoque"] -= movimentacao.quantidade
        else:
            produto["estoque"] += movimentacao.quantidade

        self.movimentacoes[movimentacao.identificador] = movimentacao
        return produto["estoque"]

    def listar_produtos(self) -> None:
        print("\n=== ESTOQUE ATUAL ===")
        for codigo, produto in self.produtos.items():
            print(
                f"{codigo} - {produto['descricao']}: "
                f"{produto['estoque']} unidades"
            )


def executar(caminho_json: str) -> None:
    estoque = Estoque(caminho_json)

    print("\n=== DESAFIO 2 - MOVIMENTAÇÃO DE ESTOQUE ===")
    estoque.listar_produtos()

    try:
        identificador = int(input("\nNúmero identificador da movimentação: "))
        codigo = int(input("Código do produto: "))
        tipo = input("Tipo (entrada/saida): ").strip().lower()
        quantidade = int(input("Quantidade: "))
        descricao = input("Descrição da movimentação: ").strip()

        movimentacao = Movimentacao(
            identificador=identificador,
            codigo_produto=codigo,
            tipo=tipo,
            quantidade=quantidade,
            descricao=descricao,
        )

        estoque_final = estoque.movimentar(movimentacao)

        print(f"\nMovimentação registrada com sucesso.")
        print(f"Estoque final do produto: {estoque_final} unidades")

    except ValueError as erro:
        print(f"Erro: {erro}")
