#Refazendo o ex035 dizendo se
#equilatero = todos lados iguais
#isoceles = dois lados iguais
#escaleno = todos lados diferentes

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triângulo pode existir!')
    if r1 == r2 and r2 == r3:
        print('O triângulo será equilátero.')
    elif r1 != r2 != r3 != r1:
        print('O triângulo será escaleno.')
    else:
        print('O triângulo será isósceles.')
else:
    print('O triângulo não pode existir!')



