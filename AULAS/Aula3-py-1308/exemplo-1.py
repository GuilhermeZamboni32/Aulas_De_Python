'''
EXERCICIO FILAS
______________________________________________

Implemente uma fila para atendimento
Simule clientes chegando e sendo atendidos
Mostre o estado da fila após cada operação
______________________________________________

chega cliente a cada 2s
tempo de atendimento 10s

cliente
nome,protocolo,hora chagada,hora atendimento,hora saida

caixa
fila

def atendimento
def entra na fila
def mostra estado
'''


from datetime import datetime, timedelta
from time import sleep
from dataclasses import dataclass



@dataclass

class Cliente:
    nome: str
    protocolo: str
    hora_chegada: datetime
    hora_atendimento: datetime = None
    hora_saida: datetime = None

class Caixa:
    def __init__(self):
        self.fila: list[Cliente] = []

    def entra_na_fila(self, cliente: Cliente):
        self.fila.append(cliente)
        print(f"Cliente {cliente.nome} entrou na fila com protocolo {cliente.protocolo}.")