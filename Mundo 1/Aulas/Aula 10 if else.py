# Condições

# O professor explica a estrutura IF usando a função Se do portugol. ja tenho uma boa base de if, elif e else por estudos anteriores entao nao estou vendo muita coisa para anotar ate agora...

# if carro.esquerda(): # Toda estrutura IF tem que ser fechada com (:)
#   bloco verdadeiro acontece (verdadeiro sempre é descrito em Ingles com a primeria letra maiuscula: True)
# else: (não esquece do :)
#   bloco falso acontece (O mesmo para falso sendo: False)

# tempo = int(input('Quantos anos tem seu carro?'))
# if tempo <= 3:
#     print('Carro Novo!')
# else:
#     print('Carro Velho!')
# print('---FIM---')

# tempo = int(input('Quantos anos tem seu carro?'))
# print('Carro Novo!'if tempo <=5 else 'Carro velho!')
# print('---FIM---')

# nome = str(input('Qual é o seu nome?'))
# if nome == 'Eric':
#     print('Que nome lindo voce tem "-"')
# else:
#     print('Seu nome é tao normal.')
# print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 6:
    print('Você passou, sua média é {:.1f}'.format(media))
else:
    print('Você reprovou, sua média é {:.1f}'.format(media))