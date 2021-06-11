import copy

d1 = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
d1['nova_chave'] = 'novo_valor'

print(d1)

print()

d2 = {
    'chave1': 'string',
    'chave2': 'Inteiro',
    'chave3': 'Tupla'
}

# del d2['str']  deletar chave
d2.update({'nova_chave': 'novo_valor'})  # adicionar chave
if d2.get('nova_chave') is not None:
    print(d2.get('nova_chave'))

print(d2)
print(123)
print()

print('str' in d2.keys())  # checa a existencia da chave
print('valor' in d2.values())  # checa a existencia dos valores da chave
print()

print(len(d2))  # mostra a quantidade de pares
print()

# iterando sobre o dicionário
for v in d2.values():  # para mostrar os valores
    print(v)
print()
for k in d2.keys():  # para mostrar as chaves
    print(k)
print()
for k in d2.items():  # para mostrar os dois
    print(k)
print()
for k in d2.items():
    print(k[0], k[1])  #valores separados por indice
print()
for k, v in d2.items():  # para mostrar os dois
    print(k, v)  #valores separados com variaveis independentes
print()
print()

# criar um dicionario dentro de um dicionario

clientes = {
    'cliente1': {
        'nome': 'Bianca',
        'sobrenome': 'Borges'
    },
    'cliente2': {
        'nome': 'André',
        'sobrenome': 'do Vale'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
print()
print()

# copiando os valores de um dicionario para uma variavel independente
# import copy

d3 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Bianca', 'Borges']}
v = copy.deepcopy(d3)

v[1] = 'Maria'
v['d'][0] = 'Custódio'

print(d3)
print(v)

# update para concatenar dicionarios d1.update(d2)
