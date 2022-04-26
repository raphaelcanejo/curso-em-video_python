# Faça um programa que leia um número e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
ant = num - 1
dep = num + 1
print('Antes de {} é {} e depois é {}.'.format(num, ant, dep))

# Se eu  não quiser adicionar novas variáveis o código pode ser dessa forma:

# n = int(input('Digite um número: '))
# print('Antes de {} é {} e depois é {}.'.format(n, (n-1), (n+1)))

# Utilizando só uma variável economiza memória porém se precisar de variáveis com esses valores não terá como usá-la.