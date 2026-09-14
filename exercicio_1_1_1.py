"""
Exercício 1.1-1

Cite um exemplo real que exija ordenação ou um exemplo real que exija o
cálculo de uma envoltória convexa.
"""


def main() -> None:
    print("Exercício 1.1-1\n")

    print("Exemplo de ordenação:")
    print(
        "  Um site de comércio eletrônico precisa ordenar os produtos de uma\n"
        "  busca por relevância, preço ou avaliação antes de exibi-los ao\n"
        "  usuário. Sem um algoritmo de ordenação eficiente, exibir milhares\n"
        "  de resultados organizados a cada consulta seria inviável em tempo\n"
        "  hábil."
    )

    print("\nExemplo de envoltória convexa:")
    print(
        "  Em robótica e planejamento de movimento, calcular a envoltória\n"
        "  convexa dos pontos que formam um obstáculo permite simplificar a\n"
        "  verificação de colisões: em vez de testar o robô contra o contorno\n"
        "  irregular completo do objeto, basta testá-lo contra o polígono\n"
        "  convexo que o envolve, o que é computacionalmente mais barato."
    )


if __name__ == "__main__":
    main()
