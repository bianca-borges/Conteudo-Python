from itertools import groupby, tee

alunos = [
    {'nome': 'Bianca', 'nota': 'A'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Lucas', 'nota': 'D'},
    {'nome': 'Nataly', 'nota': 'B'},
    {'nome': 'Diogo', 'nota': 'F'},
    {'nome': 'José', 'nota': 'E'},
    {'nome': 'Henrique', 'nota': 'E'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Julia', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'C'}
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)  # criar cópias para não esgotar os valores
    print(f'Agrupamento {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'{quantidade} de alunos tiraram {agrupamento}')
  #  for aluno in valores_agrupados:
  #      print(aluno)
    print()