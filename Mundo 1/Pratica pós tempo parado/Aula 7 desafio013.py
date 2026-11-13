#Faça um algoritmo que leia o salario de um funcionario
#e mostre seu novo salario, com 15% de aumento.

Salario = float(input('Digite o salário do funcionário: R$'))
aumento = float(input('Digite o valor do aumento a ser aplicado em %: '))
valordoaumento = (Salario / 100) * aumento

print('O novo salário do funcionário é de R${:.2f} com o aumento de {}% aplicado.'.format(Salario + valordoaumento, aumento))