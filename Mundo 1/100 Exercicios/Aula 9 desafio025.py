# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite um Nome: '))
nome2 = nome.title()
nome3 = nome2.split()
print('O Nome digitado tem Silva? {}'.format('Silva' in nome3))