#Programa que lê a média de duas notas, calcule sua média, e com base
#na média mostre aprovado se média = 7.0 ou mais
#reprovado se média abaixo de 5.0
#recuperação se média entre 5.0 e 6.9

import numpy as np

nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
media = (nota1+nota2)/2

if media > 7.0:
    print('Sua média foi de {}. APROVADO!'.format(media))
elif media < 5.0:
    print('Sua média foi de {}. REPROVADO!'.format(media))
else:
    print('Sua média foi de {}. Você ficou de RECUPERAÇÃO!'.format(media))
