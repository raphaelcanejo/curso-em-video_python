# Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores  a R$1250.00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Qual o valor do seu salário? R$'))
if sal <= 1250:
    aumento = sal + (sal*15)/100
    print('Seu novo salário será de R${:.2f}! O aumento foi de 15%'. format(aumento))
else:
    aumento = sal + (sal*10)/100
    print ('Seu novo salário será de R${:.2f}! O aumento foi de 10%'. format(aumento))
