# Sempre que quiser imprimir algo na tela use aspas, seja ela simples ('') ou duplas ("")
print('Olá, Mundo!')

# Numeros sao usados primordialmente para fazer calculos dentro do programa, também é possivel  imprimir o numero na tela sem fazer calculo ao adicionar ele dentro de aspas (''). Nessa ocasião,basicamente as aspas sao usadas para transformar numero em texto.

print(7+2, ', Imprime na tela a soma entre 7 e 2')
print('7+2, nao imprime a soma pois os numeros estão inicialmente entre aspas')

# Se quero juntar 2 mensagens dentro da mesma chamada, é possivel com a estrutura 
# print('Mensagem' + 'Mensagem') utilizando o +.
# Nome, idade, peso, são exemplos de variaveis, toda variavel é um objeto e pode receber valores
# Qualquer texto fora de aspas deve ser escrito de forma minuscula para nao confundir oprograma.
# input serve para fazer uma pergunta ao usuario, esse input pode ou deve ser atribuido a uma variavel para receber o 'valor' digitado pelo usuario.

nome = input('Qual é o seu Nome?: ')
idade = input('Qual a sua Idade?: ')
peso = input('Qual o seu Peso?: ')

print('Meu nome é ', nome, 'Tenho ', idade, 'anos e peso', peso, 'kg.' )

# Ao usar o Input o valor digitado sempre será considerado como string, mesmo que seja digitado numero inteiro ou com decimal.
# Para que o valor digitado seja considerado como numero inteiro ou decimal, é necessario usar a função int() ou float() respectivamente.Exemplo:
n1 = int(input('Digite um numero inteiro: '))
n2 = float(input('Digite um numero decimal: '))