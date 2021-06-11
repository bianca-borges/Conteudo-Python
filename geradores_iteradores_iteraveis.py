
import time
import sys

# iteravel e iterador ao mesmo tempo
"""
lista = [0,1,2,3,4,5]
lista = iter(lista)  #iterador

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
"""

# gerador
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)
g = gera()

for v in g:
    print(v)

print()

l1 = [x for x in range(100)]  # lista
l2 = (x for x in range(100))  # gerador
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))