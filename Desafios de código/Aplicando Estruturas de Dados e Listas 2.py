# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:

for participante in range(n):
    linha = input().strip().replace(",", "")
    
    # Encontra a última ocorrência de espaço para separar nome e tema
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do participante e o tema
    nome = linha[:posicao_espaco]
    tema = linha[posicao_espaco + 1:]
    
    # Adiciona o participante ao dicionário de eventos
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(nome)


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")