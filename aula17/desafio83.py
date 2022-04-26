# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite uma expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()  # Remove o último elemento da lista
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão ESTÁ válida')
else:
    print('Sua expressão NÃO é válida')

# Cada vez que eu completo um par de parêmteses '()' a função pop() remove os parênteses deixando a lista vazia
# É sabendo se a lista tá vazia ou com caracteres que vou saber se tem parênteses sobrando,
# pois seu náo tiver o par '()' o algoritmo identifica o parênteses sozinho e desvalida a expressão.
