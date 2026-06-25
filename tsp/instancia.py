import math
import re
from pathlib import Path


def distancia_euclidiana(p1, p2):
    return round(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))


def ler_tsp(caminho):
    texto = Path(caminho).read_text()
    nome = re.search(r"NAME\s*:\s*(.+)", texto).group(1).strip()
    dim = int(re.search(r"DIMENSION\s*:\s*(\d+)", texto).group(1))
    tipo = re.search(r"EDGE_WEIGHT_TYPE\s*:\s*(\S+)", texto).group(1).strip()

    coords = {}
    if "NODE_COORD_SECTION" in texto:
        bloco = texto.split("NODE_COORD_SECTION")[1].split("EOF")[0]
        for linha in bloco.strip().splitlines():
            partes = linha.split()
            if len(partes) >= 3:
                i = int(partes[0]) - 1
                coords[i] = (float(partes[1]), float(partes[2]))

    n = dim
    matriz = [[0] * n for _ in range(n)]

    if tipo == "EUC_2D":
        for i in range(n):
            for j in range(i + 1, n):
                d = distancia_euclidiana(coords[i], coords[j])
                matriz[i][j] = d
                matriz[j][i] = d
    elif tipo == "EXPLICIT" and "EDGE_WEIGHT_SECTION" in texto:
        bloco = texto.split("EDGE_WEIGHT_SECTION")[1].split("EOF")[0]
        nums = [int(x) for x in bloco.split()]
        k = 0
        for i in range(n):
            for j in range(i + 1, n):
                d = nums[k]
                k += 1
                matriz[i][j] = d
                matriz[j][i] = d
    else:
        raise ValueError(f"formato nao suportado: {tipo}")

    return {"nome": nome, "n": n, "matriz": matriz}
