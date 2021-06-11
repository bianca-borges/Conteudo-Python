nome = input('Qual o seu nome? \n')
idade = input('Qual a sua idade? \n')

if int(idade) == 16 and int(idade) < 18:
    print(f'\n{nome}, seu voto é opcional.')
elif 18 <= int(idade) <= 70:
    print(f'\n{nome}, seu voto é obrigatório.')   
elif int(idade) < 16 or int(idade) > 70:
    print(f'\n{nome}, você não pode votar.')
