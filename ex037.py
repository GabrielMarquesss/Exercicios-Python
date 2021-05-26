#Programa que lê um numero inteiro, pede pro usuário escolher
# a base de conversãoe realiza a operação

import math

n = int(input('Digite um número inteiro: '))
user = int(input('Digite digite [1] para binário, [2] para octal ou [3] para hexadecimal: '))

if user == 1:
    print('O número {} em sua forma binária é {}'.format(n,bin(n).replace('0b','')))
elif user == 2:
    print('O número {} em sua forma octal é {}.'.format(n,oct(n).replace('0o','')))
elif user == 3:
    print('O número {} em sua forma hexadecimal é {}.'.format(n,hex(n).replace('0x','').upper()))
else:
    print('{} não é uma opção válida. Tente novamente.'.format(user))
