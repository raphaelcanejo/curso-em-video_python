# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

random.seed(5)
# O método random.seed() é utilizado
# para definir o número inicial inteiro que servirá como base para a geração de números flutuantes aleatórios.
# Portanto, ao definirmos um valor para seed(),
# dizemos ao compilador que os números aleatórios serão gerados com base no valor informado.
# Se não informarmos nenhum valor, o número utilizado como semente será o horário atual do sistema.

num = random.getstate()
# O método random.getstate() é utilizado para armazenar o estado corrente da sequência de números aleatórios
# gerados para serem usados em outro momento pelo programa.
# Por isso, o ideal é armazenar o valor retornado em uma variável,
# pois ela será acessada pela função random.setstate(), de que falaremos próximo tópico.

cont = int(input('Escolha um valor e irei sortear 5 entre esses: '))
resp = random.sample(range(cont), k=5)  # Retorna uma LISTA
print(f'Os valores sorteados são  {resp}')
# A função random.sample() retorna um determinado trecho de uma sequência. Sua sintaxe é:
# random.sample(sequence, k)
# sequence: representa uma sequência que pode ser uma lista, uma tupla, um range etc.;
# k: indica a quantidade de itens retornados.

print(f'O menor valor gerado é {min(resp)}')
print(f'O maior valor gerado é {max(resp)}')
