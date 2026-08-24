# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.

# a soma de 2 lados tem que ser maior que o terceiro lado para ser considerado um triangulo, isso para todos os lados.
lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print('Pode formar um TRIANGULO!')
else:
    print('Não pode formar um TRIANGULO')
