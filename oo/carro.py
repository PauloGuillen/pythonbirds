'''
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.acelerar()
>>> motor.acelerar()
>>> motor.frear()
>>> motor.velocidade
1
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.valor = 'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
1


'''

class Carro:
    def __init__(self, direcao, motor) -> None:
        self.direcao = direcao
        self.motor = motor
    
    def calcular_velocidade(self):
        return self.motor.velocidade

class Motor:
    def __init__(self) -> None:
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 1
    
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)

NORTE ='Norte'
LESTE = 'Leste'
SUL = 'Sul' 
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE }
    
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL }
    
    def __init__(self):
        self.valor = NORTE
    
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]




