from tsp.vizinhanca import (
    aplicar_2opt,
    aplicar_relocate,
    aplicar_swap,
    melhor_2opt,
    melhor_relocate,
    melhor_swap,
)
from tsp.solucao import calcular_custo


def vnd(rota, matriz):
    # desce o morro trocando de vizinhanca quando trava
    rota = rota[:]
    melhorou = True

    while melhorou:
        melhorou = False

        # ordem fixa: 2-opt -> swap -> relocate
        par, delta = melhor_2opt(rota, matriz)
        if par and delta < 0:
            aplicar_2opt(rota, par[0], par[1])
            melhorou = True
            continue  # melhorou? volta pro 2-opt

        par, delta = melhor_swap(rota, matriz)
        if par and delta < 0:
            aplicar_swap(rota, par[0], par[1])
            melhorou = True
            continue

        par, delta = melhor_relocate(rota, matriz)
        if par and delta < 0:
            aplicar_relocate(rota, par[0], par[1])
            melhorou = True

    # recalcula no final pq swap/relocate nao ficaram atualizando custo incremental
    return rota, calcular_custo(rota, matriz)
