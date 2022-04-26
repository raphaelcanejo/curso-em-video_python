# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
print(40*'-')
print('Sorteio de que aluno vai limpar o quadro')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]    # para o Python os elementos de uma lista devem ficar entre colchetes.]
escolhido = choice(lista)   # vai escolher randomicamente um dos nomes dentro da lista.
print('O aluno escolhido para limpar o quadro é {}'.format(escolhido))

