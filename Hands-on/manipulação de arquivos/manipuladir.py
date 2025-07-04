import os
import shutil
from pathlib import Path # Importando o módulo pathlib para manipulação de caminhos de arquivos

ROOT_PATH = Path(__file__).parent
# os.mkdir(ROOT_PATH / 'nova-pasta')  # Cria um novo diretório chamado 'nova-pasta' no caminho atual

# os.mkdir('nova-pasta') #isso criaria o novo diretório sem especificar o caminho
# arquivo = open (ROOT_PATH / 'novo-arquivo.txt', 'w')
# arquivo.close()  # Fecha o arquivo após a criação


# os.rename(ROOT_PATH / 'novo-arquivo.txt', ROOT_PATH / 'arquivo-renomeado.txt')  # Renomeia o arquivo criado
try:
    os.remove(ROOT_PATH / 'nova-pasta')  # Remove a nova pasta
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError: 
    print("Permissão negada para remover o arquivo ou diretório.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# shutil.move(ROOT_PATH / 'novo-arquivo.txt', ROOT_PATH / 'nova-pasta/novo-arquivo.txt')  # Move o arquivo criado para um novo local

