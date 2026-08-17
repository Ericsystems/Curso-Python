print('====== Aula 6 ======')

# Crie um algoritmo que pergunte 2 numeros e calcule a soma entre eles:

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
soma = n1 + n2

print('A Soma vale {}'.format(soma))

# Para descobrir a classe de uma variavel, use a função type().
print('A variavel n1 é do tipo: ', type(n1))
print('A variavel n2 é do tipo: ', type(n2))
print('A variavel soma é do tipo: ', type(soma))

# O tipo primitivo de uma variavel deve ser especificado no momento da criação da variavel, caso contrario o python ira assumir o tipo primitivo como string. Para isso, use a função int() para numeros inteiros, float() para numeros decimais e str() para textos.

print('A Soma entre {} e {} vale {}'.format(n1, n2, soma))
