#Faça um algoritmo que leia o salario de um funcionario
#e mostre seu novo salario, com 15% de aumento.

salario = float(input('Digite o seu salario: '))

#novosalario = salario + (salario * 0.15) # da pra remover os parenteses, deixei para ficar explicito a intenção
# ideal seria usar 2 variaveis, uma para o aumento e outra para o novo salario, mas como é um exercicio simples, deixei assim.
novosalario = (salario * 15 / 100) + salario # mesmo resultado, menos codigo
print('Seu novo salario com aumento de 15% é R${:.2f}'.format(novosalario))