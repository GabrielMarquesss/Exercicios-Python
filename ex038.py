#Programa que le dois numeros e diz se:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior já que os dois são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O número {} é maior que {}!'.format(n1,n2))
elif n2 > n1:
    print('O número {} é maior que {}!'.format(n2, n1))
else:
    print('Não há valor maior. {} e {} são iguais!'.format(n1, n2))