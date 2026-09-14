"""
Exercício 1.1-3

Selecione uma estrutura de dados que você já tenha visto antes e discuta
seus pontos fortes e suas limitações.
"""


def main() -> None:
    print("Exercício 1.1-3\n")
    print("Estrutura escolhida: lista ligada (linked list)\n")

    print("Pontos fortes:")
    print(
        "  - Inserção e remoção em O(1) quando já se tem a referência do nó\n"
        "    (não é necessário deslocar elementos, como em um array).\n"
        "  - Tamanho dinâmico: cresce e diminui conforme a necessidade, sem\n"
        "    precisar realocar um bloco contíguo de memória.\n"
        "  - Não desperdiça memória com espaço não utilizado, ao contrário\n"
        "    de um array alocado com folga."
    )

    print("\nLimitações:")
    print(
        "  - Acesso a um elemento por índice é O(n), pois é preciso percorrer\n"
        "    a lista a partir do início (ou do fim, em uma lista duplamente\n"
        "    ligada) até chegar à posição desejada.\n"
        "  - Overhead de memória extra para armazenar os ponteiros/referências\n"
        "    de cada nó.\n"
        "  - Pior localidade de cache comparada a um array, já que os nós\n"
        "    podem estar espalhados pela memória, o que impacta o desempenho\n"
        "    real mesmo quando a complexidade assintótica é favorável."
    )

    print(
        "\nEm contraste, um array (lista contígua) tem acesso O(1) por\n"
        "índice, mas inserção/remoção no meio custa O(n) devido ao\n"
        "deslocamento dos elementos."
    )


if __name__ == "__main__":
    main()
