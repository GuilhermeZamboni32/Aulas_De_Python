import sys

# Classe para representar um nó da Árvore AVL
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # A altura de um novo nó (folha) é 1

# Classe para a Árvore AVL
class AVLTree:
    def __init__(self):
        self.root = None

    # Função para obter a altura de um nó
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    # Função para obter o Fator de Balanceamento (FB) de um nó [cite: 35]
    def getBalance(self, node):
        if not node:
            return 0
        # FB(node) = altura(esq) - altura(dir)
        return self.getHeight(node.left) - self.getHeight(node.right)

    # Rotação Simples à Direita [cite: 46]
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Realiza a rotação
        y.right = z
        z.left = T3

        # Atualiza as alturas
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Retorna a nova raiz da sub-árvore
        return y

    # Rotação Simples à Esquerda [cite: 48]
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Realiza a rotação
        y.left = z
        z.right = T2

        # Atualiza as alturas
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Retorna a nova raiz da sub-árvore
        return y

    # Função principal de inserção
    def insert(self, key):
        print(f"--- Inserindo o valor {key} ---")
        self.root = self._insert(self.root, key)
        self.printTree()
        print("-" * 25)


    # Função recursiva auxiliar para inserir um nó e balancear a árvore
    def _insert(self, root, key):
        # 1. Inserção padrão de uma Árvore Binária de Busca
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        # 2. Atualiza a altura do nó ancestral [cite: 38]
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3. Calcula o Fator de Balanceamento para verificar se o nó ficou desbalanceado
        balance = self.getBalance(root)

        # 4. Se o nó estiver desbalanceado, aplica uma das 4 rotações

        # Caso Esquerda-Esquerda (Rotação Direita) [cite: 46]
        # FB do nó é +2 e o FB do filho esquerdo é >= 0
        if balance > 1 and self.getBalance(root.left) >= 0:
            print(f"Rotação Direita no nó {root.key}")
            return self.rightRotate(root)

        # Caso Direita-Direita (Rotação Esquerda) [cite: 48]
        # FB do nó é -2 e o FB do filho direito é <= 0
        if balance < -1 and self.getBalance(root.right) <= 0:
            print(f"Rotação Esquerda no nó {root.key}")
            return self.leftRotate(root)

        # Caso Esquerda-Direita [cite: 50]
        # FB do nó é +2 e o FB do filho esquerdo é < 0
        if balance > 1 and self.getBalance(root.left) < 0:
            print(f"Rotação Esquerda-Direita (Esquerda em {root.left.key}, Direita em {root.key})")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Caso Direita-Esquerda [cite: 52]
        # FB do nó é -2 e o FB do filho direito é > 0
        if balance < -1 and self.getBalance(root.right) > 0:
            print(f"Rotação Direita-Esquerda (Direita em {root.right.key}, Esquerda em {root.key})")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    
    # Função para imprimir a árvore (percurso em pré-ordem)
    def printTree(self):
        print("Árvore atual:")
        self._printTree(self.root, "", True)

    def _printTree(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            
            fb = self.getBalance(currPtr)
            print(f"{currPtr.key} (FB={fb})")

            self._printTree(currPtr.left, indent, False)
            self._printTree(currPtr.right, indent, True)

# --- Execução do Exercício ---
if __name__ == '__main__':
    myTree = AVLTree()
    
    # Conjunto de dados a ser inserido sequencialmente [cite: 55]
    keys = [11, 23, 47, 35, 24, 1, 2]

    for key in keys:
        myTree.insert(key)