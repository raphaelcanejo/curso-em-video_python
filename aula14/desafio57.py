# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0] # vai jogar pra maiúsculo, tirar espaços antes e depois e pegar só a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ')).strip().upper()[0]
print('sexo {} Registrado com sucesso'.format(sexo))