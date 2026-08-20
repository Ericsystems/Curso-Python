# Faça um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math
op = float(input('Digite o cumprimento do cateto oposto: '))
adj = float(input('Digite o cumprimento do cateto adjacente: '))

hip = math.sqrt(pow(op, 2) + pow(adj, 2))

print('O cumprimento oposto é {}, o adjacente {} e a hipotenusa mede {}'.format(op, adj, hip))