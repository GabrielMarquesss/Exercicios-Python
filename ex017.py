#Programa que lê comprimeto cateto oposto e do adjacente de um
#triangulo retangulo, calcule o tamanho da hipotenusa
import math

cat1 = float(input('Digite qual o cateto oposto: '))
cat2 = float(input('Digite qual o cateto adjacente: '))

print('O cateto tem o valor de {} e o cateto adjacente {}. Logo, sua'
      'hipotenusa é de {:.2f}'.format(cat1,cat2,math.hypot(cat1,cat2)))