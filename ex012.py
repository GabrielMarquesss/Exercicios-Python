#Programa que lê o preço de um produto e mostre o novo preço com 5% desc

produto = float(input('Digite qual o valor do produto: '))
desc = 0.05
novo = produto - (produto*desc)
print('O produto cujo valor inicial de R${:.2f}, com desconto de 5% sai por R${:.2f}'.format(produto,novo))