# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,0 por cada km acima do limite.

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade >= 80:
    print('Você foi multado. A velocidade permitida é de até 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar R${:.2f} de multa.'.format(multa))
else:
    print('Você está dentro do limite de velocidade')
print('Tenha um bom dia, dirija com segurança!')