from Vehicles import Vehicles

class Carro (Vehicles):
    
    def __init__(self, marca, modelo, ano, combustivel, quilometragem, custo, capacidade_mala):
        super().__init__(marca, modelo, ano, combustivel, quilometragem, custo)
        self._capacidade_mala = capacidade_mala


    def mostrar_tabela(self):
        print(" ")
        print("_______________")
        print(" ")
        return (f"{self._modelo} \n"
                f"Fabricação: {self._ano} \n"
                f"Combustível: {self._combustivel} litros \n"
                f"Quilometragem: {self._quilometragem} km \n"
                f"Custo: R$ {self._custo} \n"
                f"Capacidade da Mala: {self._capacidade_mala} litros \n"
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
                f"Capacidade da Mala: {self._capacidade_mala} litros \n"
                f"Autonomia: {self.calcular_autonomia()} km \n"
                f"Custo operacional: R$ {self.calcular_custo_operacional()} \n"                               
                f" \n"
                f"_______________\n"
                f" \n")
        

# Modelos de Carro

Porsche = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Capacidade Mala
    Carro("Porsche","718 Cayman", 2024, 64, 0, 535000, 275),
    Carro("Porsche","911 Turbo", 2024, 64, 0, 1505000, 132),
    Carro("Porsche","Panamera 4 E-Hybrid", 2025, 75, 0, 803000, 495),
    Carro("Porsche","Cayenne GTS", 2025, 0, 75, 930000, 600)
]

Toyota = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Capacidade Mala
    Carro("Toyota", "Corolla GLi", 2024, 50, 20.000, 130000, 470),
    Carro("Toyota", "Hilux GR-Sport", 2024, 80, 20.000, 350000, 1200),
    Carro("Toyota", "RAV4 SX Connect Hybrid", 2024, 55, 30.000, 310000, 580)
]

Ferrari = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Capacidade Mala
    Carro("Ferrari", "LaFerrari", 2013, 85, 0, 8000000, 100),
    Carro("Ferrari", "SF90 Spider", 2020, 65, 0, 3500000, 80),
    Carro("Ferrari", "SF90 Stradale", 2020, 65, 0, 2750000, 80)
]
        
Nissan = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Capacidade Mala
    Carro("Nissan", "Kicks", 2024, 41, 40.000, 100000, 432),
    Carro("Nissan", "Sentra", 2024, 50, 50.000, 120000, 500),
    Carro("Nissan", "Frontier", 2024, 80, 0, 270000, 1100)
]

Audi = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Capacidade Mala
    Carro("Audi", "RS 6 Avant", 2024, 73, 0, 1300000, 565),
    Carro("Audi", "A3 Sportback", 2024, 50, 0, 370000, 380),
    Carro("Audi", "A4 Sedan", 2024, 54, 0, 340000, 460),
]

Hyundai = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Capacidade Mala
    Carro("Hyundai", "Creta", 2024, 55, 30.000, 170000, 431),
    Carro("Hyundai", "HB20", 2024, 50, 40.000, 70000, 300),
    Carro("Hyundai", "Palisade", 2024, 71, 0, 400000, 311)
]