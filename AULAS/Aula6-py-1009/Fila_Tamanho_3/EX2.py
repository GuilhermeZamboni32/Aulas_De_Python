# Fila Circular
class FilaCircular:
    """Classe que simula uma Fila Circular."""
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.head = 0
        self.tail = 0
        self.elementos = 0

    def enfileirar(self, item):
        if self.elementos == self.tamanho:
            print("Fila cheia! Não é possível inserir.")
            return

        self.fila[self.tail] = item
        self.tail = (self.tail + 1) % self.tamanho
        self.elementos += 1
        print(f"Inserido '{item}'. Head: {self.head}, Tail: {self.tail}")

    def desenfileirar(self):
        if self.elementos == 0:
            print("Fila vazia! Não é possível remover.")
            return None

        item_removido = self.fila[self.head]
        self.fila[self.head] = None
        self.head = (self.head + 1) % self.tamanho
        self.elementos -= 1
        print(f"Removido '{item_removido}'. Head: {self.head}, Tail: {self.tail}")
        return item_removido

    def exibir_ponteiros(self):
        print(f"Valor final dos ponteiros -> Head: {self.head}, Tail: {self.tail}")


print("2. Fila Circular:")
print("-" * 20)

#  fila de tamanho 3
fila_circular = FilaCircular(3)
print(f"Estado Inicial -> Head: {fila_circular.head}, Tail: {fila_circular.tail}")
print("-" * 20)


# Inserindo 3 elementos
fila_circular.enfileirar('A')
fila_circular.enfileirar('B')
fila_circular.enfileirar('C')
print("-" * 20)


# Removendo 1 elemento
fila_circular.desenfileirar()
print("-" * 20)


# Resultado final
fila_circular.exibir_ponteiros()
print("\n" + "="*40 + "\n")