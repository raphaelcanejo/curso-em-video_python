# Crie um progama que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas;
# -> O nome com todas as letras minúsculas;
# -> Quantas letras tem o nome completo (sem considerar espaços);
# -> Quantas letras tem o primeiro nome.

print('--------------ANALISADOR DE NOMES--------------')
nome = str(input('Digite seu nome completo: ')).strip()
print('-> Seu nome com letras maiúsculas é {}'.format(nome.upper()))
print('-> Seu nome com letras minúsculas é {}'.format(nome.lower()))
print('-> Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

# print('-> Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))