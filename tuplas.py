# mudar valor numa tupla
t1 = (1, 2, 3, 'Bianca', 5, 6)
t1 = list(t1)
t1[3] = 4
t1 = tuple(t1)

print(t1)

print()

# concatenando tuplas
t2 = (1,2,3,4,5)
t3 = (6,7,8,9,10)
t4 = t2 + t3

n1, n2, n3, *_ = t4  # desempacotar 

print(n3)
print(t4)