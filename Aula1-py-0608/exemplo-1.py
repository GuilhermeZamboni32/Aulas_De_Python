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