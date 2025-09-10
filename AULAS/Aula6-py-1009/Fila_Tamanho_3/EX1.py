# a Lista Encadeada
class No:
    """Classe que representa um nó na lista encadeada."""
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade
        self.proximo = None  

    def __repr__(self):
        
        next_nome = self.proximo.nome if self.proximo else "NIL"
        return f"( {self.nome} ({self.prioridade}) ) ---> {next_nome}"


#  lista inicial 
no_joao = No("João", 1)
no_carlos = No("Carlos", 2)
no_ana = No("Ana", "NIL") 

# Ligando os ponteiros
no_joao.proximo = no_carlos
no_carlos.proximo = no_ana

print("1. Lista Encadeada:")
print("-" * 20)
print("Lista Original:")
print(f"Ponteiro de João: {no_joao}")
print(f"Ponteiro de Carlos: {no_carlos}")
print("-" * 20)


#  Removendo o nó Carlos 
print("1.1. Removendo o nó 'Carlos'...")
print("Atualizando o ponteiro de 'João' para apontar para 'Ana'.\n")

no_joao.proximo = no_ana

print("Lista Após a Remoção:")
print(f"Ponteiro de João: {no_joao}")
print("-" * 20)


#  Reinserindo o nó Carlos 
print("1.2. Reinserindo o nó 'Carlos'...")
print("Atualizando o ponteiro de 'Carlos' para 'Ana' e o de 'João' para 'Carlos'.\n")
no_carlos.proximo = no_ana 
no_joao.proximo = no_carlos 

print("Lista Após a Reinserção:")
print(f"Ponteiro de João: {no_joao}")
print(f"Ponteiro de Carlos: {no_carlos}")
print("\n" + "="*40 + "\n")