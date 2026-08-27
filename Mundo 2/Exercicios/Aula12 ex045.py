# Crie um programa que faça o computador jogar Jokenpô com voce.
from random import randint
from time import sleep
computador = randint(1,3)
print('-=-' * 20)
print('                   BORA JOGAR JANKENPÔ')
print('-=-' * 20)
print(' 1 | PEDRA')
print(' 2 | PAPEL')
print(' 3 | TESOURA')
usuario = int(input('FAÇA SUA JOGADA [1] [2] [3]: '))
print('')

if computador == 1:
    jogada_computador = 'PEDRA'
elif computador == 2:
    jogada_computador = 'PAPEL'
elif computador == 3:
    jogada_computador = 'TESOURA'

if usuario == 1:
    jogada_usuario = 'PEDRA'
elif usuario == 2:
    jogada_usuario = 'PAPEL'
elif usuario == 3:
    jogada_usuario = 'TESOURA'

# 1 ganha do 3 
# 2 ganha do 1 
# 3 ganha do 2
if usuario != computador:
    if computador == 1 and usuario == 3 or computador == 2 and usuario == 1 or computador == 3 and usuario == 2:
        print('USUARIO JOGOU: {}'.format(jogada_usuario))
        print('')
        print('COMPUTADOR JOGOU: {}'.format(jogada_computador))
        print('')
        print('VITORIA DA MAQUINA !!')
    elif computador == 3 and usuario == 1 or computador == 1 and usuario == 2 or computador == 2 and usuario == 3:
        print('USUARIO JOGOU: {}'.format(jogada_usuario))
        print('')
        print('COMPUTADOR JOGOU: {}'.format(jogada_computador))
        print('')
        print('VITORIA DO JOGADOR !!')
    else:
        print('Escolha uma opção válida')
else:
    print('EMPATE, joga denovo ^^')
