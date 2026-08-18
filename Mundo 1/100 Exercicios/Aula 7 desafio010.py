# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere US$1,00 = R$3,27

carteira = float(input('Digite o Saldo da sua carteira: '))
dolar = float(input('Qual a cotação atual do dolar?: '))

conversao = carteira / dolar

print('Considerando o valor atual do dolar: {}, com seu saldo atual de {} voce pode comprar {:.2f} dólares'.format(dolar, carteira, conversao))