# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
alunos = []
alunos2 = []
for i in range(1, 5):
    aluno = input('Nome do aluno: ')
    alunos.append(aluno)
while len(alunos) > 0:
    sorteio = random.randint(0, len(alunos)-1)
    sorteado = alunos[sorteio]
    alunos2.append(sorteado)
    alunos.remove(sorteado)
print('A ordem de apresentação do trabalho é 1°{}, 2°{}, 3°{}, e 4°{}'.format(alunos2[0], alunos2[1], alunos2[2], alunos2[3]))