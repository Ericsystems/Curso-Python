# Crie um programa que leia um numero Real qualque pelo teclado e mostre na tela a sua porção inteira. 
# Ex: Digite um numero: 6.127
# O numero 6127 tem a parte inteira 6.

# from math import trunc
# num = float(input('Digite um numero: '))
# parteinteira = trunc(num)
# print('O numero {} tem a parte inteira {}'.format(num, parteinteira))

num = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(num, int(num)))