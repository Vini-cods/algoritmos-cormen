from math import factorial, log2, sqrt


def calcular_funcoes(n: int) -> dict[str, float]:
    """Calcula diferentes funções de crescimento para uma entrada n."""
    return {
        "lg n": log2(n),
        "sqrt(n)": sqrt(n),
        "n": float(n),
        "n lg n": n * log2(n),
        "n^2": float(n**2),
        "n^3": float(n**3),
        "2^n": float(2**n),
        "n!": float(factorial(n)),
    }


def main() -> None:
    try:
        n = int(input("Digite o valor de n: "))
    except ValueError:
        print("Erro: informe um número inteiro válido.")
        return

    if n <= 0:
        print("Erro: n deve ser maior que zero.")
        return

    resultados = calcular_funcoes(n)

    print(f"\nFunções de crescimento para n = {n}:\n")
    for nome, valor in resultados.items():
        print(f"{nome:>8}: {valor:.6e}")


if __name__ == "__main__":
    main()
