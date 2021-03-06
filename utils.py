from statistics import mean
from tabulate import tabulate
from time import time


def make_table(results: dict[int, list], format="fancy_grid"):
    # Adiciona a média de cada categoria
    for valores_cat in zip(*results.values()):
        media_valores_cat = mean(valores_cat)

        results.setdefault("Média", []).append(round(media_valores_cat, 3))

    # Adiciona a média de cada sample size
    for values in results.values():
        values.append(round(mean(values), 3))

    print(
        tabulate(
            {" ": ["Categoria 1", "Categoria 2", "Categoria 3", "Média"]} | results,
            headers="keys",
            numalign="center",
            tablefmt=format,
        )
    )


def fazer_testes(funcao, repeticoes, sizes=[100, 200, 500, 1000, 2000, 5000, 10000]):
    res = {}
    tempos = {}

    for i in range(repeticoes):
        for cat in [1, 2, 3]:
            for size in sizes:
                start = time()
                desempenho = funcao(cat, size)
                end = time()

                if i == 0:
                    res.setdefault(size, []).append(round(desempenho, 3))

                # Guarda o tempo de execução dos 3 maiores sample sizes para cada categoria

                t = end - start

                tempos.setdefault(size, [0, 0, 0])
                tempos[size][cat - 1] = round(t, 3)

    for ts in tempos.values():
        for t in ts:
            t = t / repeticoes

    return res, tempos
