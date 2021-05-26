#Programa que calcula a rota de uma viagem em km
#Se km <=200 cobra 0,50 por km
#>200 cobra 0,45

km = float(input('Digite o da viagem total em Km: '))

if km <=200:
    print('Uma viagem de {}Km, terá um custo de {:.2f}.'.format(km,km*0.50))
elif km > 200:
    print('Uma viagem de {}Km, terá um custo de {:.2f}.'.format(km, km * 0.45))