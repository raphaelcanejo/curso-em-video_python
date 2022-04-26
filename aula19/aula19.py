# # dados = {} -> Declarando um Dicionário vazio
# dados = dict()  -> Outra forma de declarar um DICIONÁRIO.

pessoas = {'nome': 'Raphael', 'idade': 26, 'sexo': 'M'}
print(pessoas)
print(pessoas['nome'])
# Como tudo está dentro de aspas simples, na hora de declarar a variável preciso por aspas duplas se não da erro.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())   # ['nome', 'idade', 'sexo']
print(pessoas.values())  # ['Raphael', 26, 'M']
print(pessoas.items())  # [('nome', 'Raphael'), ('idade', 26), ('sexo', 'M')]
#                       Na tela vai mostrar que temos uma LISTA que é composta por três TUPLAS.

print('===' * 20)

for k in pessoas.keys():
    print(k)
print('~~' * 20)
for v in pessoas.values():
    print(v)
print('~~' * 20)
del pessoas['sexo']
# pessoas['nome'] = Canejo -> Se eu quiser trocar o nome que está dentro do dicionário.
# Estou adicionando mais um item dentro do dicionário. Não preciso usar . append() para isso.
pessoas['peso'] = 93.4
for k, v in pessoas.items():
    print(f'{k}: {v}')

print('===' * 20)
