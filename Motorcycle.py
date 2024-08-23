from Vehicles import Vehicles

class Moto (Vehicles):
    
    def __init__(self, marca, modelo, ano, combustivel, quilometragem, custo, cilindrada, tipo):
        super().__init__(marca, modelo, ano, combustivel, quilometragem, custo)
        self._cilindrada = cilindrada
        self._tipo = tipo
    
    
    def calcular_velocidade_maxima(self):
        velocidade_base = 200 # in km/h
        
        if self._tipo.lower() == "sport":
            velocidade_maxima = velocidade_base + (self._cilindrada / 10)
            
        elif self._tipo.lower() == "adventure":
            velocidade_maxima = velocidade_base + (self._cilindrada / 15)
            
        elif self._tipo.lower() == "roadster":
            velocidade_maxima = velocidade_base + (self._cilindrada / 12)
            
        elif self._tipo.lower() == "cruiser":
            velocidade_maxima = velocidade_base + (self._cilindrada / 18)
            
        else:
            velocidade_maxima = velocidade_base + (self._cilindrada / 20)
            
        return velocidade_maxima
    
    def mostrar_tabela(self):
        print(" ")
        print("_______________")
        print(" ")
        return (f"{self._modelo} \n"
                f"Fabricação: {self._ano} \n"
                f"Combustível: {self._combustivel} litros \n"
                f"Quilometragem: {self._quilometragem} km \n"
                f"Custo: R$ {self._custo} \n"
                f"Cilindrada: {self._cilindrada} cc \n"
                f"Tipo: {self._tipo} \n"
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
                f"Cilindrada: {self._cilindrada} cc \n"
                f"Tipo: {self._tipo} \n"
                f"Autonomia: {self.calcular_autonomia()} km \n"
                f"Custo operacional: R$ {self.calcular_custo_operacional()} \n"     
                f"Velocidade Máxima: {self.calcular_velocidade_maxima()} km/h \n"                   
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
                f"Cilindrada: {self._cilindrada} cc \n"
                f"Tipo: {self._tipo} \n"
                f"Autonomia: {self.calcular_autonomia()} km \n"
                f"Custo operacional: R$ {self.calcular_custo_operacional()} \n"     
                f"Velocidade Máxima: {self.calcular_velocidade_maxima()} km/h \n"                   
                f" \n"
                f"_______________\n")


# Modelos de Moto

BMW = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Cilindrada / Tipo
    Moto("BMW", "S 1000 RR", 2024, 16.5, 0, 150000, 999, "Sport"),
    Moto("BMW", "R 1300 GS", 2024, 30, 0, 160000, 1301, "Adventure"),
    Moto("BMW", "G 310 R", 2024, 11, 0, 40000, 313, "Roadster"),
]


Yamaha = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Cilindrada / Tipo
    Moto("Yamaha", "Tracer 900 GT ABS", 2024, 18, 0, 65000, 890, "Adventure"),
    Moto("Yamaha", "R3 ABS", 2025, 14, 0, 35000, 321, "Sport"),
    Moto("Yamaha", "R15 ABS", 2024, 11, 0, 25000, 155, "Sport")
]


Kawasaki = [
    # Marca / Modelo / Ano / Combustível / Quilometragem / Custo / Cilindrada / Tipo
    Moto("Kawasaki", "Ninja 650", 2024, 15, 0, 45000, 649, "Sport"),
    Moto("Kawasaki", "Ninja 300", 2024, 17, 0, 30000, 269, "Sport"),
    Moto("Kawasaki", "Vulcan S", 2025, 14, 0, 40000, 649, "Cruiser")
]