from Vehicles import Vehicles

class Caminhao (Vehicles):
    
    def __init__(self, marca, modelo, ano, combustivel, quilometragem, peso, capacidade_carga, numero_eixos, capacidade_eixo):
        super().__init__(marca, modelo, ano, combustivel, quilometragem)
        self._capacidade_carga = capacidade_carga
        self._numero_eixos = numero_eixos
        self._capacidade_eixo = capacidade_eixo
        self._peso = peso

    def calcular_peso_maximo(self):
        peso_max = self._peso + self._capacidade_carga
        return peso_max
    
    
    def calcular_carga_maxima(self):
        carga_max = self.calcular_peso_maximo() - self._peso
        return carga_max
        
        
    def calcular_peso_atual(self):
        peso_atual_caminhao = (self._numero_eixos * self._capacidade_eixo) - self._capacidade_carga
        return peso_atual_caminhao
    
    
    def exibir_informacoes(self):
        print(" ")
        print("_______________")
        print(" ")
        return (f"Caminhão:\n"
                f"Marca: {self._marca}\n"
                f"Modelo: {self._modelo}\n"
                f"Fabricação: {self._ano}\n"
                f"Combustível: {self._combustivel} litros\n"
                f"Quilometragem: {self._quilometragem} km \n"
                f"Peso Vazio: {self._peso} kg\n"
                f"Peso Atual: {self.calcular_peso_atual()} kg\n"
                f"Peso Máximo: {self.calcular_peso_maximo()} kg\n"
                f"Número de eixos: {self._numero_eixos} \n"
                f"Capacidade de eixo: {self._capacidade_eixo} \n"
                f"Capacidade de Carga: {self.calcular_carga_maxima()} litros \n"    
                f"Autonomia: {self.calcular_autonomia()} km \n"
                f"Custo operacional: R$ {self.calcular_custo_operacional()} \n"                         
                f" \n"
                f"_______________\n"
                f" \n")
