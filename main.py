import time
from pathlib import Path

from tsp.construcao import vizinho_mais_proximo
from tsp.instancia import ler_tsp
from tsp.vnd import vnd

OTIMOS = {
    "eil51": 426,
    "berlin52": 7542,
    "st70": 675,
    "kroa100": 21282,
}

REPETICOES = 10


def rodar_instancia(caminho):
    inst = ler_tsp(caminho)
    nome = inst["nome"].lower()
    matriz = inst["matriz"]
    otimo = OTIMOS.get(nome)

    melhor_custo = float("inf")
    tempos = []

    for _ in range(REPETICOES):
        inicio = time.perf_counter()
        rota_inicial = vizinho_mais_proximo(matriz)
        rota_final, custo = vnd(rota_inicial, matriz)
        fim = time.perf_counter()

        tempos.append(fim - inicio)
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_rota = rota_final

    tempo_medio = sum(tempos) / len(tempos)
    gap = None
    if otimo:
        gap = ((melhor_custo - otimo) / otimo) * 100

    return {
        "nome": nome,
        "n": inst["n"],
        "melhor": melhor_custo,
        "otimo": otimo,
        "gap": gap,
        "tempo_medio": tempo_medio,
        "rota": melhor_rota,
    }


def main():
    pasta = Path(__file__).parent / "instancias"
    arquivos = sorted(pasta.glob("*.tsp"))

    if not arquivos:
        print("nenhuma instancia em instancias/")
        return

    print(f"rodando {REPETICOES}x cada instancia...\n")

    resultados = []
    for arq in arquivos:
        r = rodar_instancia(arq)
        resultados.append(r)

        if r["gap"] is not None:
            print(
                f"{r['nome']}: achado {r['melhor']} "
                f"(otimo {r['otimo']}, gap {r['gap']:.1f}%) "
                f"em {r['tempo_medio']:.2f}s"
            )
        else:
            print(
                f"{r['nome']}: achei {r['melhor']} "
                f"em {r['tempo_medio']:.2f}s"
            )

    print("\nresumo:")
    for r in resultados:
        gap = f", gap {r['gap']:.1f}%" if r["gap"] is not None else ""
        print(f"  {r['nome']}: {r['melhor']}{gap}, tempo medio {r['tempo_medio']:.3f}s")


if __name__ == "__main__":
    main()
