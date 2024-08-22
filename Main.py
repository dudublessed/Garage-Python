from Manager import Manager
from Vehicles import Vehicles
from Car import Carro, Porsche, Toyota, Ferrari, Nissan, Audi, Hyundai
from Motorcycle import Moto, BMW, Yamaha, Kawasaki
from Truck import Caminhao, Mercedes, Volvo, Foton
from Client import Cliente

import random
import sys

if __name__ == "__main__":
    gerenciador = Manager()
    
    # Generates a random value of the user money
    nubank = random.randint(25000, 3000000)
    itau = random.randint(25000, 300000)
    bradesco = random.randint(25000, 1000000)
    santander = random.randint(25000, 500000)
    
    banks = [
        ["NuBank", nubank],
        ["Itau", itau],
        ["Bradesco", bradesco],
        ["Santander", santander]
    ]
    
    print("")
    print("________________________")
    print("")
    print("Bem-vindo a Concessionária Python!")
    print("Antes de tudo, é necessário que você se cadastre em nosso sistema.")
    
    print(" ")
    print("________________________")
    print(" ")
    print("Cadastro: ")
    clientName = input("Qual o seu nome? ")
    
    while True:
        try:
            clientAge = int(input("Qual a sua idade? "))
            if clientAge >= 18:
                break
            else:
                print("Você não pode adquirir um veículo, pois é menor de idade.")
                sys.exit()
        except ValueError:
            print("Entrada inválida. A idade deve ser um valor inteiro.")
    
    while True:
        clientBank = input("Qual o seu banco? (NuBank), (Itau), (Bradesco), (Santander) \n")
        
        for banco in banks:
            if clientBank.lower() == banco[0].lower(): 
                clientMoney = banco[1]
                print(" ")
                print(f"Banco: {banco[0]}")
                print(f"Saldo: R$ {clientMoney}")
                print(" ")
                print("________________________")
                print(" ")
                break
        else:
            print("Opção inválida. Selecione um dentre os bancos existentes.")
            continue
        break
    
    cliente = Cliente(clientName, clientAge, clientBank, clientMoney)
    
    start_decision = input("Gostaria de comprar um veículo? Digite 'Sim' ou 'Nao' \n")
    
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
            while True:
                brand_chosen = input("Qual marca você está interessado? Temos (Porsche), (Toyota), (Ferrari), (Nissan), (Audi) e (Hyundai). \n")
            
                if brand_chosen.lower() == "porsche":
                    for carro in Porsche:
                        print(carro.mostrar_tabela())

                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for carro in Porsche:
                            if model_chosen.lower() == carro._modelo.lower():
                                print(carro.exibir_informacoes())
                                # prosseguir para a compra...
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break    
                
                elif brand_chosen.lower() == "toyota":
                    for carro in Toyota:
                        print(carro.mostrar_tabela())
                    
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for carro in Toyota:
                            if model_chosen.lower() == carro._modelo.lower():
                                print(carro.exibir_informacoes())
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break    
                    
                elif brand_chosen.lower() == "ferrari":
                    for carro in Ferrari:
                        print(carro.mostrar_tabela())
                        
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for carro in Ferrari:
                            if model_chosen.lower() == carro._modelo.lower():
                                print(carro.exibir_informacoes())
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break    
                    
                elif brand_chosen.lower() == "nissan":
                    for carro in Nissan:
                        print(carro.mostrar_tabela())
                    
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for carro in Nissan:
                            if model_chosen.lower() == carro._modelo.lower():
                                print(carro.exibir_informacoes())
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break    
            
                elif brand_chosen.lower() == "audi":
                    for carro in Audi:
                        print(carro.mostrar_tabela())
                        
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for carro in Audi:
                            if model_chosen.lower() == carro._modelo.lower():
                                print(carro.exibir_informacoes())
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break                            
                    
                elif brand_chosen.lower() == "hyundai":
                    for carro in Hyundai:
                        print(carro.mostrar_tabela())
                        
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for carro in Hyundai:
                            if model_chosen.lower() == carro._modelo.lower():
                                print(carro.exibir_informacoes())
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break                       
            
                else:
                    print("Opção inválida. Tente novamente.")
                    continue
                break

        
        elif vehicle_type.lower() == "moto":
            vehicle_chosen = Moto
            brand_chosen = input("Qual marca você está interessado? Temos (BMW), (Yamaha) e (Kawasaki). \n")

            
        elif vehicle_type.lower() == "caminhao":
            vehicle_chosen = Caminhao
            brand_chosen = input("Qual marca você está interessado? Temos (Mercedes), (Volvo) e (Foton). \n")


        else: 
            print("Opção inválida. Tente novamente.")
            continue
        
        break