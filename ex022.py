#Programa que leia nome completo de uma pessoa e mostre
#nome inteiro maiusculo, minusculo, letras sem considerar espaço
#quantas letras tem primeiro nome

nome = input('Digite o seu nome completo:')
splt = nome.split()

print(splt)
print('{}'.format(nome.upper()))
print('{}'.format(nome.lower()))
print('{}'.format(len(nome.replace(' ',''))))
print('{}'.format(splt[0]))
