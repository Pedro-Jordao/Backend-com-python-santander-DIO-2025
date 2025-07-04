from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'loremipsum.txt', 'r') as arquivo:
    print('Trabalhando com o arquivo loremipsum.txt')
    
print(arquivo.read())