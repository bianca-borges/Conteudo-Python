from dados import produtos, pessoas, lista

nova_lista = filter(lambda p: p['preço'] > 50, produtos)

for produto in nova_lista:
    print(produto)

print()

def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista1 = filter(filtra, pessoas)

for p in nova_lista1:
    print(p)