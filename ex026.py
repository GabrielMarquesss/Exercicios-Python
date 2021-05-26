#Programa que leia uma frase e diga:
# quantas vazes aparece a letra a
# em que posicao ela aparece a primeira vez
# a posicao que ela aparece a ultima vez

frase = input('Digite aqui uma frase: ').lower()

print('A letra "a" aparece {} vezes na frase.'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(frase.find('a') + 1))
print('A letra "a" aparece pela última vez na posição {}.'.format(frase.rfind('a') + 1))

