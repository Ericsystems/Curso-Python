# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.
Algo = input('Digite algo: ')
print('O tipo primitivo de {} valor é: {} '.format(Algo, type(Algo)))
if Algo.isspace() == True:
    print('No texto " {} " só tem espaços.'.format(Algo))
else:
    print('No texto " {} " não tem só espaços'.format(Algo))
if Algo.isnumeric() == True:
    print('O texto " {} " é um numero'.format(Algo))
else:
    print('O texto " {} " não é um numero'.format(Algo))
if Algo.isalpha() == True:
    print('O texto " {} " é alfabetico'.format(Algo))
else:
    print('O texto " {} " não é alfabetico'.format(Algo))
if Algo.isalnum() == True:
    print('O texto " {} " é alfanumerico'.format(Algo))
else:
    print('O texto " {} " não é alfanumerico'.format(Algo))
if Algo.isupper() == True:
    print('O texto " {} " está totalmente em maiusculas'.format(Algo))
else:
    print('O texto " {} " não está em maiusculas'.format(Algo))
if Algo.islower() == True:
    print('O texto " {} " está totalmente em minúsculas'.format(Algo))
else:
    print('O texto " {} " não está em minúsculas'.format(Algo))
if Algo.istitle() == True:
    print('O texto " {} " está capitalizada'.format(Algo))
else:
    print('O texto " {} " não está capitalizada'.format(Algo))
