# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um numero: '))

dobro = numero * 2
triplo = numero * 3
raizquad = numero ** (1/2)

print('O dobro de {} vale {}\nO triplo de {} vale {}\nA raiz quadrada de {} é {:.2f}'.format(numero, dobro, numero, triplo, numero, raizquad))
# As operações podem ser feitas dentro do .format, mas é interessante criar variaveis para deixar o código mais legivel.