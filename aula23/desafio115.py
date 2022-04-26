# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema sóp vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa',
                    'Sair do Sistema'])

    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        top('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        top('Saindo do sistema...')
        sleep(2)
        break
    else:
        # Digitou uma opção errada no menu
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
