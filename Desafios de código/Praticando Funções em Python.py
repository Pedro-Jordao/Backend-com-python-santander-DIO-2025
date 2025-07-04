# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# Função de chave para ordenar
def prioridade(paciente):
    nome, idade, status = paciente
    # Prioridade: 0 = urgente, 1 = idosos, 2 = demais
    if status == "urgente":
        prioridade = 0
    elif idade >= 60:
        prioridade = 1
    else:
        prioridade = 2
    # Retornamos uma tupla (prioridade, -idade) para garantir que mais velhos venham primeiro em caso de empate
    return (prioridade, -idade)

# Ordenar a lista de pacientes
pacientes.sort(key=prioridade)

# Exibir a ordem de atendimento
print("Ordem de Atendimento:", ", ".join(paciente[0] for paciente in pacientes))



