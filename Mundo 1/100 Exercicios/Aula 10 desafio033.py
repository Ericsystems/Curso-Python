# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor.

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

if n1 >= n2 and n1 >= n3:
    print('O numero {} é o MAIOR dos digitados.'.format(n1))
elif n2 >= n1 and n2 >= n3:
    print('O numero {} é o MAIOR dos digitados.'.format(n2))
else:
    print('O Numero {} é o MAIOR dos digitados.'.format(n3))

if n1 <= n2 and n1 <= n3:
    print('O numero {} é o MENOR dos digitados.'.format(n1))
elif n2 <= n1 and n2 <= n3:
    print('O numero {} é o MENOR dos digitados.'.format(n2))
else:
    print('O Numero {} é o MENOR dos digitados.'.format(n3))

# Também da pra simplificar usando max() e min() ex:

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print('O NUMERO {} É O MAIOR.'.format(maior))
print('O NUMERO {} É O MENOR.'.format(menor))

#usei a estrutura if else porque a aula é sobre ela.