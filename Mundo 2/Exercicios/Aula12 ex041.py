#A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# -Até 9 anos: MIRIM 
# -Até 14 ano : INFANTIL 
# -Até 19 anos: JUNIOR 
# -Até 20 anos: SêNIOR 
# -Acima: MASTER

ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = int(input('Ano Atual: '))

idade = ano_atual - ano_nasc

if idade < 9:
    print('CATEGORIA MIRIM')
elif idade >= 9 and idade < 14:
    print('CATEGORIA INFANTIL')
elif idade >= 14 and idade < 19:
    print('CATEGORIA JUNIOR')
elif idade >= 19 and idade <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('MASTER')