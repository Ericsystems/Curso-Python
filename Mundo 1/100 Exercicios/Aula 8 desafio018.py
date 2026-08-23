#Faça um programa que leia um angulo qualquer e mostre o valor do seno, cosseno e tangente desse angulo.

import math
angulo = float(input('Digite o angulo: '))
radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print('Para o angulo de {} Graus, os valores do seno, cosseno e tangente sao:\n Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}'.format(angulo, seno, cosseno, tangente))