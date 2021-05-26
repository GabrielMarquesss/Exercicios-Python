#Programa que calcula o valor de um produto considerando o preço normal
#e a forma de pagamento
#à vista dinheiro/cheque = 10% desconto
#à vsta no cartão: 5% de desconto
#2x no cartão = preço normal
#3x ou mais no cartão = 20% de juros

p1 = float(input('Digite o preço do produto: '))
pag = int(input('Digite qual será a forma de pagamento. [1] para dinheiro ou cheque. '
                '[2] para cartão: '))

if pag == 1:
    print('O pagamento à vista com dinheiro ou cheque tem 10% de desconto. O novo valor é de R${:.2f}'.format(p1-(p1*0.10)))
elif pag == 2:
    vista = 1
    user = int(input('Digite [1] se o pagamento for à vista e [2] se o pagamento for à prazo: '))
    if user == 1:
        print('O pagamento à vista com cartão tem 5% de desconto. O novo valor é de R${:.2f}'.format(p1-(p1*0.05)))
    else:
        prazo = int(input('Digite em quantas vezes o produto será parcelado: '))
        if prazo < 2:
            print('O produto foi dividido em {} parcelas, ficando {}x de R${:.2f}'.format(prazo,prazo,p1/prazo))
        else:
            print('O produto foi dividio em {} parcelas com de 20% de juros. O valor parcelado é de {}x de {:.2f}, com valor total de {:.2f}'.format(prazo,prazo,(p1+(p1*0.2))/prazo,p1+(p1*0.2)))
