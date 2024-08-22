from Manager import Manager
from Vehicles import Vehicles
from Car import Carro
from Motorcycle import Moto
from Truck import Caminhao

import sys



if __name__ == "__main__":
    gerenciador = Manager()
    
    print("Bem-vindo a Garagem Python! Registre aqui os seus veículos!")
    
    start_decision = input("Gostaria de registrar um veículo? Digite 'Sim' ou 'Nao' \n")
    
    while True:
        if start_decision.lower() == "sim":
            print("Perfeito! Vou pedir algumas informações sobre o veículo para que tudo seja registrado corretamente.")
            break
        
        elif start_decision.lower() == "nao": 
            print("Tudo-bem! Muito obrigado por utilizar a Garagem Python!")
            sys.exit()
        
        else: 
            print("Opção inválida. Tente novamente.")
            continue
     
    while True:   
        vehicle_type = input("Qual o tipo de veículo? Carro, Moto ou Caminhao? \n")
        if vehicle_type.lower() == "carro":
            vehicle_chosen = Carro
            break
        
        elif vehicle_type.lower() == "moto":
            vehicle_chosen = Moto
            break
            
        elif vehicle_type.lower() == "caminhao":
            vehicle_chosen = Caminhao
            break
            
        else: 
            print("Opção inválida. Tente novamente.")
            continue