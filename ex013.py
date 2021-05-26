#Programa que leia o salário de um funcionario e depois o novo salario
#com aumento de 15%

oldsal = float(input('Digite o salário atual: '))
amnt = 0.15
newsal = oldsal + (oldsal*amnt)

print('O salário de {:.2f} com aumento de 15% ficará {:.2f}'.format(oldsal,newsal))