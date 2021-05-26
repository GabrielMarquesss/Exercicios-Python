#Programa que leia o nome de uma pessoa e diga se ela tem silva no nome

nome = input('Digite o seu nome completo: ').title()
splt = nome.split()

if 'Silva' in splt:
    print('Seu nome possui Silva.')
else:
    print('Seu nome não possui Silva.')