import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# Se quiser arredondar o valor da raiz para cima, só utilizar o seguinte comando:
# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

'''
Quando uso a biblioteca math apenas com o comando import fica da seguinte forma [math.ceil(raiz)] por exemplo,
quando uso o comando from import não precisa utilizar o math.ceil por exemplo, só utiliza o ceil()
'''

# se eu apertar ctrl + espaço depois do math aparece toda a lista de comandos da biblioteca.