from math import log10

MICROSEGUNDOS_POR_DIA = 24 * 60 * 60 * 1_000_000


def main() -> None:
    """Calcula a ordem de grandeza de n para um algoritmo lg(n)."""
    try:
        dias = float(input("Digite a quantidade de dias: "))
    except ValueError:
        print("Erro: informe um número válido de dias.")
        return

    if dias < 0:
        print("Erro: a quantidade de dias não pode ser negativa.")
        return

    # O exercício considera o tempo de execução em microssegundos.
    tempo_us = dias * MICROSEGUNDOS_POR_DIA

    # Para lg(n) <= t, temos n <= 2^t.
    # Em valores muito grandes, evitamos construir 2^t diretamente.
    log10_n = tempo_us * log10(2)

    print(f"\nTempo disponível: {tempo_us:.0f} microssegundos")
    print("Para lg(n) <= t, temos n <= 2^t.")
    print(f"\nlog10(n) ≈ {log10_n:.3e}")
    print(f"n ≈ 10^({log10_n:.3e})")


if __name__ == "__main__":
    main()
