#Faça um programa que leia uma frase pelo teclado e ostre: 
# Quantas vezes aparece a letra "A" 
# Em que posição ela aparece a primeira vez. 
# Em que posição ela aparece a ultima vez.

frase = str(input('Digite uma frase: '))
maiusc = frase.upper()
print('A letra A aparece {} vezes'.format(maiusc.count('A')))
print('Ela aparece primeiro na posição {}.'.format(maiusc.find('A')))
print('Ela aparece por ultimo na posição {}.'.format(maiusc.rfind('A')))