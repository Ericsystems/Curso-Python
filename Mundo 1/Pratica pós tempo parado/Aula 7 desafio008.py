# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros.

metros = float(input('Digite um valor em metros: '))
print('O valor de {} metros corresponde a:'.format(metros))
print('{} quilômetros'.format(metros / 1000))
print('{} hectômetros'.format(metros / 100))
print('{} decâmetros'.format(metros / 10))
print('{} decímetros'.format(metros * 10))
print('{} centímetros'.format(metros * 100))
print('{} milímetros'.format(metros * 1000))