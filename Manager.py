from Vehicles import Vehicles

class Manager:
    
    def __init__(self):
        self.veiculos = []
        
        
            
    def adicionar_veiculo(self, veiculo):
        if isinstance (veiculo, Vehicles):
            self.veiculos.append(veiculo)
            
    
    def remover_veiculo(self, veiculo):
        if isinstance (veiculo, Vehicles) and veiculo in self.veiculos:
            self.veiculos.remove(veiculo)
            
            
    def listar_veiculos (self, cliente):
        for veiculo in self.veiculos:
            print(veiculo.exibir_adquiridos(cliente))