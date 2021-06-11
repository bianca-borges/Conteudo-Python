num = input('Digite um número inteiro: ')


if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print('Este número é par.')
    else:
        print('Este número é ímpar.')
else:
    print('Este número não é inteiro')
