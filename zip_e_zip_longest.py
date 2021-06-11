# zip -> unindo iteráveis
# zip longest -> itertools

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro', 'Manaus']
estados = ['SP', 'MG', 'BA', 'RJ']
cidades_estados = zip(indice, cidades, estados)
for indice, cidades, estados in cidades_estados:
    print(indice, cidades, estados)

print()

cidades1 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro', 'Manaus']
estados1 = ['SP', 'MG', 'BA', 'RJ']
cidades_estados1 = zip_longest(cidades1, estados1, fillvalue='Estado')
print(list(cidades_estados1))