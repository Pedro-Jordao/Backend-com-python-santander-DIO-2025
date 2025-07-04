class Bicicleta:
#cor, modelo, ano, valor
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Trim Trim")
    
    def parar(self):
        print("Bicicleta parada")

    def correr(self):
        print("Vruuuum")

    # def __str__(self):
    #     return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# b1 = Bicicleta("azul", "caloi", 2020, 500)
# b1.buzinar()
# b1.correr()
# b1.parar()

# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("vermelha", "monark", 2021, 600)
# Bicicleta.buzinar(b2) # b2.buzinar()

print(b2)