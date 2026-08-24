# Crie um programa que leia um numero inteiro qualquer e leia na tela se ele é PAR ou IMPAR.

from random import randint
numero = randint(1,10)
print(numero)
if numero % 2 == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é ÍMPAR'.format(numero))