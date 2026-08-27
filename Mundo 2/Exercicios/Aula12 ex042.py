# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
# EX 35: Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.
#        a soma de 2 lados tem que ser maior que o terceiro lado para ser considerado um triangulo, isso para todos os lados.

lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if (lado1 + lado2) > lado3 and (lado3 + lado2) > lado1 and (lado1 + lado3) > lado2:
    print('Pode ser um triangulo')
    if lado1 == lado2 and lado1 == lado3:
        print('E esse triangulo é Equilátero (onde todos os lados são iguais)')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('E esse triangulo é Isóceles (onde pelomenos dois lados são iguais)')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('E esse triangulo é Escaleno (onde todos os lados sao diferentes)')
else:
    print('Não pode formar um triangulo')