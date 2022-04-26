'''Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
Aprenda como usar a estrutura try except no Python de uma forma simples.'''

try:    # tenta executar o programa - OPERAÇÃO
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:  # Se der problema no programa executa esse bloco - FALHOU
    print('Infelizmente tivemos um problema :(')
else:   # - DEU CERTO
    # O r só vai ser "criado" se o programa conseguir receber os dois valores inteiros.
    print(f'O resultado é {r:.1f}')

    # Se não colocar o else depois do bloco do except ao executar o programa receberemos uma mensagem de erro.
    # Se botar o bloco do else o programa será execultado normalmente mesmo se tiver erro,
    # Mais aí será executado o bloco do else.

finally:    # Esse bloco será executado indendente se o programa foi execultado com erros ou sem erros.
    print('Volte sempre! muito obrigado!')
    # Importante mencionar que os comandos else e finally nem sempre serão utilizados, são opcionais.
