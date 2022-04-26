# Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no intervalo entre 1 a 50.

print('-=' * 10)
for c in range(2, 51, 2): # Com o código desse jeito o programa cria menos laços de interação, usando menos memória.
    print(c, end=' ')
print('FIM!')

'''
for c in range(1, 51):
    if c % 2 == 0
        print(c, end=' ')
print('FIM!')
'''
