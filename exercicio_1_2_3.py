"""
Exercício 1.2-3

Qual é o menor valor de n tal que um algoritmo cujo tempo de execução é
100n² funciona mais rapidamente que um algoritmo cujo tempo de execução
é 2^n na mesma máquina?
"""


def menor_n(limite_busca: int = 1000) -> int | None:
    """Retorna o menor n > 0 tal que 100*n**2 < 2**n, ou None se não achar."""
    for n in range(1, limite_busca + 1):
        if 100 * n**2 < 2**n:
            return n
    return None


def main() -> None:
    print("Exercício 1.2-3\n")

    n = menor_n()

    if n is None:
        print("Não foi encontrado um valor de n dentro do limite de busca.")
        return

    print("Comparando 100n² e 2^n para valores crescentes de n:\n")
    for i in range(max(1, n - 3), n + 2):
        insercao = 100 * i**2
        exponencial = 2**i
        mais_rapido = "100n²" if insercao < exponencial else "2^n"
        print(f"n = {i:>2} -> 100n² = {insercao:>8} | 2^n = {exponencial:>8} "
              f"| mais rápido: {mais_rapido}")

    print(f"\nMenor n em que 100n² passa a ser mais rápido que 2^n: n = {n}")


if __name__ == "__main__":
    main()
