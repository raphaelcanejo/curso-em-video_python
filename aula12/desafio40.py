# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('1° NOTA: '))
n2 = float(input('2° NOTA: '))
n3 = float(input('3° NOTA: '))
m = (n1 + n2 + n3) / 3
print('-=' * 15)
print('Sua média foi {:.2f}'.format(m))
print('-=' * 15)
if m < 5:
    print('REPROVADO! Estude mais da próxima vez.')
elif 7 > m >= 5:
    print('Você está de RECUPERAÇÃO.')
elif m >= 7:
    print('APROVADO! Parabéns, você é um nerd.')