class Livro {
  constructor(titulo, autor, ano, preco) {
    this.titulo = titulo;
    this.autor = autor;
    this.ano = ano;
    this.preco = preco;
  }

  // Desafio I: método para saber se o livro é recente (<5 anos)
  recente() {
    const anoAtual = new Date().getFullYear();
    return (anoAtual - this.ano) < 5;
  }
}

// Criando os 5 livros
const livro1 = new Livro("O Senhor dos Anéis", "Golummm", 1954, 39.90);
const livro2 = new Livro("Assasine o credito", "Moura", 2004, 50.99);
const livro3 = new Livro("O lobbit", "Monteiro Lobato", 1937, 29.90);
const livro4 = new Livro("No olho do sue botão", "kenga de Gala", 2018, 35.90);
const livro5 = new Livro("two pichii", "Atinro o Ouooda", 2025, 100.00);

// Função para mostrar dados do livro
function mostrarLivro(livro) {
  console.log(`Título do livro: ${livro.titulo}`);
  console.log(`Autor do livro: ${livro.autor}`);
  console.log(`Ano do livro: ${livro.ano}`);
  console.log(`Preço do livro: R$${livro.preco.toFixed(2)}`);
  console.log('---');
}

// Mostrar todos os livros
const livros = [livro1, livro2, livro3, livro4, livro5];
livros.forEach(mostrarLivro);

// Desafio II: função para retornar livros caros (preço > média)
function livrosCaros(listaLivros) {
  const media = listaLivros.reduce((acc, livro) => acc + livro.preco, 0) / listaLivros.length;
  return listaLivros.filter(livro => livro.preco > media);
}

// Função para filtrar livros recentes (<5 anos)
function livrosRecentes(listaLivros) {
  return listaLivros.filter(livro => livro.recente());
}

console.log('Livros recentes (<5 anos):');
livrosRecentes(livros).forEach(mostrarLivro);

console.log('Livros caros (> preço médio):');
livrosCaros(livros).forEach(mostrarLivro);
