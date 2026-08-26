#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -Se ele ainda vai se alistar ao serviço militar. 
# -Se é a hora de se alistar.
# -Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = int(input('Ano atual: '))
idade = ano_atual - ano_nasc
hora_de_alistar = 16

if idade < hora_de_alistar:
    print('Ainda vai se alistar no serviço militar! Faltam {} anos para seu alistamento obrigatorio.'.format(hora_de_alistar - idade))
elif idade == hora_de_alistar:
    print('Dirija-se ate a base do serviço militar mais proxima para se apresentar, vocÊ está na idade de alistamento obrigatorio!')
else:
    print('Você ja passou do tempo de alistamento.')


