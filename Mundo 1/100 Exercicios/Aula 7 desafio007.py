# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media.

aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2

print('A média do aluno {} é {:.2f}'.format(aluno, media))