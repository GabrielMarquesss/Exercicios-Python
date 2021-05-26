#Programa que leia um nome completo e diga o primeiro e ultimo nome

nome = input('Digite seu nome completo: ').title()
splt = nome.split()

print(splt[0],splt[-1])