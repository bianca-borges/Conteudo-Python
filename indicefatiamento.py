"""
Manipulando strings

* String indices
* Fatiamento de strings [inicio:fim:etc..]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

"""
# indice positivo
texto = 'Python S2'
print(texto[2:7])
print(texto[0:6:2])  # pula de 2 em 2
print(texto[-9:-3])  # negativo


#indice negativo
url = 'www.google.com.br/'
print(url[:-1])