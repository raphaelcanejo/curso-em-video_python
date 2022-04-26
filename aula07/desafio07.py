# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('=======BOLETIM ESCOLAR=======')
pbim = float(input('Digite a nota do 1º Bimestre: '))
sbim = float(input('Digite a nota do 2º Bimestre:'))
tbim = float(input('Digite a nota do 3º Bimestre: '))
qbim = float(input('Digite a nota do 4º Bimestre: '))
m = (pbim + sbim + tbim + qbim)/4
print('Sua média é {:.3}.'.format(m))

