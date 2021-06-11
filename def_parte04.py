variavel = 'valor'  # var global

def func():
    outra_variavel = 'valor'  # var local
    return outra_variavel

def func2(args):
    print(args)  # para acessar a var de outra def

var = func()
func2(var)