"""
combinations, permutations ans product -> itertools
combinação -> ordem não importa
permutação -> ordem importa
ambos não repetem valores únicos
produto -> ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Bianca', 'André', 'Nataly', 'Suely', 'Lorena', 'Cecília']
#  for grupo in combinations(pessoas, 2):
#    print(grupo)

#  for grupo in permutations(pessoas, 2):
#    print(grupo)

for grupo in product(pessoas, repeat=2):
    print(grupo)