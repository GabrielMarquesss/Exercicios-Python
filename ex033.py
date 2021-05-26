#Programa que lê 3 numeros e diz o maior e menor

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
splt = [n1,n2,n3]

splt.sort()
print('O maior número é {}, e o menor é {}.'.format(splt[2],splt[0]))