"""
minha_string = 'Bianca do Vale Borges'
tamanho_string = len(minha_string)


c = 0
nova_string = ''

while c < tamanho_string:
    if minha_string[c] == 'a':
        nova_string += minha_string[c].upper()
    else:
        nova_string += minha_string[c]
    c += 1
print(nova_string)
"""


while True:
    minha_string = input('Informe o seu nome completo: ')
    tamanho_string = len(minha_string)
    c = 0
    contagem_atual = 0
    letra = ''

    while c < tamanho_string:
        qtde_letras = minha_string.count(minha_string[c])

        if contagem_atual < qtde_letras and minha_string[c].strip():
            letra = minha_string[c]
            contagem_atual = qtde_letras
        c += 1
    print(letra, contagem_atual)