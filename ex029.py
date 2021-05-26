#Programa que leia velocidade de um carro
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que foi multado
#A multa vai custar 7,00 por km acima do limite

vel = int(input('Digite qual a velocidade capturada pelo radar móvel: '))
multa = (vel - 80) * 7.00

if vel > 80:
    print('Acima do limite de velocidade ({}) km/h! Aplicar multa de R${:.2f}.'.format(vel,multa))
else:
    print('Siga com cuidado!')

