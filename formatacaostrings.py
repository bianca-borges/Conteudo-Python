nome = 'Bianca'
idade = 21
altura = 1.62
maior = idade > 18
peso = 55
imc = peso / altura ** 2

print('Nome:', nome)  
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade:', maior)
print(nome, 'tem o seu imc equivalente a:', imc)

print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{} tem {} anos e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu IMC é {im:.2f}'.format(n = nome, i = idade, im = imc))