# Dessa forma nós tiramos as funções criadas do código principal, criamos módulos,
# colocando as funções criadas em outro arquivo.py, o que vai deixar o código mais legível e organizado.
# Nesse exemplo a quantidade de funções e o código em si, é pequeno,
# mas para códigos/ projetos muito grandes esse conceito de modularização é importantíssimo.

# Para o Python qualquer arquivo.py pode ser um módulo, contando que ele tenha funções.

import modulos_aula22
# from modulos_aula22 import fatorial, dobro ->> Se eu quiser importar só aulas funções do módulo ai na hora de usar no código
# não preciso digitar modulos_aula22.fatorial(num), é só digitar fatorial(num)

# A forma  de importar módulos from modulos_aula22 import fatorial, dobro, não é tão recomendada, pois pode conter conflitos.
# Se tiver uma outra biblioteca que contenha a função dobro, o Python vai ficar meio confuso, para saber qual o dobro ele irá calcular.
# Para o Python o que vai valer é a última biblioteca importada, mas para evitar problemas de incompatibilidades é melhor evitar importar usando o from em casos assim.

num = int(input('Digite um número: '))
fat = modulos_aula22.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {modulos_aula22.dobro(num)}.')
print(f'O triplo de {num} é {modulos_aula22.triplo(num)}')
