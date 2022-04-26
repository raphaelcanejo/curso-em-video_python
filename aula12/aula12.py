        # elif -> senão se

nome = str(input('Qual o seu nome? '))
if nome == 'Raphael':
    print('Que nome bonito!')
elif nome == 'Ana Caroline' or nome == 'Miguel' or nome == 'Daniella' or nome == 'Paulo':
    print('Seu nome é bem comum')
elif nome in 'Demar Derozan Rosana Jaider':
    print('Seu nome é bem popular')
else:
    print('Que nome diferente.')
print('Tenha um bom dia, {}'.format(nome))