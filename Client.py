from Vehicles import Vehicles
from Manager import Manager

class Cliente():
    
    def __init__(self, nome, idade, banco, dinheiro):
        self.nome = nome
        self.idade = idade
        self.banco = banco
        self.dinheiro = dinheiro
        
        
    def adquirir_veiculo(self, veiculo, manager):
        custo_veiculo = veiculo.custo_veiculo()
        if self.dinheiro >= custo_veiculo:
            self.dinheiro -= custo_veiculo
            print(f"Parabéns, {self.nome}! Você adquiriu o {veiculo._marca} {veiculo._modelo} por R${custo_veiculo}!")
            print(veiculo.exibir_informacoes())
            print(f"Saldo restante: R$ {self.dinheiro}. \n")
            manager.adicionar_veiculo(veiculo)
            print(" \n")
            print("Veículos adquiridos:")
            manager.listar_veiculos(self)
        else:
            print("Dinheiro insuficiente.")     