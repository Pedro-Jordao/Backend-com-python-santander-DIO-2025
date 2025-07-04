class Veiculo:
    def __init__(self, cor, placa, ano):
        self.cor = cor
        self.placa = placa
        self.ano = ano
    def ligar(self):
        print(f"Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    def __init__(self, cor, placa, ano, carregado):
        super().__init__(cor, placa, ano)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Este caminhão está carregado' if self.carregado else 'Este caminhão não está carregado'}")


moto = Motocicleta("vermelha", "ABC1234", 2021)
# print(moto.cor)

carro = Carro("azul", "XYZ5678", 2020)


caminhao = Caminhao("verde", "LMN9012", 2019, True)

print("", moto, carro, caminhao, sep="\n \n")