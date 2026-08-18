#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pintá-la,sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

area = altura * largura
tinta = area / 2

print('A área total da parede é {:.2f}m², e para pintar ela completamente você irá gastar {:.2f} litros de tinta.'.format(area, tinta))