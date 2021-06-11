"""
Listas em Python

fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
"""
lista = ['A', 'B', 'C', 'D', 'E', True, 10.2]
lista[3] = 'outro valor'
print(lista[3])
print(lista[0:6:2])  # fatiamento

print('-------------------')

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l1.extend(l2)  # junta outras listas
l1.append('a')  # adicionar novos valores
l2.insert(0, 'bianca')
l3.pop() # remove um valor da lista
del(l4[3:5])  # deleta valores

print(l3)
print(l1)
print(l2)
print(l3)
print(l4)
print(max(l4))  # maior valor da lista
print(min(l4))  # menor valor da lista

print('-------------------')

l5 = list(range(0, 10))  # range para criar uma lista
print(l5)

print('-------------------')

l6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for valor in l6:
     soma += valor
print(soma)

print('-------------------')
"""

secreto = 'perfume'
digitadas = []
chance = 3

while True:
    if chance <= 0:
        print('Game Over!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite somente uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Parabéns! A letra {letra} existe na palavra secreta.')
    else:
        print(f'Quase! A letra {letra} não está presente na palavra secreta.')
        digitadas.pop()  # deleta o ultimo elemente se ele estiver errado

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Parabéns! Você completou a palavra.')
        break
    if letra not in secreto:
        chance -= 1






