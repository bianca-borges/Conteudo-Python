texto = 'Bianca'

for letra in texto:
    print(letra)

print('------------------')

for n in range(5, 20, 2):  # função range(start, stop e step)
    print(n)

print('------------------')

for a in range(100):
    if a % 8 == 0:
        print(a)

print('------------------')

string = 'bianca'
nova_string = ''

for letras in string:
    if letras == 'b':
        nova_string += letras.upper()
    else:
        nova_string += letras

print(nova_string)