#Programa que mostra se um numero é par ou impar

n = int(input('Digite um número: '))
cal = n % 2

if cal == 0 :
    print('O número é par.')
else:
    print('O número é ímpar')