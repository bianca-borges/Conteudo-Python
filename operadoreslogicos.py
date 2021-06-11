# and, or, not,in e not in

"""
a = 2
b = 3

if not b > a:  # o operador not inverte a expressão
    print('B é maior do que A.')
else:
    print('B não é maior do que A.')
"""

"""
nome = 'Bianca'

if 'a' in nome:
    print('Existe a letra A no seu nome.')
"""

nome = input('Nome de usuário: ')
senha = input('Informe a sua senha: ')

usuario_bd = 'bianca'
senha_bd = '123456'

if usuario_bd == nome and senha_bd == senha:
    print('Você foi logado com sucesso.')
else:
    print('Senha ou usuário inválidos.')

