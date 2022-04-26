# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# Os arquivos __init__.py são necessários para que o Python trate diretórios contendo o arquivo como pacotes.
# Isso previne que diretórios com um nome comum, como string, ocultem, involuntariamente, módulos válidos
# que ocorrem posteriormente no caminho de busca do módulo.
# No caso mais simples, __init__.py pode ser apenas um arquivo vazio,
# mas pode também executar código de inicialização do pacote, ou configurar a variável __all__.

from ex111.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)
