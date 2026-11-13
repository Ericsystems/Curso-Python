# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um numero: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(numero, numero*2, numero*3, numero**(1/2)))