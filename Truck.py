from Vehicles import Vehicles

class Caminhao (Vehicles):
    
    def __init__(self, marca, modelo, ano, combustivel, quilometragem, custo, peso, capacidade_carga, numero_eixos, capacidade_eixo):
        super().__init__(marca, modelo, ano, combustivel, quilometragem, custo)
        self._peso = peso
        self._capacidade_carga = capacidade_carga
        self._numero_eixos = numero_eixos
        self._capacidade_eixo = capacidade_eixo


    def calcular_peso_maximo(self):
        peso_max = self._peso + self._capacidade_carga
        return peso_max
    
    
    def calcular_carga_maxima(self):
        carga_max = self.calcular_peso_maximo() - self._peso
        return carga_max
        
        
    def calcular_peso_atual(self):
        peso_atual_caminhao = (self._numero_eixos * self._capacidade_eixo) - self._capacidade_carga
        return peso_atual_caminhao
    
    def mostrar_tabela(self):
        print(" ")
        print("_______________")
        print(" ")
        return (f"{self._modelo} \n"
                f"Fabricação: {self._ano} \n"
                f"Combustível: {self._combustivel} litros \n"
                f"Quilometragem: {self._quilometragem} km \n"
                f"Custo: R$ {self._custo} \n"
                f"Peso: {self._peso} kg \n"
                f"Capacidade de Carga: {self.calcular_carga_maxima()} litros \n"
                f"Número de eixos: {self._numero_eixos} \n"
                f"Capacidade de eixo: {self._capacidade_eixo} kg \n"
                f" \n"
                f"_______________\n")
    
    
    def exibir_informacoes(self):
        print(" ")
        print("_______________")
        print(" ")
        return (f"Informações do {self._modelo}: \n"
                f" \n"
                f"Marca: {self._marca} \n"
                f"Fabricação: {self._ano} \n"
                f"Combustível: {self._combustivel} litros \n"
                f"Quilometragem: {self._quilometragem} km \n"
                f"Custo: R$ {self._custo} \n"
                f"Peso Vazio: {self._peso} kg \n"
                f"Peso Atual: {self.calcular_peso_atual()} kg \n"
                f"Peso Máximo: {self.calcular_peso_maximo()} kg \n"
                f"Número de eixos: {self._numero_eixos} \n"
                f"Capacidade de eixo: {self._capacidade_eixo} kg \n"
                f"Capacidade de Carga: {self.calcular_carga_maxima()} litros \n"    
                f"Autonomia: {self.calcular_autonomia()} km \n"
                f"Custo operacional: R$ {self.calcular_custo_operacional()} \n"                         
                f" \n"
                f"_______________\n")


    def exibir_adquiridos(self, cliente):
        print(" ")
        print("_______________")
        print(" ")
        return (f"{self._marca} {self._modelo} de {cliente.nome}: \n"
                f" \n"
                f"Fabricação: {self._ano} \n"
                f"Combustível: {self._combustivel} litros \n"
                f"Quilometragem: {self._quilometragem} km \n"
                f"Custo: R$ {self._custo} \n"
                f"Peso Vazio: {self._peso} kg \n"
                f"Peso Atual: {self.calcular_peso_atual()} kg \n"
                f"Peso Máximo: {self.calcular_peso_maximo()} kg \n"
                f"Número de eixos: {self._numero_eixos} \n"
                f"Capacidade de eixo: {self._capacidade_eixo} kg \n"
                f"Capacidade de Carga: {self.calcular_carga_maxima()} litros \n"    
                f"Autonomia: {self.calcular_autonomia()} km \n"
                f"Custo operacional: R$ {self.calcular_custo_operacional()} \n"                         
                f" \n"
                f"_______________\n")
        

# Modelos de Caminhao

Mercedes = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Peso / Capacidade de Carga / Numero de Eixos / Capacidade de Eixo
    Caminhao("Mercedes-Benz", "Acello BlueTec 6", 2024, 100, 0, 250000, 3500, 5500, 2, 2750),
    Caminhao("Mercedes-Benz", "Atego", 2024, 150, 0, 350000, 6000, 8000, 3, 2700),
    Caminhao("Mercedes-Benz", "Arocs", 2024, 300, 0, 800000, 10000, 30000, 4, 7500)
]


Volvo = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Peso / Capacidade de Carga / Numero de Eixos / Capacidade de Eixo
    Caminhao("Volvo", "FMX", 2024, 900, 0, 900000, 12000, 30000, 4, 7500),
    Caminhao("Volvo", "FH", 2024, 1000, 0, 800000, 9000, 20000, 4, 5000),
    Caminhao("Volvo", "VM", 2024, 300, 0, 400000, 8000, 10000, 3, 3333)
]

Foton = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Peso / Capacidade de Carga / Numero de Eixos / Capacidade de Eixo
    Caminhao("Foton", "Auman", 2024, 300, 0, 350000, 8000, 15000, 4, 3750),
    Caminhao("Foton", "Aumark", 2024, 100, 0, 200000, 3500, 5500, 2, 2750),
    Caminhao("Foton", "Ollin", 2024, 70, 0, 180000, 2800, 4500, 2, 2250)
]