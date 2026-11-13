#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto

preco = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o valor do desconto a ser aplicado em %: '))
valordodesconto = (preco / 100) * desconto

print('O produto vai sair a R${:.2f} com o desconto aplicado.'.format(preco - valordodesconto))
print('Desconto aplicado: {}%'.format(desconto))
print('O valor do desconto aplicado foi de R${:.2f}'.format(valordodesconto))