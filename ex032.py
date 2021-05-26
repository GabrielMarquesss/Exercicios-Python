#Programa que diz se ano é bissexto ou não:

ano = int(input('Digite um ano: '))

if ano // 400 and ano % 4 == 0 and ano % 100 != 0 :
    print('{} é bissexto'.format(ano))
else:
    print('{} não é ano bissexto.'.format(ano))
