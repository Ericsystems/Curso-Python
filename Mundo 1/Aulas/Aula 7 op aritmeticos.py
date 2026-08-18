#====== Aula 7 ======

# Alguns OPERADORES ARITMÉTICOS em python:

# Adição: +
# 5 + 2 == 7

# Subtração: -
# 5 - 2 == 3

# Multiplicação: *
# 5 * 2 == 10
                      
# Divisão: /
# 5 / 2 == 2.5

# Potência: ** ou pow(n1,n2). Retorna o resultado da potenciação ex 5² = 5x5. Se 5**3 entao seria 5³, ou 5x5x5.
# 5 ** 2 == 25

# Divisão inteira: //.  Retorna a parte inteira da divisão.
# 5 // 2 == 2

# Módulo(ou resto da divisão): %. Retorna o resto da divisão.
# 5 % 2 == 1

# A ordem de precedência dos operadores aritméticos é:
# 1. Parênteses
# 2. Potência
# 3. Multiplicação e Divisão, Divisão inteira e Resto da divisão.
# 4. Adição e Subtração

# Para calcular a raiz quadrada de um numero é a mesma coisa que calcular a potencia dele por 0,5 ou seja, 9**(1/2) ou 9**0.5 == 3.0
# Raiz Quadrada
# 81**(1/2) == 9.0

# Raiz cúbica
# 123**(1/3) == 5.0

# Alguns desses operadores aritmeticos tambem podem ser utilizados com strings, como por exemplo a adição e a multiplicação. A adição de strings é chamada de concatenação, ou seja, juntar duas strings em uma só. A multiplicação de strings é chamada de repetição, ou seja, repetir uma string um determinado número de vezes.
# Exemplo:
# Concatenação:
# print('Olá' + ' Mundo!') == 'Olá Mundo!'
# print('Olá' + 21) == 'Olá 21' # O python irá converter o número 21 para string e concatenar com a string 'Olá'

# Repetição:
# print('oi' * 5) == 'oi oi oi oi oi '
# print('=' * 20) == '===================='


#======== ALINHAMENTO DE TEXTO ========

# É possivel alinhar o texto que vai ser exibido no print. print('texto {} texto'.format(variavel)). Para isso, use o caractere de alinhamento dentro das chaves {}.
# Use  :^  para alinhar ao centro.
# Use  :>  para alinhar a direita.
# Use  :<  para alinhar a esquerda.
# Deve ser inserido um numero apos o caractere de alinhamento para definir o tamanho do campo de exibição.
# Se o tamanho do campo de exibição for MAIOR que o tamanho da string, a string será preenchida com espaços em branco.
# Se o tamanho do campo de exibição for MENOR que o tamanho da string, a string será exibida normalmente.
# EX:
# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer, {:>20}!'.format(nome))
# Retorna o nome do usuario alinhado a direita, com um campo de exibição de 20 caracteres.
# também é possivel preencher esse espaço em branco quando existir, ao adicionar um caractere antes do caractere de alinhamento.
# Ex: {:=^20} irá preencher o espaço em branco com o caractere =.
# Pode ser usado qualquer sinal...

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))

soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
divi = n1 / n2
divint = n1 // n2
pot = n1 ** n2
rest = n1 % n2

print('A Soma é {}, subtração é {}, a multiplicação {}, a divisão é {:.3f}'.format(soma, subt, mult, divi), end=' ')
print('a potencia {}, a divisao inteira {} e o resto da divisão é {}'.format(pot, divint, rest))

# Ao adicionar 2 prints irá ocorrer uma quebra de linha, para manter a linha colada voce pode ao final do print adicionar o parametro end=''. recomento colocar um espaço entre as aspas pro texto nao colar um no outro. exemplo acima.

# Da mesma forma é possivel colocar uma quebra de linha dentro do texto do print ao adicionar contra barra + n (\n) no local que deseja quebrar a linha. Exemplo:
print('Soma: {} \nSubtração: {} \nMultiplicação: {} \nDivisão: {:.3f}'.format(soma, subt, mult, divi), end=' ')
print('\nPotencia: {} \nDivisao inteira: {} \nResto da divisão: {}'.format(pot, divint, rest))