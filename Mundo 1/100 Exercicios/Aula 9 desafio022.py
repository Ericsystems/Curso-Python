#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas.
# O nome com todas as letras minusculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())

lista = nome.split()
semespaco = ''.join(lista) 

# também era possivel utilizar um nome.count(' ') para contar os espaços vazios no texto, e utilizar o len menos esses espaços para evitar as duas funçoes acima.

print('Tem {} letras no total (sem espaços)'.format(len(semespaco)))
print('O primeiro nome tem {} letras.'.format(len(lista[0])))

# o professor evitou o split e usou nome.find() para procurar o primeiro ' ' e assim indentificar quantas letras tinha o primeiro nome da pessoa ja que o find retorna o indice do caractere procurado, ex: Ana Maria, o ' ' está no indice 4, mas quando voce imprime o find ele imprime o numero anterior ao indice procurado, ou seja, print 3, que é a quantidade de caracteres do nome de Ana, funcionaria para qualquer nome da mesma forma.