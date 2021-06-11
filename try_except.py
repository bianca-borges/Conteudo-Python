try:
    a = 0
except NameError as erro:
    print('Erro do desenvolvedor.')
except (IndexError, KeyError) as erro:
    print('Ocorreu um erro no índice ou na chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally:
    a = 'valor'
print(a)