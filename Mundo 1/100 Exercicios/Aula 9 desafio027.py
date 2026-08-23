# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome sparadamente.
# EX: Ana Maria de Souza 
# primeiro = Ana 
# ultimo = Souza

nome = input('Digite seu Nome Completo: ')
nome = nome.title()
lista = nome.split()
print('O Primeiro nome é: {}'.format(lista[0]))
print('O Ultimo nome é: {}'.format(lista[len(lista) -1]))