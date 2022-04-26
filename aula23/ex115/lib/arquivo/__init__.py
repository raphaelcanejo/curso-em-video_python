from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        # 'rt' é read text
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        # 'wt+' é write text o + faz com que o arquivo seja criado
        a = open(nome, 'wt+')
        a.close()
    except:
        print('House um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        top('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<35}{dados[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        # 'at+' é append text
        a = open(arq, 'at')
    except:
        print('Houve um ERRo na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
