#Programa que escreva o salario de um funcionario e o aumento
#salarios acima de 1250 aumenta em 10%
#salario inferior a 1250 aumentar 15%

oldsal = float(input('Digite o salário atual: '))

if oldsal > 1250:
    print('O salário com aumento de 10% de aumento ficará {:.2f}.'.format((oldsal*0.10) + oldsal))
else:
    print('O salário com aumento de 15% de aumento ficará {:.2f}.'.format((oldsal * 0.15) + oldsal))