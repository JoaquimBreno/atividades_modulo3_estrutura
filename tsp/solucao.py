def calcular_custo(rota, matriz):
    # soma as arestas do ciclo, a ultima volta pro inicio tb
    n = len(rota)
    total = 0
    for i in range(n):
        a = rota[i]
        b = rota[(i + 1) % n]  # % n fecha o ciclo
        total += matriz[a][b]
    return total


def copiar_rota(rota):
    return rota[:]  # shallow copy ja basta, rota eh so int
