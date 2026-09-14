"""
Exercício 1.1-2

Além da velocidade, que outras medidas de eficiência poderiam ser usadas
em uma configuração real?
"""


def main() -> None:
    print("Exercício 1.1-2\n")
    print("Outras medidas de eficiência relevantes na prática:\n")

    medidas = [
        (
            "Uso de memória (espaço)",
            "quanto de memória RAM ou armazenamento o algoritmo consome, "
            "especialmente crítico em dispositivos com recursos limitados.",
        ),
        (
            "Número de acessos a disco/rede",
            "operações de E/S costumam ser muito mais lentas que operações "
            "em memória, então minimizar acessos a disco ou chamadas de "
            "rede pode importar mais do que o número bruto de instruções.",
        ),
        (
            "Consumo de energia",
            "em dispositivos móveis e data centers, algoritmos mais "
            "eficientes em energia reduzem custos operacionais e aumentam "
            "a autonomia da bateria.",
        ),
        (
            "Uso de largura de banda",
            "em sistemas distribuídos, a quantidade de dados trafegados "
            "pela rede pode ser o gargalo, não o tempo de CPU.",
        ),
        (
            "Escalabilidade / uso de múltiplos núcleos",
            "quão bem o algoritmo se beneficia de paralelismo, importante "
            "em processadores com vários núcleos.",
        ),
        (
            "Simplicidade e manutenibilidade do código",
            "algoritmos mais simples são mais fáceis de depurar, manter e "
            "verificar quanto à correção, o que tem custo humano associado.",
        ),
    ]

    for titulo, descricao in medidas:
        print(f"- {titulo}: {descricao}\n")


if __name__ == "__main__":
    main()
