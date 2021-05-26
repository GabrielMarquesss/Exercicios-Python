#Programa que lê duas notas e calcula sua média

n1 = float(input('Digite qual a nota mensal: '))
n2 = float(input('Digite qual a nota bimestral: '))
media = (n1+n2)/2

print('A média do aluno foi de {:.1f}'.format(media))