# crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo:
# Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer {}'.format(nome))
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n) - 1]))