# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere US$1,00 = R$3,27
quantoemreal = float(input('Quanto dinheiro você tem na carteira? R$'))
dolares = quantoemreal / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(quantoemreal, dolares))