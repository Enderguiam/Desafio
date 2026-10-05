# Desafio Dev

Solução dos três desafios propostos:

1. Cálculo de comissão por vendedor a partir de um JSON de vendas.
2. Movimentação de entrada/saída de estoque.
3. Cálculo de juros por atraso a partir de valor e data de vencimento.

## Tecnologias

- Python 3.10+
- Biblioteca padrão (`json`, `datetime`, `pathlib`)

Não é necessário instalar dependências externas.

## Como executar

Na raiz do projeto:

```bash
python src/main.py
```

O programa apresenta um menu para executar cada desafio.

## Regras implementadas

### Desafio 1 — Comissão

Para cada venda:

- Abaixo de R$ 100,00: 0% de comissão.
- De R$ 100,00 até abaixo de R$ 500,00: 1%.
- A partir de R$ 500,00: 5%.

A comissão é calculada individualmente por venda e depois totalizada por vendedor.

### Desafio 2 — Estoque

Cada movimentação possui:

- número identificador único;
- código do produto;
- tipo da movimentação (entrada ou saída);
- quantidade;
- descrição da movimentação.

O estoque é atualizado e, ao final, é exibida a quantidade final do produto movimentado.

Não é permitida saída superior ao estoque disponível.

### Desafio 3 — Juros

O programa recebe:

- valor original;
- data de vencimento.

Para cada dia de atraso, é aplicada multa de 2,5% sobre o valor original.

Se o vencimento for hoje ou estiver no futuro, não há juros de atraso.

## Estrutura

```text
desafio-dev/
├── data/
│   ├── estoque.json
│   └── vendas.json
├── src/
│   ├── main.py
│   ├── desafio1_comissao.py
│   ├── desafio2_estoque.py
│   └── desafio3_juros.py
└── README.md
```
