from tsp.solucao import calcular_custo


def delta_2opt(rota, i, j, matriz):
    # troca 2 arestas por outras 2 sem remontar a rota inteira
    n = len(rota)
    if i > j:
        i, j = j, i
    if j - i < 2:
        return 0  # nao da pra fazer 2opt em cima de nada

    a = rota[i]
    b = rota[(i + 1) % n]
    c = rota[j]
    d = rota[(j + 1) % n]

    antes = matriz[a][b] + matriz[c][d]
    depois = matriz[a][c] + matriz[b][d]
    return depois - antes


def aplicar_2opt(rota, i, j):
    if i > j:
        i, j = j, i
    # inverte o pedaco do meio, efeito pratico do 2-opt
    rota[i + 1 : j + 1] = reversed(rota[i + 1 : j + 1])


def melhor_2opt(rota, matriz):
    n = len(rota)
    melhor_delta = 0
    melhor_par = None

    for i in range(n - 1):
        for j in range(i + 2, n if i > 0 else n - 1):
            d = delta_2opt(rota, i, j, matriz)
            if d < melhor_delta:
                melhor_delta = d
                melhor_par = (i, j)

    return melhor_par, melhor_delta


def aplicar_swap(rota, i, j):
    rota[i], rota[j] = rota[j], rota[i]


def melhor_swap(rota, matriz):
    # recalcula custo inteiro, delta de swap da dor de cabeca
    n = len(rota)
    custo_atual = calcular_custo(rota, matriz)
    melhor_par = None
    melhor_custo = custo_atual

    for i in range(n):
        for j in range(i + 1, n):
            nova = rota[:]
            aplicar_swap(nova, i, j)
            c = calcular_custo(nova, matriz)
            if c < melhor_custo:
                melhor_custo = c
                melhor_par = (i, j)

    if melhor_par:
        return melhor_par, melhor_custo - custo_atual
    return None, 0


def aplicar_relocate(rota, i, j):
    # tira cidade de i e encaixa em j
    if i == j:
        return
    cidade = rota.pop(i)
    if j > i:
        j -= 1  # indice muda depois do pop
    rota.insert(j, cidade)


def melhor_relocate(rota, matriz):
    # testa tudo e pega o melhor
    n = len(rota)
    custo_atual = calcular_custo(rota, matriz)
    melhor_par = None
    melhor_custo = custo_atual

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            nova = rota[:]
            aplicar_relocate(nova, i, j)
            c = calcular_custo(nova, matriz)
            if c < melhor_custo:
                melhor_custo = c
                melhor_par = (i, j)

    if melhor_par:
        return melhor_par, melhor_custo - custo_atual
    return None, 0
