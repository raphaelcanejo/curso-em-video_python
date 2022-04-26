# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

print('-=' * 20)
print('CALCULADORA DE IMC')
print('(apenas números)')
print('-=' * 20)
peso = float(input('QUAL O SEU PESO: '))
altura = float(input('QUAL A SUA ALTURA: '))
imc = peso / (altura ** 2)
print('SEU IMC É DE {:.2f}'.format(imc))
print('-=' * 20)
if imc < 18.5:
    print('STATUS: Abaixo do Peso.')
elif 18.5 <= imc <= 24.99:
    print('STATUS: Peso Ideal.')
elif 25 <= imc <= 29.99:
    print('STATUS: Sobrepeso.')
elif 30 <= imc <= 39.99:
    print('STATUS: Obesidade.')
else:
    print('STATUS: Obesidade Mórbida.')