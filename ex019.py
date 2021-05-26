#Programa que ajude a sortear 1 aluno entre 4

import random

aluno1 = input('Digite o nome de um aluno: ').title()
aluno2 = input('Digite o nome de um aluno: ').title()
aluno3 = input('Digite o nome de um aluno: ').title()
aluno4 = input('Digite o nome de um aluno: ').title()
alunos = [aluno1, aluno2, aluno3, aluno4]

alunos.sort()
print(random.choice(alunos))

