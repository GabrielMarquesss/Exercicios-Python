#Programa que leia o ano de nascimento e diga de acordo com sua idade se:
#Ainda vai se alistar
#Se é hora de se alistar
#Ou se já passou o tempo de se alistar, e quanto tempo

from datetime import date

ano = int(input('Digite em qual ano você nasceu: '))
ytd = date.today().year - ano

if ytd < 18:
    print('Você atualmente tem {} anos. O alistamento é obrigatório após os 18 anos, se aliste daqui {} anos.'.format(ytd,18-ytd))
elif ytd == 18:
    print('Você tem {} anos e está apto a se alistar. Compareça à junta militar.'.format(ytd))
else:
    print('Você está atrasado em {} anos para o alistamento. Compareça à junta militar para regularizar sua situação.'.format(ytd-18))

