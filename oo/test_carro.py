from unittest import TestCase
from carro import Carro, Motor

class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    
    def test_acelerar(self):
        motor = Motor()
        velocidade = motor.velocidade + 1
        motor.acelerar()
        self.assertEqual(motor.velocidade, velocidade)
