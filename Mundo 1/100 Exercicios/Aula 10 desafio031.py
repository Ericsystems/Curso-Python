# Desenvolva um programa que pergunte a distancia de uma viagem em KM. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de ate 200Km e R$0,45 para viagens mais longas.
distancia = float(input('Digite a distancia da viagem em Km: '))

'''if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45'''

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('Sua passagem custa {:.2f}.'.format(preco))