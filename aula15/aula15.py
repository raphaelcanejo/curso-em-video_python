#                   Interromper Repetições while

n = s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break           # O comando break interrompe o looping de repetição.
                        # True faz com que aconteça um looping infinito que só vai parar com o comando Break
    s += n
    cont += 1
print(f'Você digitou {cont:.2f} valores e a soma entre eles vale {s:.2f}.') # aqui aprendemos o uso das fstrings.
            # As fstrings usam um conceito que chama-se interpolação de string.
            # colocamos as variáveis já dentro dos {} para aparecer o resultado para o usuário.
