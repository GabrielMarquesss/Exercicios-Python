#Programa que leia o nome de uma cidade e diga se ela começa ou não com santo

cidade = input('Digite o nome de uma cidade:').title()
splt = cidade.split()

if splt[0] == 'Santo':
    print('{} começa com Santo.'.format(cidade))
else:
    print('{} não começa com Santo.'.format(cidade))