"""
Problema 1-1: Comparação entre tempos de execução

Para cada função f(n) e cada tempo t na tabela a seguir, determine o
maior tamanho n de um problema que pode ser resolvido no tempo t,
considerando que o algoritmo para resolver o problema demore f(n)
microssegundos.

                1 segundo  1 minuto  1 hora  1 dia  1 mês  1 ano  1 século
    lg n
    sqrt(n)
    n
    n lg n
    n^2
    n^3
    2^n
    n!

Observação: para f(n) = lg n, o maior n é 2**t_us, um número
astronomicamente grande (o expoente já é da ordem de 10^6 a 10^15). Por
isso o resultado é apresentado em notação "2^expoente" e também em
notação científica aproximada (via logaritmo), sem tentar construir o
inteiro exato, o que seria computacionalmente inviável.
"""

from math import factorial, log2, log10

TEMPOS_EM_SEGUNDOS: dict[str, float] = {
    "1 segundo": 1,
    "1 minuto": 60,
    "1 hora": 60 * 60,
    "1 dia": 24 * 60 * 60,
    "1 mês": 30 * 24 * 60 * 60,
    "1 ano": 365 * 24 * 60 * 60,
    "1 século": 100 * 365 * 24 * 60 * 60,
}


def formatar_inteiro(valor: int) -> str:
    """Formata um inteiro "normal" com separador de milhar."""
    return f"{valor:,}".replace(",", ".")


def formatar_potencia_de_2(expoente: float) -> str:
    """Representa 2**expoente sem construir o inteiro exato (que teria
    bilhões de dígitos para expoentes grandes), usando log10 para obter
    a notação científica aproximada."""
    expoente_int = int(expoente)
    log10_valor = expoente * log10(2)
    parte_inteira = int(log10_valor)
    mantissa = 10 ** (log10_valor - parte_inteira)
    return f"2^{expoente_int} (≈ {mantissa:.3f}e+{parte_inteira})"


def calc_lg(t_us: float) -> str:
    """Maior n tal que lg(n) <= t_us  =>  n <= 2**t_us."""
    return formatar_potencia_de_2(t_us)


def calc_sqrt(t_us: float) -> str:
    """Maior n tal que sqrt(n) <= t_us  =>  n <= t_us**2."""
    return formatar_inteiro(int(t_us**2))


def calc_linear(t_us: float) -> str:
    """Maior n tal que n <= t_us."""
    return formatar_inteiro(int(t_us))


def calc_nlogn(t_us: float) -> str:
    """Maior n tal que n * lg(n) <= t_us, encontrado por busca binária."""
    if t_us < 2:
        return formatar_inteiro(1)

    esquerda, direita = 1, int(t_us)
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if meio * log2(meio) <= t_us:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return formatar_inteiro(direita)


def calc_quadratico(t_us: float) -> str:
    """Maior n tal que n^2 <= t_us."""
    return formatar_inteiro(int(t_us**0.5))


def calc_cubico(t_us: float) -> str:
    """Maior n tal que n^3 <= t_us."""
    return formatar_inteiro(int(t_us ** (1 / 3)))


def calc_exponencial(t_us: float) -> str:
    """Maior n tal que 2^n <= t_us  =>  n <= lg(t_us)."""
    if t_us < 1:
        return formatar_inteiro(0)
    return formatar_inteiro(int(log2(t_us)))


def calc_fatorial(t_us: float) -> str:
    """Maior n tal que n! <= t_us, encontrado por busca linear crescente."""
    n = 1
    while factorial(n + 1) <= t_us:
        n += 1
    return formatar_inteiro(n)


FUNCOES = [
    ("lg n", calc_lg),
    ("sqrt(n)", calc_sqrt),
    ("n", calc_linear),
    ("n lg n", calc_nlogn),
    ("n^2", calc_quadratico),
    ("n^3", calc_cubico),
    ("2^n", calc_exponencial),
    ("n!", calc_fatorial),
]


def main() -> None:
    print("Problema 1-1: Comparação entre tempos de execução\n")
    print(
        "Maior tamanho de entrada n resolvível em cada tempo, considerando\n"
        "que o algoritmo demora f(n) microssegundos:\n"
    )

    colunas = list(TEMPOS_EM_SEGUNDOS.keys())

    for coluna in colunas:
        print(f"\n=== {coluna} ===")
        t_us = TEMPOS_EM_SEGUNDOS[coluna] * 1_000_000
        for nome, funcao in FUNCOES:
            print(f"  {nome:<8} -> n = {funcao(t_us)}")


if __name__ == "__main__":
    main()
