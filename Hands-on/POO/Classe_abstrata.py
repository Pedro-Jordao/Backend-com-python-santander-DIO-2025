from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleRemotoTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
    def desligar(self):
        print("Desligando a TV")

class ControleRemotoArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado")
    def desligar(self):
        print("Desligando o Ar Condicionado")


controle = ControleRemotoTV()

controle.ligar()
controle.desligar()

