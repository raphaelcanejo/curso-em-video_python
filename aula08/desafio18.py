# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = float(input('Digite algum ângulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O ângulo {} tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}.'.format(ang, seno, cosseno, tangente))

