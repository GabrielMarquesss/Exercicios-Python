#Programa que leia ano de nascimento de um atleta e mostre sua categoria
#De acordo com a sua idade
#até 9 anos = mirim
#até 14 anos = infantil
#até 19 anos = junior
#até 20 anos = senior
#acima de 20 = pleno

from datetime import date

ano = int(input('Digite em qual ano você nasceu: '))
ytd = date.today().year - ano

if ytd <= 9:
    print('Você tem {} anos. Sua categoria atual é Mirim.'.format(ytd))
elif ytd <= 14:
    print('Você tem {} anos. Sua categoria atual é Infantil.'.format(ytd))
elif ytd <= 19:
    print('Você tem {} anos. Sua categoria atual é Júnior.'.format(ytd))
elif ytd == 20:
    print('Você tem {} anos. Sua categoria atual é Sênior.'.format(ytd))
else:
    print('Você tem {} anos. Sua categoria atual é Pleno.'.format(ytd))
