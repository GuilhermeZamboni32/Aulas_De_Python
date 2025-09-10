#  Fila e Pilha
from collections import deque

print("3. Fila e Pilha:")
print("-" * 20)

#  dados iniciais
fila = deque()  
pilha = []      
dado = None

# Executando as operações em sequência
print(f"Início:      Fila={list(fila)}, Pilha={pilha}")

# enfileirar(1)
fila.append(1)
print(f"enfileirar(1): Fila={list(fila)}, Pilha={pilha}")

# enfileirar(2)
fila.append(2)
print(f"enfileirar(2): Fila={list(fila)}, Pilha={pilha}")

# dado = desenfileirar()
dado = fila.popleft()
print(f"desenfileirar(): Fila={list(fila)}, Pilha={pilha}, dado={dado}")

# enfileirar(3)
fila.append(3)
print(f"enfileirar(3): Fila={list(fila)}, Pilha={pilha}")

# dado = desenfileirar()
dado = fila.popleft()
print(f"desenfileirar(): Fila={list(fila)}, Pilha={pilha}, dado={dado}")

# empilhar(dado)
pilha.append(dado)
print(f"empilhar({dado}):   Fila={list(fila)}, Pilha={pilha}")

# desempilhar()
item_desempilhado = pilha.pop()
print(f"desempilhar():   Fila={list(fila)}, Pilha={pilha}, removido={item_desempilhado}")

print("-" * 20)
print("Resultado Final:")
print(f"-> Fila: {list(fila)}")
print(f"-> Pilha: {pilha if pilha else 'Vazia'}")