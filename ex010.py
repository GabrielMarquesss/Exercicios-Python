#Programa que leia o dinheiro em reais, depois diz quantos dólares
#ela pode comprar

brl = float(input('Digite aqui a quantidade em reais: '))
usd = 5.31

print('Com R${} é possível comprar U${:.2f}'.format(brl,brl/usd))