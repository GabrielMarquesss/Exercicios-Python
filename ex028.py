#Programa que faz o computador escolher um usuário, e o cliente tenta adivinhar

import random

n = random.randint(0,5)
print('O computador já escolher um número!')
user = int(input('Tente adivinhar o número que o computador escolheu!'
                 'Dica: é um número de 0 a 5: '))

if user == n:
    print('Parabéns!!! Você acertou!')
else:
    print('Errado! O computador pensou no número {}!'.format(n))