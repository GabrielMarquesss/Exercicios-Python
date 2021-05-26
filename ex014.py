#Programa que leia uma temperatura em Cº e converte para Fº

c = float(input('Digite a temperatura em Celsius: '))
f = c * 1.8 + 32

print('A temperatura de {:.1f}ºC corresponde à {:.1f}ºF.'.format(c, f))
