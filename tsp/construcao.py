import random


def vizinho_mais_proximo(matriz, cidade_inicial=None):
    # guloso: sempre vai pro mais perto que ainda nao visitou
    n = len(matriz)
    if cidade_inicial is None:
        cidade_inicial = random.randint(0, n - 1)  # sorteia se ninguem passou

    visitadas = {cidade_inicial}
    rota = [cidade_inicial]
    cidade_atual = cidade_inicial

    while len(visitadas) < n:
        melhor = None
        menor = float("inf")
        for j in range(n):
            if j in visitadas:
                continue
            d = matriz[cidade_atual][j]
            if d < menor:
                menor = d
                melhor = j
        visitadas.add(melhor)
        rota.append(melhor)
        cidade_atual = melhor

    # ciclo fecha sozinho no calcular_custo, nao precisa repetir cidade aqui
    return rota
