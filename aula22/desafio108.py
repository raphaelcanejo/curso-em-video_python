# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

import modulos_desafio108

p = float(input('Digite o preço: R$'))
print(
    f'A metade de {modulos_desafio108.moeda(p)} é {modulos_desafio108.moeda(modulos_desafio108.metade(p))}')
print(
    f'O dobro de {modulos_desafio108.moeda(p)} é {modulos_desafio108.moeda(modulos_desafio108.dobro(p))}')
print(
    f'Aumentado 10%, temos {modulos_desafio108.moeda(modulos_desafio108.aumentar(p, 10))}')
print(
    f'Diminuinto 10%, temos {modulos_desafio108.moeda(modulos_desafio108.diminuir(p, 10))}')

# print(
#     f'A metade de {modulos_desafio108.moeda(p, U$$)} é {modulos_desafio108.moeda(modulos_desafio108.metade(p))}')
