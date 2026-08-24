# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# divisível por 400 → bissexto
# senão, divisível por 100 → não bissexto
# senão, divisível por 4 → bissexto
# senão → não bissexto

ano = int(input('Digite um ano para descobrir se é BISSEXTO: '))
if ano % 400 == 0:
    print('O Ano {} é um ano Bissexto.'.format(ano))
elif ano % 100 == 0:
    print('O Ano {} é um ano NÃO Bissexto.'.format(ano))
elif ano % 4 == 0:
    print('O Ano {} é um ano Bissexto.'.format(ano))
else:
    print('O Ano {} é um ano NÃO Bissexto.'.format(ano))