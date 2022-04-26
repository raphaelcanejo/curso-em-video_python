# Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
d = 2 * num
t = 3 * num
r = num ** (1/2)
print('O dobro de {} é {}, o triplo é {}, e a raiz quadrada é {:.2f}.'.format(num, d, t, r))

# {:.2f} esse comando significa duas casas decimais flutuantes, ou seja, depois do ponto.

