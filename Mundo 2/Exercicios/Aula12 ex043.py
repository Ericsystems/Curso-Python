# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do peso
# -Entre 18.5 e 25: Peso ideal
# -25 até 30: Sobrepeso
# -35 até 40: Obesidade
# -Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu Peso Ideal.')
elif imc >= 25 and imc < 30:
    print('Você está em Sobrepeso.')
elif imc >= 30 and imc < 35:
    print('Você está em Obesidade.')
elif imc >= 35 and imc < 40:
    print('Você está em Obesidade Mórbida.')
else:
    print('Você está com uma puta obesidade morbida slk, nem compensa arrumar mais "-"')