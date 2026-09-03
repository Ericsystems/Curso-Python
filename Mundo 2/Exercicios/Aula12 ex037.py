# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
# -1 para binario 
# -2 para octal 
# -3 para hexadecimal
resposta = 'S'
while resposta == 'S':
    print('-=-' * 20)
    print('              CONVERSOR DE BASES NUMERICAS')
    print('-=-' * 20)
    numero = int(input('Digite um número inteiro: '))
    print('-=-' * 20)
    print('              SELECIONE A BASE DE CONVERSÃO')
    print('-=-' * 20)
    print(' 1 | BINÁRIO')
    print(' 2 | OCTAL')
    print(' 3 | HEXADECIMAL')
    conversao = int(input('Selecione [1] [2] [3]: '))
    if conversao == 1:
        numero_convertido = bin(numero)
        print('O número {} convertido para BINÁRIO é: {}'.format(numero, numero_convertido))
    elif conversao == 2:
        numero_convertido = oct(numero)
        print('O número {} convertido para OCTAL é: {}'.format(numero, numero_convertido))
    elif conversao == 3:
        numero_convertido = hex(numero)
        print('O número {} convertido para HEXADECIMAL é: {}'.format(numero, numero_convertido))
    else:
        print('Você digitou um numero invalido, tente novamente.')
    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
