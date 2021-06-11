def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_clientes1 = ['Fabrício']
clientes1 = lista_de_clientes(['Bianca', 'Maria', 'André'], lista_clientes1)
clientes2 = lista_de_clientes(['Juca', 'Suely', 'Marcos'])
clientes3 = lista_de_clientes(['Joana', 'Lidia', 'José'])

print(clientes1)
print(clientes2)
print(clientes3)
