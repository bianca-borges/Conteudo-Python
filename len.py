usuario = input('Digite oseu usuário: ')
qtde_caracteres = len(usuario)

#print(usuario, qtde_caracteres, type(qtde_caracteres))

if qtde_caracteres < 6:
    print('Número de caracteres insuficiente.')
else:
    print('Cadastrado com sucesso.')
