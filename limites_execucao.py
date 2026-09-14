from math import factorial, log2

MICROSSEGUNDOS_POR_SEGUNDO = 1_000_000


def maior_n_logaritmico(tempo: float) -> int:
    """Retorna o maior n tal que lg(n) <= tempo."""
    return 2 ** int(tempo)


def maior_n_linear(tempo: int) -> int:
    """Retorna o maior n tal que n <= tempo."""
    return tempo


def maior_n_quadratico(tempo: float) -> int:
    """Retorna uma aproximação do maior n tal que n² <= tempo."""
    return int(tempo**0.5)


def maior_n_cubico(tempo: float) -> int:
    """Retorna uma aproximação do maior n tal que n³ <= tempo."""
    return int(tempo ** (1 / 3))


def maior_n_nlogn(tempo: int) -> int:
    """Encontra por busca o maior n cujo n lg(n) não ultrapassa o tempo."""
    if tempo < 2:
        return 1

    esquerda, direita = 1, tempo

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        custo = meio * log2(meio)

        if custo <= tempo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return direita


def main() -> None:
    try:
        segundos = float(input("Digite o tempo disponível em segundos: "))
    except ValueError:
        print("Erro: informe um valor numérico válido.")
        return

    if segundos <= 0:
        print("Erro: o tempo deve ser maior que zero.")
        return

    tempo_us = segundos * MICROSSEGUNDOS_POR_SEGUNDO

    print(f"\nTempo disponível: {tempo_us:.0f} microssegundos\n")
    print(f"lg n   -> n ≈ 2^{int(tempo_us):d} (representação compacta)")
    print(f"sqrt n -> n = {maior_n_quadratico(tempo_us):,}")
    print(f"n      -> n = {int(tempo_us):,}")
    print(f"n lg n -> n = {maior_n_nlogn(int(tempo_us)):,}")
    print(f"n²     -> n = {maior_n_quadratico(tempo_us):,}")
    print(f"n³     -> n = {maior_n_cubico(tempo_us):,}")

    # Para funções de crescimento muito rápido, evitamos calcular 2^n ou n!
    # com valores de n que tornariam a saída impraticável.
    if tempo_us < 1024:
        n_2n = int(log2(tempo_us)) if tempo_us >= 1 else 0
        n_fatorial = 1
        while factorial(n_fatorial) <= tempo_us:
            n_fatorial += 1
        n_fatorial -= 1
        print(f"2^n    -> n = {n_2n}")
        print(f"n!     -> n = {n_fatorial}")
    else:
        print("2^n    -> omitido para evitar uma busca desnecessariamente grande")
        print("n!     -> omitido para evitar uma busca desnecessariamente grande")


if __name__ == "__main__":
    main()
