# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.
from time import sleep
print('')
print('-=-' * 20)
print('Aprovando Financiamento Imobiliario')
print('-=-' * 20)
print('')
valorimovel = float(input('Qual o valor do ímovel?: '))
Salariocomprador = float(input('Salario do comprador?: '))
prazo_em_anos = int(input('Vai pagar em quantos anos?: '))
print('PROCESSANDO DADOS...')
sleep(3)

prazo_mensal = prazo_em_anos * 12
prestacao = valorimovel / prazo_mensal
trinta = Salariocomprador * 0.30

if prestacao <= trinta:
    print('Parabéns, sua compra foi APROVADA')
    sleep(1)
    print('A prestação será R${:.2f} durante o prazo de {} meses.'.format(prestacao, prazo_mensal))
else:
    print('COMPRA NEGADADA')
    sleep(1)
    print('De acordo com os dados informados, a prestação de R${:.2f}, ultrapassa o limite de segurança do seu salario.'.format(prestacao))
    print('Salario R${:.2f}, Limite de segurança R${:.2f}'.format(Salariocomprador, trinta))
    print('A prestação mensal não pode ultrapassar 30% do salario do comprador, que é R${:.2f}'.format(trinta))

"Teste 2 dos comandos git"
