import random
import time

class SimulacaoSemaforo:
    def __init__(self, modo_inteligente=False):
        self.modo_inteligente = modo_inteligente

        self.fila_principal = 0
        self.fila_secundaria = 0

        self.verde_principal = True
        self.tempo_no_estado_atual = 0

        self.total_tempo_espera = 0
        self.carros_atendidos = 0

    def passo(self):

        if random.random() < 0.3:
            self.fila_principal += 1
        if random.random() < 0.05:
            self.fila_secundaria += 1

        if not self.modo_inteligente:
            self.logica_burra_antiga()
        else:
            self.logica_inteligente_automato()

        if self.verde_principal and self.fila_principal > 0:
            self.fila_principal -= 1
            self.carros_atendidos += 1
        elif not self.verde_principal and self.fila_secundaria > 0:
            self.fila_secundaria -= 1
            self.carros_atendidos += 1

        self.total_tempo_espera += (self.fila_principal + self.fila_secundaria)
        self.tempo_no_estado_atual += 1

    def logica_burra_antiga(self):

        limite = 40 if self.verde_principal else 20

        if self.tempo_no_estado_atual >= limite:
            self.trocar_sinal()

    def logica_inteligente_automato(self):

        if self.verde_principal and self.fila_principal == 0 and self.fila_secundaria > 0:
            self.trocar_sinal()

        elif not self.verde_principal and self.fila_secundaria == 0:
            self.trocar_sinal()

        elif self.verde_principal and self.fila_secundaria > 10:
             self.trocar_sinal()

    def trocar_sinal(self):
        self.verde_principal = not self.verde_principal
        self.tempo_no_estado_atual = 0

#  1 hora (3600 segundos)
DURACAO = 3600
print("INICIANDO SIMULAÇÃO")
# modelo antigo
random.seed(42)
sistema_antigo = SimulacaoSemaforo(modo_inteligente=False)
for _ in range(DURACAO):
    sistema_antigo.passo()
# modelo novo
random.seed(42)
sistema_novo = SimulacaoSemaforo(modo_inteligente=True)
for _ in range(DURACAO):
    sistema_novo.passo()

print(f"\nRESULTADOS APÓS {DURACAO} SEGUNDOS DE SIMULAÇÃO:")
print("-" * 50)
print(f"MODELO ANTIGO (Temporizador Fixo):")
print(f"Tempo total desperdiçado em fila: {sistema_antigo.total_tempo_espera} segundos acumulados")
print("-" * 50)
print(f"MODELO NOVO (Autômato Inteligente):")
print(f"Tempo total desperdiçado em fila: {sistema_novo.total_tempo_espera} segundos acumulados")
print("-" * 50)

melhoria = (sistema_antigo.total_tempo_espera - sistema_novo.total_tempo_espera)
porcentagem = (melhoria / sistema_antigo.total_tempo_espera) * 100

print(f"CONCLUSÃO:")
print(f"Reduziu o tempo de espera em {porcentagem:.2f}%!")