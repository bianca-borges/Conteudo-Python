class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, e não atributo em {name}.')
        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B(A):
    teste = 'Valor'
   # b_fala = 'Olá'
    def b_fala(self):
        print('Olá!')
    def sei_la(self):
        pass

b = B()