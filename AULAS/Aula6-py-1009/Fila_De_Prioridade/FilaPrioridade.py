import heapq

# A fila de prioridade será representada por uma lista (min-heap)
fila_de_prioridade = []

# Lista de pacientes na ordem em que chegaram
pacientes_chegada = [
    {"nome": "João", "prioridade": 3},
    {"nome": "Maria", "prioridade": 1},
    {"nome": "Pedro", "prioridade": 4},
    {"nome": "Ana", "prioridade": 2},
]

print("--- Simulação da Chegada de Pacientes ---")

# Adicionando pacientes à fila de prioridade
# Usamos uma tupla (prioridade, nome) porque o heapq ordena pelo primeiro item.
for paciente in pacientes_chegada:
    nome = paciente["nome"]
    prioridade = paciente["prioridade"]
    
    print(f"Chegou: {nome} (Prioridade: {prioridade})")
    heapq.heappush(fila_de_prioridade, (prioridade, nome))

print("\nTodos os pacientes deram entrada.")
print(f"Estado atual da fila interna (heap): {fila_de_prioridade}")
print("-" * 40)


# --- Processo de Atendimento ---
print("\n--- Ordem de Atendimento (do mais urgente para o menos urgente) ---")

ordem_final = []
posicao = 1

# Enquanto a fila não estiver vazia, removemos o paciente de maior prioridade
while fila_de_prioridade:
    # heappop() sempre remove e retorna o menor item (neste caso, a menor prioridade)
    prioridade_atendido, nome_atendido = heapq.heappop(fila_de_prioridade)
    
    print(f"{posicao}º a ser atendido: {nome_atendido} (Prioridade: {prioridade_atendido})")
    ordem_final.append(nome_atendido)
    posicao += 1

print("-" * 40)

# Imprime um resumo final
print("\nResumo da ordem de atendimento:")
print(" -> ".join(ordem_final))