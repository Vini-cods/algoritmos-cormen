# Algoritmos - Cormen

Repositório de estudos e exercícios da disciplina de **Algoritmos**, utilizando como referência o livro *Algoritmos: Teoria e Prática*, de Thomas H. Cormen et al.

O objetivo deste repositório é registrar a evolução dos exercícios, implementações e anotações desenvolvidas durante a disciplina.

## Conteúdo

- **`lgn.py`** - exercício relacionado à comparação de tempos de execução para a função `lg n`.
- **`01 - Algoritmos.pdf`** - material de referência utilizado na aula, quando autorizado para compartilhamento.
- **`Resumo.pptx`** - material complementar da disciplina, quando autorizado para compartilhamento.

## Sobre o exercício `lg n`

No capítulo inicial, o Cormen utiliza a função `lg n` (logaritmo na base 2) para analisar o crescimento do tempo de execução de algoritmos. Em problemas desse tipo, o tempo disponível pode ser convertido para a unidade adotada no exercício e, a partir da relação

```text
lg n <= t
```

obtemos:

```text
n <= 2^t
```

O programa `lgn.py` recebe uma quantidade de dias, converte o tempo para microssegundos e calcula a ordem de grandeza do maior `n` que poderia ser processado por um algoritmo cujo tempo de execução fosse `lg n` microssegundos.

Como esse valor pode ser astronomicamente grande, o programa não tenta armazenar ou imprimir `2^t` por extenso. Em vez disso, apresenta uma aproximação em notação científica por meio de `log10(n)`.

## Execução

Requisitos:

- Python 3.10+

Execute:

```bash
python lgn.py
```

Exemplo para 1 dia:

```text
Digite a quantidade de dias: 1

Tempo disponível: 86400000000 microssegundos
Para lg(n) <= t, temos n <= 2^t.

log10(n) ≈ 2.600e+10
n ≈ 10^(2.600e+10)
```

## Referência

CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L.; STEIN, Clifford. *Algoritmos: Teoria e Prática*.
