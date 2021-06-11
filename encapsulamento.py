"""
_ -> protected
__ -> private
"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    # permite acesso aos dados
    @property
    def dados(self):
        return self.__dados

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_clientes(1, 'Bianca')
bd.inserir_clientes(2, 'André')
bd.inserir_clientes(3, 'Nataly')
print(bd.dados)
# print(bd._BaseDeDados__dados)  # acessar dados diretamente
# bd.lista_clientes()