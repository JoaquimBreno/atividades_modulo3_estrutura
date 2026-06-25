# TSP com Heurística e VND

Projeto final da disciplina Estrutura de Dados e Complexidade de Algoritmos (UFPB).

Resolve o Problema do Caixeiro Viajante com:
- heurística de construção: vizinho mais próximo
- busca local: VND com 2-opt, swap e relocate

## Como rodar

```bash
python main.py
```

Precisa só de Python 3, sem dependências externas.

## Estrutura

```
main.py              roda os experimentos
tsp/
  instancia.py       lê arquivos TSPLIB (.tsp)
  solucao.py         calcula custo da rota
  construcao.py      vizinho mais próximo
  vizinhanca.py      movimentos 2-opt, swap, relocate
  vnd.py             Variable Neighborhood Descent
instancias/          eil51, berlin52, st70, kroA100
relatorio/main.tex   relatório A1 (Overleaf)
```

## Instâncias

Benchmarks do TSPLIB: eil51, berlin52, st70, kroA100.

## Relatório

O relatório em LaTeX está em `relatorio/main.tex`. Compila no Overleaf e gera o PDF pro SIGAA.
