#Programa que lê um número float e retorna apenas sua parte inteira.

from math import trunc

n = float(input('Digite um número: '))

print('O número {} em sua forma inteira é {}'.format(n,trunc(n)))