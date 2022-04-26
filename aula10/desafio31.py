# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando
# R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.

dis = float(input('Quantos Km tem a viagem? '))
print('Você está prestes a começar uma viagem de {:.0f}Km!'.format(dis))
if dis <= 200:
    vc = 0.50 * dis
    print('O preço da passagem é R${:.2f}!'.format(vc))
else:
    vl = 0.45 * dis
    print('O preço da passagem é R${:.2f}!'.format(vl))
