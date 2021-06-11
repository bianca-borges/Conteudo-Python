def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

dividir = divisao(8,0)
if dividir:
    print(dividir)
else:
    print('Conta inválida.')

print()

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('Não são iguais')