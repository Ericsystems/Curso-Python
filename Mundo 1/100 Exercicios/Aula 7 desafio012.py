#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto

preco = float(input('Preço: '))

desconto = (preco / 100) * 5
#desconto = preco * 0.05 mesmo resultado, menos codigo
novopreco = preco - desconto
#novopreco = preco * 5 / 100 mesmo resultado, menos codigo

print('Novo preço com desconto de 5%: R$ {:.2f}'.format(novopreco))