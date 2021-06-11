def func(*args, **kwargs):  # args serve para qnd não se sabe a qtde de parametros
    print(args)

    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não informada.')

lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Bianca',sobrenome= 'Borges', idade=21)