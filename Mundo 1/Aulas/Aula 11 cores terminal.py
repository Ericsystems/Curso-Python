# Como trabalhar com cores no terminal

#codigo ANSI começa com contra barra (\) e depois o codigo
# Sempre que quiser representar uma cor em Python, começa com \033[ style / text / background m ex:
# \033[0:33:44m

# Os codigos para Style sao:
# 0 para none, ou deixa sem o numero
# 1 para Bold (negrito)
# 2 para Underline (sublinhado)
# 7 para Negative (inverter as configurações)

# Texto
# de 30 a 37 cada um representando uma cor, se quiser outra cor tem que baixar uma biblioteca pra isso

# background
# de 40 a 47 sendo as mesmas cores que o text

print('\033[1;35;47mOlá, Mundo!')