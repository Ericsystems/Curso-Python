# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite um numero: '))

x2 = numero * 2
x3 = numero * 3
x4 = numero * 4
x5 = numero * 5
x6 = numero * 6
x7 = numero * 7
x8 = numero * 8
x9 = numero * 9
x10 = numero * 10

#print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(numero, numero, numero, x2, numero, x3, numero, x4, numero, x5, numero, x6, numero, x7, numero, x8, numero, x9, numero, x10))
print('-' * 12)
print('{}  x  1 = {:2}'.format(numero, numero))
print('{}  x  2 = {:2}'.format(numero, x2))
print('{}  x  3 = {:2}'.format(numero, x3))
print('{}  x  4 = {:2}'.format(numero, x4))
print('{}  x  5 = {:2}'.format(numero, x5))
print('{}  x  6 = {:2}'.format(numero, x6))
print('{}  x  7 = {:2}'.format(numero, x7))
print('{}  x  8 = {:2}'.format(numero, x8))
print('{}  x  9 = {:2}'.format(numero, x9))
print('{}  x 10 = {:2}'.format(numero, x10))
print('-' * 12)