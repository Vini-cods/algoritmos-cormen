"""
Exercício 1.1-4

Em que aspectos os problemas anteriores do caminho mais curto e do
caixeiro-viajante são semelhantes? Em que aspectos eles são diferentes?
"""


def main() -> None:
    print("Exercício 1.1-4\n")

    print("Semelhanças:")
    print(
        "  - Ambos são modelados sobre um grafo com pesos (distâncias) nas\n"
        "    arestas.\n"
        "  - Ambos buscam minimizar o custo total (distância) de um\n"
        "    percurso.\n"
        "  - Ambos têm um número muito grande de soluções candidatas\n"
        "    possíveis, das quais a maioria não é ótima."
    )

    print("\nDiferenças:")
    print(
        "  - O caminho mais curto conecta apenas dois vértices específicos\n"
        "    (origem e destino), sem precisar visitar os demais vértices do\n"
        "    grafo. Já o caixeiro-viajante exige visitar TODOS os vértices\n"
        "    exatamente uma vez e retornar ao ponto de partida.\n"
        "  - O caminho mais curto tem algoritmos eficientes e bem\n"
        "    conhecidos (ex.: Dijkstra, tempo polinomial). O caixeiro-\n"
        "    viajante é NP-completo: não se conhece nenhum algoritmo\n"
        "    eficiente (polinomial) para resolvê-lo de forma exata."
    )


if __name__ == "__main__":
    main()
