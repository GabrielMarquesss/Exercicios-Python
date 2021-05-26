#Programa que leia um valor em metros e exiba convertido em cm e mm

m = float(input('Digite a quantiade em metros: '))

print('{} metros é equivalente a {:.0f} centímetros ou {:.0f} milímetros.'.format(m,m*100,m*1000))