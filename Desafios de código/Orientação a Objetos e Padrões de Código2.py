class Pedido:
    def __init__(self):
        self.itens = []  
    
    # Método para adicionar um item (preço) à lista
    def adicionar_item(self, preco):
        self.itens.append(preco)

    # Método para calcular o total da conta
    def calcular_total(self):
        return sum(self.itens)

# Lê a quantidade de pedidos
quantidade_pedidos = int(input().strip())

# Cria uma instância de Pedido
pedido = Pedido()ls

# Lê os itens e preços, adiciona ao pedido
for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)  # Separa o último elemento como preço
    pedido.adicionar_item(float(preco))  # Converte o preço para float e adiciona

# Exibe o total formatado com duas casas decimais
print(f"{pedido.calcular_total():.2f}")
