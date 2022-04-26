# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# >>>>> Função <<<<<
def voto(ano):
    """vai dizer quem pode votar ou não.

    Args:
        ano (int): Ano de nascimento da pessoa

    Returns:
        str: Escreve na tela se o voto é obrigatório, opcional ou  não vota
    """
    from datetime import date

    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal
print(voto(1995))
help(voto)
