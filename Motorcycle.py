from Vehicles import Vehicles

class Moto (Vehicles):
    
    def __init__(self, marca, modelo, ano, combustivel, quilometragem, cilindrada, tipo):
        super().__init__(marca, modelo, ano, combustivel, quilometragem)
        self._cilindrada = cilindrada
        self._tipo = tipo
    
    
    def calcular_velocidade_maxima(self):
        velocidade_base = 200 # in km/h
        
        if self._tipo.lower() == "esportiva":
            velocidade_maxima = velocidade_base + (self._cilindrada / 10)
            
        elif self._tipo.lower() == "cruiser":
            velocidade_maxima = velocidade_base + (self._cilindrada / 12)
            
        elif self._tipo.lower() == "naked":
            velocidade_maxima = velocidade_base + (self._cilindrada / 15)
            
        else:
            velocidade_maxima = velocidade_base + (self._cilindrada / 20)
            
        return velocidade_maxima
    
    
    def exibir_informacoes(self):
        print(" ")
        print("_______________")
        print(" ")
        return (f"Moto:\n"
                f"Marca: {self._marca}\n"
                f"Modelo: {self._modelo}\n"
                f"Fabricação: {self._ano}\n"
                f"Combustível: {self._combustivel} litros\n"
                f"Quilometragem: {self._quilometragem} km \n"
                f"Cilindrada: {self._cilindrada} cc \n"
                f"Tipo: {self._tipo} \n"
                f"Autonomia: {self.calcular_autonomia()} km \n"
                f"Custo operacional: R$ {self.calcular_custo_operacional()} \n"     
                f"Velocidade Máxima: {self.calcular_velocidade_maxima()} km/h \n"                   
                f" \n"
                f"_______________\n"
                f" \n")
        