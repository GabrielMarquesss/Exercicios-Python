#Programa que leia 4 alunos e crie uma ordem nova da lista

import random

aluno1 = input('Digite o nome de um aluno: ').title()
aluno2 = input('Digite o nome de um aluno: ').title()
aluno3 = input('Digite o nome de um aluno: ').title()
aluno4 = input('Digite o nome de um aluno: ').title()
alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)
print('A ordem de apresentação é:\n'
      '1º - {}\n'
      '2º - {}\n'
      '3º - {}\n'
      '4º - {}'.format(alunos[0],alunos[1],alunos[2],alunos[3]))