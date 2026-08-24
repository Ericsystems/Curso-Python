# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. 
# Para salarios superiores a R$1.250,0, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o Salário: '))

if salario > 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)
print('Seu novo salario é de R${:.2f}'.format(salario))