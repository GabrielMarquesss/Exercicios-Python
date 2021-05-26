#Programa que aprova ou não um empréstimo para compra de uma casa
#Se o valor da parcela for maior que 30% do salario, nega o emprestimo

casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
meses = int(input('Digite em quantos anos a casa será paga: '))*12

if casa/meses > sal*0.30:
    print('O valor da parcela seria de R${:.2f}. O empréstimo foi negado.'.format(casa/meses))
else:
    print('O empréstimo foi aprovado! O valor da parcela será de R${:.2f}'.format(casa/meses))