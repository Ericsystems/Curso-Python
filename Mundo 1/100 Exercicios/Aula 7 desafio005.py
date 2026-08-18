# Desafio 005
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um numero: '))

antecessor = numero - 1
sucessor = numero + 1

print('O antecessor de {} é {}, e o sucessor é {}'.format(numero, antecessor, sucessor))
# Também da para usar a operação aritmetica dentro do .format
print('O antecessor de {} é {}, e o sucessor é {}'.format(numero, numero - 1, numero + 1))
# Nesse caso as variaveis antecessor e sucessor não são mais necessárias, mas se for um programa maior, é interessante criar variaveis para deixar o código mais legivel.