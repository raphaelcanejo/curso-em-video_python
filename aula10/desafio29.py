# Escreva um programa que leia a velocidade de um caroo.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# a multa vai custar R$7,00 por cada km acima do limite.

vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80 Km/h!')
    mul = (vel - 80) * 7
    print('Você deve pagar um multa de R${:.2f}!'.format(mul))
print('Tenha um bom dia! Dirija com segurança!')