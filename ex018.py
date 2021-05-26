#Programa que lê um angulo e diz seu seno, coseno e tangente

import math

ang = float(input('Digite o valor de um ângulo: '))

print('O ângulo de {}º tem o Seno de {:.2f}, Cosseno de {:.2f} e Tangente de {:.2f}'.format(ang,math.sin(ang),math.cos(ang),math.tan(ang)))