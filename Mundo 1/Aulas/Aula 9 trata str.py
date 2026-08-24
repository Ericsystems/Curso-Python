# AULA 9: Manipulando texto
# Hora de aprender a manipular cadeias de caracteres

# O simbolo nde colchete [] <- é o identificador de uma lista (informação avulsa)
# Fatiamento de string

# frase = 'Curso em Video Python' # essa frase possui 21 caracteres, contando desde 0 (C), ate o 21 (n), os espaços em branco tambem sao levados em consideração nessa contagem.

# print(frase[9:14]) # esse print procura o caractere de indice 9 dentro da variavel frase e retorna somente aquele valor, ou seja 'V'. quiser pegar um trecho dentro da string voce usa o mesmo argumento adicionando a localização do final da leitura, ex: frase[9:14] retorna o indice de 9 a 14 excluindo o 14, ou seja, imprime de 9 a 13.

# contagem = '1234567891011121314151617181920' # também é possivel imprimir de forma ordenada, ex, pulando de 2 em 2, 3 em 3, etc, o céu é o limite kkk, pra isso é usado um 3 parametro dentro do [], ex: contagem[0:21:2]

# print(contagem[0:21:2]) # vai imprimir do indice 0 ao 21 pulando de 2 em 2 como especificado no ultimo parametro (somente imapres no caso)
# da para omitir o primeiro parametro quando quero iniciar pelo 0, se colocar contagem[:21:2] o programa entende a falta do primeiro parametro antes do : como 0.

# da mesma forma da para omitir o segundo valor [15::2] vai pular de 2 em 2 começando pelo indice 15

# Analise
# Função len(frase) retorna a quantidade de caracteres dentro da variavel, frase, lista, etc. ex print(len(frase)) retorna 21 pois é a quantidade de caracteres dentro da variavel frase (começando sempre por 0, todos os espaços utilizados tam bem sao contados)
# frase.count('o') # essa função vai contar quantas vezes aparece determinada letra, palavra, numero etc, dentro da variavel, ATENÇÃO A MAIUSCULAS E MINUSCULAS sao identificadas separadamente, entao se houver um O maiusculo dentro da variavel, ele nao será contabilizado nessa conta.
# frase.count('o,0,13') # Mescla a função de fatiamento, porem usando virgula
# frase.find('deo') # Procura o indice onde se encontra determinada palavra, trexo, numero... mesmo que 'deo' tenha 3 indices(1 para cada letra), é considerado apenas o indice da primeria letra
# Quando voce procura no .find() uma palavra que nao existe na fraase em questão, ele retorna valor -1

# O operador in me retorna um valor booleano sendo True ou False (é bem intuitivo na verdade entao nao vou explicar muito porque ja sei...)
# 'Curso' in frase # verifica se ha a palavra Curso dentro da variavel frase, porem ele so retorna se sim ou nao, sendo verdadeiro para sim, e falso para nao

# Transformação

# Por regra, uma lista de string é imutavel.
# Não conseguimos mexer direto nos elementos, mas podemos muda-la atraves de metodos. Ex:
# frase.replace('Python','Android') # Procura a frase Python dentro da variavel e substitui ela pela palavra Android, mesmo que tenha mais caracteres que a anterior. Porém ele nao substitui diretamente na variavel, ele substitui de uma forma secundaria, momentanea, enquanto for chamada ele aparece.
# frase.upper() # deixa a frase totalmente maiuscula, .lower() deixa minusculo.
# frase.capitalize() # Vai transformar a string toda em minusculo, e vai transformar em maiusculo somente a primeira letra da string
# frase.title() # Deixa todas as palavras com a primeira letra maiuscula, a cada quebra de espaço ele deixa a letra maiuscula

# frase2 = '   Aprenda Python  '
# frase2.strip() # Remove todos os espaços inuteis no inicio e no final da string, é uma opção de tratamento de texto. quando removidos os espaços escedentes no inicio da frase, o primeiro caractere (A) começa a ter indice 0. tambem tem o .rstrip(), para apagar os espaços somente da direita da frase, e o lstrip() para remover somente os da esquerda

# Divisão

# frase3 = 'Curso em Video Python'

# frase3.split() # Gera uma lista usando a divisão por espaços, ou seja, frase3 vai passar a ser [Curso][em][Video][Python] e cada palavra começa a ter indice começando em 0, dessa forma quando chamar a frase3[0], vai retornar a palavra Curso
# é possivel voltar a juntar a lista usando o metodo join e definindo qual vai ser o separador entre cada palavra(pode ser um espaço em branco ou nao),  Ex:
# '-'.join(frase3) # dessa forma vai retornar 'Curso-em-Video-Python'

frase = 'Curso em Video Python'
