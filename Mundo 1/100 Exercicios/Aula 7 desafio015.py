# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int(input('Quantos dias voce ficou com o carro?: '))
kmrodado = float(input('Quantos km voce rodou com o carro?: '))

pagamento = (dias * 60) + (kmrodado * 0.15)

print('Voce deve pagar R${:.2f} por {} dias e {:.2f} km rodados'.format(pagamento, dias, kmrodado))