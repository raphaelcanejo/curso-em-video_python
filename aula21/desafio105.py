# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*n, sit=False):
    """Recebe várias notas e diz a situação

    Args:
        sit (bool, optional): Retorna a situação da pessoa
        média >= 7: BOA
        média >= 5: RAZOÁVEL
        média < 5: RUIM

    Returns:
        Dict: Retorna um dicionário com todas as informações.
    """
    r = {}

    r['total_notas'] = len(n)
    r['maior_nota'] = max(n)
    r['menor_nota'] = min(n)
    r['média'] = sum(n) / len(n)

    if sit:  # Se sit for igual a True, ou seja, sit=True
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# >>>>> Programa Principal <<<<<
print('-=' * 30)
resp = notas(5.5, 7.3, 8.2, 4.2, sit=True)
print(resp)

print('-=' * 30)
perg = notas(8, 5, 7, 6)    # ou notas(8, 5, 7, 6, sit=False) dá no mesmo
print(perg)
