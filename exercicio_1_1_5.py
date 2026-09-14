"""
Exercício 1.1-5

Mostre um problema real no qual apenas a melhor solução servirá. Em
seguida, apresente um problema em que baste uma solução que seja
"aproximadamente" a melhor.
"""


def main() -> None:
    print("Exercício 1.1-5\n")

    print("Problema em que apenas a melhor solução serve:")
    print(
        "  Cálculo da dosagem exata de um medicamento ou de radiação em um\n"
        "  tratamento médico (radioterapia, por exemplo). Uma dose\n"
        "  'aproximadamente correta' pode ser ineficaz ou perigosa: aqui,\n"
        "  apenas o valor ótimo/exato é aceitável."
    )

    print("\nProblema em que uma solução aproximada é suficiente:")
    print(
        "  Encontrar uma rota de entrega para um caminhão (problema\n"
        "  relacionado ao caixeiro-viajante). Como o problema exato é\n"
        "  NP-completo, na prática empresas de logística usam algoritmos de\n"
        "  aproximação que encontram rotas 'suficientemente boas', com\n"
        "  distância total próxima da ótima, em tempo viável."
    )


if __name__ == "__main__":
    main()
