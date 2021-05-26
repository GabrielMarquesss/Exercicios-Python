#Pedra, papel ou tesoura!
import random

ppt = ['Pedra', 'Papel', 'Tesoura']
pc_choice = random.choice(ppt)
user = input('O computador já fez a escolha! Escolha Pedra, Papel ou Tesoura: ').title()

###################EMPATES###################
if pc_choice == 'Pedra' and user == 'Pedra':
    print('Empate. Pedra empata com Pedra!')
elif pc_choice == 'Papel' and user == 'Papel':
    print('Empate. Papel empata com Papel!')
elif pc_choice == 'Tesoura'and user == 'Tesoura':
    print('Empate. Tesoura empata com Tesoura.')

###################VITÓRIAS_USER###################
if user == 'Pedra' and pc_choice == 'Tesoura':
    print('Você venceu! Pedra quebra Tesoura!')
elif user == 'Papel' and pc_choice == 'Pedra':
    print('Você venceu! Papel embrulha Pedra!')
elif user == 'Tesoura' and pc_choice == 'Papel':
    print('Você venceu! Tesoura corta Papel.')

###################VITÓRIAS_PC###################
if pc_choice == 'Pedra' and user == 'Tesoura':
    print('Você Perdeu! Pedra quebra Tesoura!')
elif pc_choice == 'Papel' and user == 'Pedra':
    print('Você Perdeu! Papel embrulha Pedra!')
elif pc_choice == 'Tesoura' and user == 'Papel':
    print('Você Perdeu! Tesoura corta Papel.')

