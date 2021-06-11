"""
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

#  Lê tudo de uma vez
file.seek(0, 0)
print('Lendo linhas: ')
print(file.read())
print('-----------------')

#  Lê linha por linha
file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('-----------------')

#  Transforma em lista
file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')
file.close()
"""

#  melhor maneira de se trabalhar

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print(file.read())
file.close()

with open('abc.txt', 'a+') as file:  #  Adiciona outras linhas a+
    file.write('Outra linha')
    file.seek(0)
    print(file.read())