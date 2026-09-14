# Algoritmos — Estudos e Exercícios

Repositório pessoal de estudos, exercícios e implementações desenvolvidos durante a disciplina de **Algoritmos** no curso de Ciência da Computação.

O conteúdo tem como referência principal o livro _Algoritmos: Teoria e Prática_, de Thomas H. Cormen et al., além dos materiais utilizados nas aulas.

> Este repositório registra meu processo de aprendizagem. Os códigos são implementações próprias feitas para estudo e prática.

## Estrutura

| Arquivo                     | Tema                                                   |
| --------------------------- | ------------------------------------------------------ |
| `lgn.py`                    | Função `lg n` e conversão de tempo para microssegundos |
| `comparacao_ordenacao.py`   | Comparação entre `8n²` e `64n lg n`                    |
| `crescimento_algoritmos.py` | Comparação de diferentes funções de crescimento        |
| `limites_execucao.py`       | Tamanho máximo de entrada para diferentes funções      |
| `busca.py`                  | Busca linear e busca binária                           |

A estrutura poderá ser ampliada conforme novos assuntos forem estudados na disciplina.

## Conteúdo estudado

### Funções de crescimento

O material apresenta diferentes ordens de crescimento utilizadas na análise de algoritmos, incluindo:

```text
lg n
√n
n
n lg n
n²
n³
2ⁿ
n!
```

A ideia é observar como algoritmos diferentes podem apresentar comportamentos muito distintos à medida que o tamanho da entrada aumenta.

### Comparação de algoritmos de ordenação

Um dos exemplos compara a ordenação por inserção, com crescimento proporcional a `n²`, com a ordenação por intercalação, com crescimento proporcional a `n lg n`.

No exercício implementado aqui, são utilizados os custos:

```text
Inserção:     8n²
Intercalação: 64n lg n
```

O programa calcula ambos para um valor de `n` informado pelo usuário e indica qual apresenta menor custo para aquela entrada.

### Limites de execução

Também são estudadas situações em que se deseja descobrir qual o maior tamanho de entrada que pode ser processado dentro de determinado tempo, considerando diferentes funções de crescimento.

O programa `limites_execucao.py` transforma o tempo informado em microssegundos e calcula estimativas para funções como `lg n`, `n`, `n lg n`, `n²` e `n³`.

Para funções de crescimento muito rápido, como `2ⁿ` e `n!`, o programa evita cálculos que produziriam valores impraticavelmente grandes.

### Busca

O arquivo `busca.py` implementa duas estratégias básicas:

- **Busca linear:** `O(n)`
- **Busca binária:** `O(log n)`

A busca binária exige que os elementos estejam ordenados.

## Como executar

Requisitos:

- Python 3.10 ou superior

Exemplo:

```bash
python lgn.py
python comparacao_ordenacao.py
python crescimento_algoritmos.py
python limites_execucao.py
python busca.py
```

## Referência

CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L.; STEIN, Clifford. _Algoritmos: Teoria e Prática_.
