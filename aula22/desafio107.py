# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# como os módulos estão na mesma pasta do desafio não precisa especificar a pasta
import modulos_desafio107

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é R${modulos_desafio107.metade(p)}')
print(f'O dobro de {p} é R${modulos_desafio107.dobro(p)}')
print(f'Aumentado 10%, temos R${modulos_desafio107.aumentar(p, 10)}')
print(f'Diminuinto 10%, temos R${modulos_desafio107.diminuir(p, 10)}')
