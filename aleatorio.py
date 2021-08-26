import random

# gera numero entre a e b
import string

inteiro = random.randint(10, 20)

# gera um float entre a e b
flutuante = random.uniform(10, 20)

# gera um float em 0 e 1
flutuante01 = random.random()

# gera um int com step, funcao range
inteiro02 = random.randrange(900, 1000, 10)

lista = ['Luiz', 'Otavio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
sorteio = random.sample(lista, 2)
# sorteio = random.choice(lista)
# sorteio = random.choices(lista, k=2)

# embaralha a lista
random.shuffle(lista)

# gera senha aletoria

letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*.-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)

print(sorteio)
