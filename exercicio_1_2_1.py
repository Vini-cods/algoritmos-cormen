"""
Exercício 1.2-1

Cite um exemplo de aplicação que exige conteúdo algorítmico no nível da
aplicação e discuta a função dos algoritmos envolvidos.
"""


def main() -> None:
    print("Exercício 1.2-1\n")

    print("Aplicação: um serviço de navegação/GPS (ex.: Google Maps, Waze)\n")

    print("Função dos algoritmos envolvidos:")
    print(
        "  - Algoritmo de caminho mais curto (ex.: Dijkstra ou variantes\n"
        "    como A*) para calcular a rota de menor tempo/distância entre a\n"
        "    origem e o destino em um grafo que representa o mapa\n"
        "    rodoviário.\n"
        "  - Algoritmos de interpolação de endereços, que convertem um\n"
        "    endereço digitado em coordenadas geográficas aproximadas.\n"
        "  - Algoritmos de renderização de mapas, que decidem quais ruas,\n"
        "    rótulos e ícones desenhar em cada nível de zoom.\n"
        "  - Algoritmos de estimativa de tempo de chegada, que combinam\n"
        "    dados de tráfego em tempo real com o grafo de rotas."
    )

    print(
        "\nSem esses algoritmos, a aplicação dependeria apenas de hardware\n"
        "rápido, interface gráfica e rede — mas não conseguiria de fato\n"
        "calcular uma rota, o que é o núcleo do serviço."
    )


if __name__ == "__main__":
    main()
