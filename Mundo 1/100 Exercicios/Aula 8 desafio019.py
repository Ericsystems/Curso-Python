#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
alunos = []
for i in range(1, 5):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)
sorteio = random.randint(0, len(alunos)-1)
sorteado = alunos[sorteio]

print('O Sorteado foi {}'.format(sorteado))

# Usei um pouco de conhecimento que ja tinha pra agilizar o processo, isso tudo foi preguiça de escrever 4 linhas de input pra 4 alunos e depois ter que relacionar os nomes com numeros kkkkkk
# A ideia era frizar o random, que foi usado de qualquer forma, vou considerar o exercicio concluido mas vou assistir a aula de resolução depois