#Programa que calcula a quantidade de KM percorrico,
# a quantidade de dias alugado. Preço a pagar: carro = 60/dia + 0,15 por km

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados com o carro? '))
pay = (dias * 60) + (km * 0.15)

print('O carro foi alugado por {} dias e foram rodados {}Km. O preço à'
      'pagar é de R${:.2f}.'.format(dias,km,pay))