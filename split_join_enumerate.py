# Split -> dividir uma string
# Join -> juntar uma string
# Enumerate -> enumerar elementos de uma lista

string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)
print()

palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes foi {palavra}')
print()

string_2 = 'O Brasil é penta'
lista_3 = string_2.split(' ')
string_3 = ','.join(lista_3)

print(string_3)
print()

string_4 = 'O Brasil é penta'
lista_4 = string_4.split(' ')

for indice, valor in enumerate(lista_4):
    print(indice, valor)