'''
1. Ler e guardar 20 notas do aluno.
Desafio Nivel 1: Calcule média, maior e menor nota

2. Ler e guardar notas de alunos(4 alunos, com 5 notas cada)
Desafio Nivel 2: Notas acima da média'''


from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    media: float


aluno = Aluno("Felipe", 44, 9.2)
print('Nome do aluno:', aluno.nome)
print('Idade do aluno:', aluno.idade)
print('Média do aluno:', aluno.media)

print('Dados do aluno:', aluno)
print('Dados do aluno:', aluno.__dict__)
