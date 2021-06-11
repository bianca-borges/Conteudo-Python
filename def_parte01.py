def funcao(msg='Olá', nome='usuário'):
    nome = nome.replace('a', '3')  # trocar a leta 'a' por '3'
    print(msg, nome)


funcao()
funcao(nome='Bianca', msg='Como vai,')  # invuertendo funçoes
funcao('Oi', 'Bianca')
funcao('Olá', 'André')