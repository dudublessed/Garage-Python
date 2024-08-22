from Vehicles import Vehicles

class Carro (Vehicles):
    
    def __init__(self, marca, modelo, ano, combustivel, quilometragem, capacidade_mala):
        super().__init__(marca, modelo, ano, combustivel, quilometragem)
        self._capacidade_mala = capacidade_mala
    
    
    def exibir_informacoes(self):
        print(" ")
        print("_______________")
        print(" ")
        return (f"Carro:\n"
                f"Marca: {self._marca}\n"
                f"Modelo: {self._modelo}\n"
                f"Fabricação: {self._ano}\n"
                f"Combustível: {self._combustivel} litros\n"
                f"Quilometragem: {self._quilometragem} km \n"
                f"Capacidade da Mala: {self._capacidade_mala} litros \n"
                f"Autonomia: {self.calcular_autonomia()} km \n"
                f"Custo operacional: R$ {self.calcular_custo_operacional()} \n"                               
                f" \n"
                f"_______________\n"
                f" \n")

        