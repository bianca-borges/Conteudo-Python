# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois testes)
# difference - (elementos presentes ao set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.discard(2)
s1.update('Python')

print(s1)
print()
# set para remover elementos duplicados de uma lista

l1 = [1,2,2,2,3,4,5,5,5,6,6,6,6,'Bianca','Bianca']
l1 = set(l1)
l1 = list(l1)
print(l1)
print()

# union
s2 = {1,2,3,4,5}
s3 = {1,2,3,4,5,6}
s4 = s2 | s3
print(s4)
print()

# intersection
s5 = {1,2,3,4,5}
s6 = {1,2,3,4,5,6}
s7 = s5 & s6
print(s7)
print()

# difference
s8 = {1,2,3,4,5,7}
s9 = {1,2,3,4,5,6}
s10 = s8 - s9
print(s10)
print()

# symmetric_difference
s11 = {1,2,3,4,5,7}
s12 = {1,2,3,4,5,6}
s13 = s11 ^ s12
print(s13)
print()

# comparando listas

l2 = ['Bianca', 'André', 'Maria']
l3 = ['Bianca', 'Bianca', 'Bianca', 'André', 'Maria', 'André']

if set(l2) == set(l3):
    print('As listas são iguais.')
else:
    print('As listas não são iguais.')