from math import log2


def main() -> None:
    """Compara os tempos de execução de dois algoritmos de ordenação."""
    try:
        n = int(input("Digite o tamanho da entrada n: "))
    except ValueError:
        print("Erro: informe um número inteiro válido.")
        return

    if n <= 0:
        print("Erro: n deve ser maior que zero.")
        return

    insercao = 8 * n**2
    intercalacao = 64 * n * log2(n) if n > 1 else 0

    print(f"\nPara n = {n}:")
    print(f"Ordenação por inserção: {insercao:.2f} passos")
    print(f"Ordenação por intercalação: {intercalacao:.2f} passos")

    if insercao < intercalacao:
        print("\nA ordenação por inserção é mais rápida para esse valor de n.")
    elif insercao > intercalacao:
        print("\nA ordenação por intercalação é mais rápida para esse valor de n.")
    else:
        print("\nOs dois algoritmos apresentam o mesmo custo para esse valor de n.")


if __name__ == "__main__":
    main()
