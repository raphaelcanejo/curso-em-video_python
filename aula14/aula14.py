for c in range(1, 11):
    print(c, end=' ',)
print('FIM! ___for___')

        # Nos dois casos tanto com for quanto while, chegamos ao mesmo resultado.
        # não exite comando mais rápido. for e while vão funcionar na mesma velocidade.
        # Quando não conhecemos o limite de repetição é mais indifaco usar while.

        # while -> enquanto

c = 1
while c < 11:
    print(c, end=' ')
    c += 1
print('FIM! ___while___')
print('-=' * 15)

# Outro exemplo com while

n = 1
while n != 0: # Nesse exemplo usamos o que é chamado de condição de parada/ Ponto de parada.
    n = int(input('Digite um valor: '))
print('FIM!')
print('-=' * 15)

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('FIM!')
print('-=' * 15)

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} valores pares e {} valores ímpares'.format(par, impar))
print('FIM!')
print('-=' * 15)

'''
Por enquanto vamos trabalhar com o while dessa forma, está meio gambiarra mais é isso, na próxima aula 
Vamos aprender como imterromper o while.
'''
