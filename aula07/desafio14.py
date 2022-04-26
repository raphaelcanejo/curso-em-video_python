# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('CONVERSOR DE TEMPERATURA DE Celsius -> Fahrenheit')
c = float(input('Digite o valor da temperatura em ºC: '))
f = c * 1.8 + 32
print('{}Cº corresponde à {}ºF'.format(c, f))