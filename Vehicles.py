from abc import ABC, abstractmethod

class Vehicles(ABC):
    
    def __init__(self, marca, modelo, ano, combustivel, quilometragem):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._combustivel = combustivel
        self._quilometragem = quilometragem
        
    
    def calcular_consumo(self):
        consumo = (self._combustivel / self._quilometragem) * 100
        return consumo
    
    
    def calcular_autonomia(self):
        consumo = self.calcular_consumo()
        autonomia = (self._combustivel / consumo) * 100
        return autonomia


    def calcular_custo_operacional(self):
        preco_combustivel = 5
        eficiencia = self.calcular_consumo()
        custo = (self._quilometragem / 100) * eficiencia * preco_combustivel
        return custo
    
    
    def exibir_informacoes(self):
        pass


        
        
        
