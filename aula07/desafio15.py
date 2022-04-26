# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Locação de carros')
d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros foi rodado? '))
pagar = (d * 60) + (km * 0.15)
print('você deve pagar R${:.2f}'.format(pagar))

