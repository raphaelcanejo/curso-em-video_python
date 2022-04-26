# ESCOPO DE VARIÁVEIS: Escopo é o local onde uma variável vai existir e o local onde a variável não vai mais existir.
# TUDO que está dentro do def, na indentação, só funciona dentro da indentação da função, chamamos isso de ESCOPO LOCAL.
# O que eu declaro dentro do def só funciona dentro do def, se tentar declarar fora do def irá da erro no código

# Uma variável declarada DENTRO do def é uma variável LOCAL. E só funciona dentro do def
# Uma variável declarada FORA do def é uma variável GLOBAL. E funciona tanto dentro como fora do def.

def teste(b):
    global a  
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')