#Programa que leia a largura de uma parede em metros, calcule sua area
#e a qtd necessaria de tinta, sabendo que 1l tinta pinta 2m²

larg = float(input('Digite qual a largura da parede: '))
alt = float(input('Digite qual a altura da parede: '))
tinta = 2

print('Uma parede de {}m de largura e {}m de altura tem área de {:.2f}m². Neste'
      'caso, será necessário {:.2f}L de tinta.'.format(larg,alt,larg*alt,(larg*alt)/2))