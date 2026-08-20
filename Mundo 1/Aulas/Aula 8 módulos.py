# Hora de aprender como extender a linguagem, como colocar mais funcionalidades no programa, muito alem do que vem de fabrica com a linguagem.

# Fase 8, aprendendo a trabalhar com Módulos

# Modulos
# Pacotes
# Conjunto de funções

# O comando 'Import' é usado para importar módulos, pacotes e funções para dentro do programa.
# Ao usar o comando Import voce importa todas as funçoes ou variaveis de um determinado módulo, pacote ou função.
# EX: import bebida 
# (ficticio, mas em teoria traria todas as bebidas cadastradas no módulo bebida para dentro do programa) 
# Esse import é mais generalista, traria todas as funçoes para dentro do programa.

# Supondo que eu nao queira importar todas as bebidas, mas apenas a cerveja, eu poderia fazer o seguinte:
# EX: from bebida import cerveja 
# (ficticio, mas em teoria traria apenas a cerveja cadastrada no módulo bebida para dentro do programa) 
# Essa função é mais especifica, usada quando quero importar apenas uma função ou variavel especifica de um módulo, pacote ou função.

# Uma bibliotefca que vem preinstalada no python é a biblioteca 'math', que significa matemática, e ela contem varias funções matemáticas que diferentes das aprendidas na aula 7, que podem ser muito uteis se usadas em alguns programas.
# import math   (ao usar esse comando, irá importat todas as funções matemáticas da biblioteca math para dentro do programa, abaixo alguns exemplos de funções matemáticas que podem ser usadas:)
#    ceil = math.ceil(5.1) # Arredonda para cima (resultado é 6)
#    floor = math.floor(5.9) # Arredonda para baixo (resultado é 5)
#    trunc = math.trunc(5.9) # Remove a parte decimal sem fazer arredondamento (resultado é 5)
#    pow = math.pow(5, 2) # Calcula a potência (resultado é 25)
#    sqrt = math.sqrt(25) # Calcula a raiz quadrada (resultado é 5)
#    factorial = math.factorial(5) # Calcula o fatorial (resultado é 120)

# PRATICA
# from math import sqrt, trunc
# num = int(input('Digite um numero: '))

# raizq = sqrt(num)
# print('A raiz de {} é {}'.format(num, trunc(raizq)))
# Ao importar somente a funcionalidade do modulo, voce nao precisa chamar o nome do modulo para chamar a funcionalidade, chamar somente a funcionalidade ja retorna a resposta, porém se voce chamar o modulo completo voce precisa especificar que aquela função é de tal modulo, ex:
#-----------------------
# import math
# num = int(input('Digite um numero: '))

# raizq = math.sqrt(num)

# print('A raiz de {} é {}'.format(num, math.trunc(raizq)))
# Repare que aqui voce precisa do nome do modulo para chamar a função.

# Python.org/docs/(ache a versão do python instalado)/Library reference/na biblioteca 9 voce encontra todos os dados sobre os modulos matematicos.

# Biblioteca Random
# import random #(gera numeros aleatorios)

# num = random.random()
    # a função random do modulo random gera um numero real aleatorio entre 0 e 1, incluindo o 0, excluindo o 1
# num2 = random.randint(1,10)
    # a função randint do modulo random gera um numero inteiro entre os 2 parametros passados (inicio, fim) incluindo os dois numeros citados no inicio e fim
# print('{}\n{}'.format(num, num2))
# import (ctrl + espaço) mostra a lista de modulos preinstalados no python

# Instale bibliotecas que voce nao tem usando o seguinte codigo no terminal:
# python -m pip install (no caso usei python -m pip install emoji para instalar a biblioteca de emojis como exemplo abaixo)

import emoji

print(emoji.emojize('Python é legal :snake:'))