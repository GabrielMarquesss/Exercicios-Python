#Programa que calcula IMC e mostre status
#Abaixo de 18.5 abaixo do peso
#entre 18.5 e 25 peso ideal
#entre 25 e 30 sobrepeso
#entre 30 ate 40 obesidade
#acima de 40 obesidade morbida

peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura em M: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('IMC de {:.2f}. Você está abaixo do peso.'.format(imc))
elif 18.5 < imc < 25:
    print('IMC de {:.2f}. Você está no peso ideal!'.format(imc))
elif 25 < imc < 30:
    print('IMC de {:.2f}. Você está com sobrepeso.'.format(imc))
elif 30 < imc < 40:
    print('IMC de {:.2f}. Você está com obesidade.'.format(imc))
else:
    print('IMC de {:.2f}. Você está com obesidade mórbida. Procure ajuda médica.'.format(imc))
