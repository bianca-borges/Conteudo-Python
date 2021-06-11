from itertools import count

contador = count(start=0, step=2)
for valor in contador:
    print(round(valor, 2))
    if valor >= 10 or valor <= -10:
        break