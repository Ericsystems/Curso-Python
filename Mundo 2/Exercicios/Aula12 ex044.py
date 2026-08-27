#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/ cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em ate 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

from time import sleep
preco = float(input('Valor: '))
qtd = int(input('Quantidade: '))
total = preco * qtd
print('-=-' * 20)
print('               SELECIONE A FORMA DE PAGAMENTO')
print('-=-' * 20)
print(' 1 | À vista DINHEIRO / Cheque')
print(' 2 | À vista CARTÃO')
print(' 3 | Dividir no cartão (até 2x)')
print(' 4 | Dividir no cartão (3x ou mais)')
resposta = int(input('Selecione a forma de pagamento. [1] [2] [3] [4]: '))

if resposta == 1:
    desconto = total - (total * 0.90)
    precofinal = total - desconto
    print('PAGAMENTO À VISTA SELECIONADO')
    print('Desconto de 10% sendo aplicado...')
    print('')
    sleep(2)
    print('Valor total: R${:.2f}.'.format(total))
    print('VALOR A RECEBER: R${:.2f}.'.format(precofinal))
    print('Desconto aplicado: R${:.2f}.'.format(desconto))
elif resposta == 2:
    desconto = total - (total * 0.95)
    precofinal = total - desconto
    print('PAGAMENTO À VISTA CARTÃO  | SELECIONADO')
    print('Desconto de 5% sendo aplicado...')
    print('')
    sleep(2)
    print('Valor total: R${:.2f}.'.format(total))
    print('VALOR A RECEBER: R${:.2f}.'.format(precofinal))
    print('Desconto aplicado: R${:.2f}.'.format(desconto))
elif resposta == 3:
    precofinal = total / 2
    print('PAGAMENTO 2X CARTÃO  | SELECIONADO')
    print('PROCESSANDO...')
    print('')
    sleep(2)
    print('Valor total: R${:.2f}.'.format(total))
    print('VALOR POR PARCELA: R${:.2f} em 2x.'.format(precofinal))
elif resposta == 4:
    juros = total - (total * 0.80)
    precofinal = total + juros
    print('PAGAMENTO À VISTA CARTÃO  | SELECIONADO')
    print('Juros de 20% sendo aplicado...')
    print('')
    sleep(2)
    print('Valor total: R${:.2f}.'.format(total))
    print('VALOR A RECEBER: R${:.2f}.'.format(precofinal))
    print('Juros aplicado: R${:.2f}.'.format(juros))
else:
    print('Você não selecionou uma das opções validas')

    

