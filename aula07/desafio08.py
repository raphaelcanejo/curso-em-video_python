# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

print('=====CONVERSOR DE MEDIDAS (m para cm e mm)=====')
m = float(input('Digite a medida em metros: '))
cm = m*100
mm = m*1000
print('O valor de {} em centimetros é {} cm e em milímetros é {} mm.'.format(m, cm, mm))