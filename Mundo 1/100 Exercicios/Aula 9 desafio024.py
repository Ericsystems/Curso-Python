# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo".
cidade = str(input('Digite o nome de uma cidade: '))
cidade2 = cidade.title()
cidade3 = cidade2.split()
print('O Nome da cidade começa com Santo? {}'.format('Santo' in cidade3[0]))