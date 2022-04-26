try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:   # Esse comando faz com que mostre qual foi o erro para o usuário.
    print(f'Problema encontrado foi {erro.__class__}')  # Existe diversos timos de erro que podem ser exibidos, só escolher.
    # Não sou obrigado a mostrar esse erro para o usuário, nem devemos, com esse código podemos tratar esse erro e exibir para o usuário de outra forma.
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! muito obrigado!')
