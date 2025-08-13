'''
crie a estrutura Livro com:
titulo,autor,ano,preco
implemente com dataclass e classs
mostre os dados
5 livros diferentes

desafio I: função/metodo recente() (<5anos)
desafio II: função/metodo caro() (>media)
'''

from dataclasses import dataclass

@dataclass

class Livro:
    titulo: str
    autor: str
    ano: int
    preco: float
    
livro1 = Livro("O Senhor dos Anéis", "Golummm", 1954, 39.90)
print('Título do livro:', livro1.titulo)
print('Autor do livro:', livro1.autor)
print('Ano do livro:', livro1.ano)
print('Preço do livro:', livro1.preco)
print('//////////////////////////////////////////////////////')

livro2 = Livro("Assasine o credito", "Moura", 2004, 50.99)
print('Título do livro:', livro2.titulo)
print('Autor do livro:', livro2.autor)
print('Ano do livro:', livro2.ano)
print('Preço do livro:', livro2.preco)
print('//////////////////////////////////////////////////////')

livro3 = Livro("O lobbit", "Monteiro Lobato", 1937, 29.90)
print('Título do livro:', livro3.titulo)
print('Autor do livro:', livro3.autor)
print('Ano do livro:', livro3.ano)
print('Preço do livro:', livro3.preco)
print('//////////////////////////////////////////////////////')

livro4 = Livro("No olho do sue botão", " kenga de Gala", 2018, 35.90)
print('Título do livro:', livro4.titulo)
print('Autor do livro:', livro4.autor)
print('Ano do livro:', livro4.ano)
print('Preço do livro:', livro4.preco)
print('//////////////////////////////////////////////////////')

livro5 = Livro("two pichii", "Atinro o Ouooda", 2025, 100.00)
print('Título do livro:', livro5.titulo)
print('Autor do livro:', livro5.autor)
print('Ano do livro:', livro5.ano)
print('Preço do livro:', livro5.preco)
print('//////////////////////////////////////////////////////')



# desafio I: função/metodo recente() (<5anos)
def recente(livro: Livro) -> bool:
    from datetime import datetime
    ano_atual = datetime.now().year
    return (ano_atual - livro.ano) < 5

def livros_recentes(livros: list[Livro]) -> list[Livro]:
    return [livro for livro in livros if recente(livro)]



# desafio II: função/metodo caro() (>media)
def caro(livros: list[Livro]) -> list[Livro]:
    media = sum(livro.preco for livro in livros) / len(livros)
    return [livro for livro in livros if livro.preco > media]
livros = [livro1, livro2, livro3, livro4, livro5]


print('Livros recentes:', livros_recentes(livros))
print('Livros caros:', caro(livros))

