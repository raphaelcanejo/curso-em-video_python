# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import modulos_desafio109

p = float(input('Digite o preço: R$'))
print(
    f'A metade de {modulos_desafio109.moeda(p)} é {modulos_desafio109.metade(p, True)}')
print(
    f'O dobro de {modulos_desafio109.moeda(p)} é {modulos_desafio109.dobro(p, True)}')
print(
    f'Aumentado 10%, temos {modulos_desafio109.aumentar(p, 10, True)}')
print(
    f'Diminuinto 10%, temos {modulos_desafio109.diminuir(p, 10, True)}')

# print(
#     f'A metade de {modulos_desafio108.moeda(p, U$$)} é {modulos_desafio108.moeda(modulos_desafio108.metade(p))}')
