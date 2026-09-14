def busca_linear(valores: list[int], alvo: int) -> int:
    """Retorna o índice do alvo usando busca linear, ou -1 se não existir."""
    for indice, valor in enumerate(valores):
        if valor == alvo:
            return indice
    return -1


def busca_binaria(valores: list[int], alvo: int) -> int:
    """Retorna o índice do alvo em uma lista ordenada usando busca binária."""
    inicio = 0
    fim = len(valores) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if valores[meio] == alvo:
            return meio
        if valores[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def main() -> None:
    valores = [3, 8, 12, 17, 21, 29, 34, 41, 56, 63, 72]

    try:
        alvo = int(input("Digite o valor que deseja buscar: "))
    except ValueError:
        print("Erro: informe um número inteiro válido.")
        return

    indice_linear = busca_linear(valores, alvo)
    indice_binario = busca_binaria(valores, alvo)

    print(f"\nLista ordenada: {valores}")
    print(f"Busca linear: índice {indice_linear}")
    print(f"Busca binária: índice {indice_binario}")
    print("\nComplexidade:")
    print("Busca linear  -> O(n)")
    print("Busca binária -> O(log n)")


if __name__ == "__main__":
    main()
