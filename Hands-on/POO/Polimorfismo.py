class Passaro:
    def voar(self):
        print ("O pássaro está voando")
class Pardal (Passaro):
    def voar(self):
        return super().voar()

class Avestruz (Passaro):
    def voar(self):
        print ("O avestruz não voa")

#FIXME exemplo ruim do uso da herança e do polimorfismo, pois o avião não é um pássaro
# mas sim um veículo que voa, o correto seria usar uma interface ou classe abstrata
# para representar o comportamento de voar, e não herdar de Passaro.
class Aviao(Passaro):
    def voar(self):
        print("O avião está decolando")

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(Pardal())  # Saída: O pássaro está voando
plano_de_voo(Avestruz())  # Saída: O avestruz não vo
plano_de_voo(Aviao())  # Saída: O avião está decolando