from datetime import datetime
class Veiculo:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def verificar_antiguidade(self):
    # Obtendo o ano atual
    ano_atual = datetime.now().year
    # Verificando se o veículo é antigo
    if ano_atual - self.ano > 20:
        return "Veículo antigo"
    else:
        return "Veículo novo"

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())