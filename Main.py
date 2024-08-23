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
    nubank = random.randint(25000, 100000000)
    itau = random.randint(25000, 3000000)
    bradesco = random.randint(25000, 9000000)
    santander = random.randint(25000, 5000000)
    
    banks = [
        ["NuBank", nubank],
        ["Itau", itau],
        ["Bradesco", bradesco],
        ["Santander", santander]
    ]
    
    print("")
    print("________________________")
    print("")
    print("Bem-vindo à Concessionária Python!")
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
    
    if start_decision.lower() == "sim":
        print("Perfeito! Vou pedir algumas informações sobre o veículo para que tudo seja registrado corretamente.")
    else:
        print("Tudo-bem! Muito obrigado por utilizar a Garagem Python!")
        sys.exit()

    while True:   
        vehicle_type = input("Qual o tipo de veículo? Carro, Moto ou Caminhao? \n")
        
        # Cars
        if vehicle_type.lower() == "carro":
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
                                cliente.adquirir_veiculo(carro)
                                gerenciador.adicionar_veiculo(carro)
                                gerenciador.listar_veiculos()
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
                                cliente.adquirir_veiculo(carro)
                                gerenciador.adicionar_veiculo(carro)
                                gerenciador.listar_veiculos()
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
                                cliente.adquirir_veiculo(carro)
                                gerenciador.adicionar_veiculo(carro)
                                gerenciador.listar_veiculos()
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
                                cliente.adquirir_veiculo(carro)
                                gerenciador.adicionar_veiculo(carro)
                                gerenciador.listar_veiculos()
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
                                cliente.adquirir_veiculo(carro)
                                gerenciador.adicionar_veiculo(carro)
                                gerenciador.listar_veiculos()
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
                                cliente.adquirir_veiculo(carro)
                                gerenciador.adicionar_veiculo(carro)
                                gerenciador.listar_veiculos()
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break                       
            
                else:
                    print("Opção inválida. Tente novamente.")
                    continue
                break

        # Motorcycles
        elif vehicle_type.lower() == "moto":
            while True:
                brand_chosen = input("Qual marca você está interessado? Temos (BMW), (Yamaha) e (Kawasaki). \n")
            
                if brand_chosen.lower() == "bmw":
                    for moto in BMW:
                        print(moto.mostrar_tabela())
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for moto in BMW:
                            if model_chosen.lower() == moto._modelo.lower():
                                print(moto.exibir_informacoes())
                                cliente.adquirir_veiculo(moto)
                                gerenciador.adicionar_veiculo(moto)
                                gerenciador.listar_veiculos()
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break    
                
                elif brand_chosen.lower() == "yamaha":
                    for moto in Yamaha:
                        print(moto.mostrar_tabela())
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for moto in Yamaha:
                            if model_chosen.lower() == moto._modelo.lower():
                                print(moto.exibir_informacoes())
                                cliente.adquirir_veiculo(moto)
                                gerenciador.adicionar_veiculo(moto)
                                gerenciador.listar_veiculos()
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break

                elif brand_chosen.lower() == "kawasaki":
                    for moto in Kawasaki:
                        print(moto.mostrar_tabela())
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for moto in Kawasaki:
                            if model_chosen.lower() == moto._modelo.lower():
                                print(moto.exibir_informacoes())
                                cliente.adquirir_veiculo(moto)
                                gerenciador.adicionar_veiculo(moto)
                                gerenciador.listar_veiculos()
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break

                else:
                    print("Opção inválida. Tente novamente.")
                    continue
                break
                
        # Trucks
        elif vehicle_type.lower() == "caminhao":
            while True:
                brand_chosen = input("Qual marca você está interessado? Temos (Mercedes), (Volvo) e (Foton). \n")
            
                if brand_chosen.lower() == "mercedes":
                    for caminhao in Mercedes:
                        print(caminhao.mostrar_tabela())
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for caminhao in Mercedes:
                            if model_chosen.lower() == caminhao._modelo.lower():
                                print(caminhao.exibir_informacoes())
                                cliente.adquirir_veiculo(caminhao)
                                gerenciador.adicionar_veiculo(caminhao)
                                gerenciador.listar_veiculos()
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break    
                
                elif brand_chosen.lower() == "volvo":
                    for caminhao in Volvo:
                        print(caminhao.mostrar_tabela())
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for caminhao in Volvo:
                            if model_chosen.lower() == caminhao._modelo.lower():
                                print(caminhao.exibir_informacoes())
                                cliente.adquirir_veiculo(caminhao)
                                gerenciador.adicionar_veiculo(caminhao)
                                gerenciador.listar_veiculos()
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break
                    
                elif brand_chosen.lower() == "foton":
                    for caminhao in Foton:
                        print(caminhao.mostrar_tabela())
                    while True:
                        model_chosen = input(f"Qual modelo de {brand_chosen} você deseja adquirir? \n")
                        for caminhao in Foton:
                            if model_chosen.lower() == caminhao._modelo.lower():
                                print(caminhao.exibir_informacoes())
                                cliente.adquirir_veiculo(caminhao)
                                gerenciador.adicionar_veiculo(caminhao)
                                gerenciador.listar_veiculos()
                                break
                        else:
                            print("Modelo não encontrado, por favor tente novamente.")
                            continue
                        break

                else:
                    print("Opção inválida. Tente novamente.")
                    continue
                break

        else:
            print("Tipo de veículo inválido. Tente novamente.")
            continue
        
        continue_decision = input("Deseja comprar outro veículo? Digite 'Sim' para continuar ou 'Nao' para sair. \n")
        if continue_decision.lower() == "nao":
            print("Muito obrigado por utilizar a Garagem Python!")
            break
