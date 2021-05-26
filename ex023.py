#Programa que irá ler numero 0 a 9999 e mostre na tela
#milhar, centena, dezena e unidade separados

n = int(input('Digite um número: '))
u = n // 1 % 10
c = n // 10 % 10
d = n // 100 % 10
m = n // 1000 % 10

print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(u,c,d,m))