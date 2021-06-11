nome = input('Digite o seu nome: ')

if len(nome) <= 4:
    print('O seu nome é curto.')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')