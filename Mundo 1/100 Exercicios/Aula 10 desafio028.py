# Escreva um programa que faça o computador pensar um numero aleatorio entre 0 e 5, peça para o usuario tentar adivinhar qual numero foi escolhido pelo computador. 
# O Programa deverá escrever na tela se o usuario venceu ou perdeu.
from time import sleep
from random import randint
computador = randint(0,5) # Faz a maquina sortear um numero
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, quer tentar adivinhar??')
print('-=-' * 20)
jogador = int(input('Seu chute é??: ')) # Jogador tenta adivinhar
if computador == jogador:
    print('PROCESSANDO...')
    sleep(2) # FAZ O PROGRAMA ESPERAR 2 SEGUNDOS PARA PROSSEGUIR
    print('Parabéns voce acertou! eu tinha escolhido {} ;-;'.format(computador))
else:
    print('PROCESSANDO...')
    sleep(2) # FAZ O PROGRAMA ESPERAR 2 SEGUNDOS PARA PROSSEGUIR
    print('HiHi, trouxa, eu pensei no {} ^^!! PERDEU!!'.format(computador))