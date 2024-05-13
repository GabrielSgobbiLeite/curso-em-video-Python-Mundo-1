import random


a = input('digite um nome de aluno:')
b = input('digite outro nome:')
c = input('digite outro nome:')
d = input('ditite outro nome:')

lista_de_aluno=a,b,c,d

aluno = random.sample(lista_de_aluno,4)

print(f'o aluno escolhido foi {aluno}')