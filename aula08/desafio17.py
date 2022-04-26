# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# import math
from math import hypot
print('Calculadora de hipotenusa de um triângulo')
print('DIGITE APENAS NÚMEROS')
print(25*'-')
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
# hi = math.sqrt(co**2 + ca**2)
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))

