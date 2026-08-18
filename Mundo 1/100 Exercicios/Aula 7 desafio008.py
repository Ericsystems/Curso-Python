# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros.

metros = float(input('Digite um valor em metros: '))

quilometros = metros * 0.001
hectometros = metros * 0.01
decametros = metros * 0.1
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

print('{} metros equivalem a {:.3f} quilômetros\n{} metros equivalem a {:.2f} hectômetros\n{} metros equivalem a {:.1f} decâmetros\n{} metros equivalem a {:.0f} decímetros\n{} metros equivalem a {:.0f} centímetros\n{} metros equivalem a {:.0f} milímetros'.format(metros, quilometros, metros, hectometros, metros, decametros, metros, decimetros, metros, centimetros, metros, milimetros))