from pathlib import Path
try:
    arquivo = open('novo01-arquivo.py')
except FileNotFoundError as exc:
    print("Arquivo não encontrado.")
    print(exc)


ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / 'nova-pasta')
except IsADirectoryError as exc:
    print("Tentativa de abrir um diretório como arquivo.")
    print(exc)