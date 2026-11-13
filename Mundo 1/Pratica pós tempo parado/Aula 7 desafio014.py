# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
temperatura_celsius = float(input('Digite a temperatura em °C: '))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print('A temperatura em °F é: {:.1f}'.format(temperatura_fahrenheit))