# Um try pode ter vários blocos de except para tratar vários tipos de erros e mostrá-los para o usuário de forma clara.
# as possibilidades são infinitas.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por ZERO!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os valores.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! muito obrigado!')
