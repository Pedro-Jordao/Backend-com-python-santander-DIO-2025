caminho = r'C:\Área de Trabalho\programing\DIO BOOTCAMPS\Backend com Python - Santander Bootcamp 2025\Hands-on\manipulação de arquivos\loremipsum.txt'
file = open(caminho, 'r', encoding='utf-8')
# print(file.read())
# print (file.readline())  # Lê a primeira linha do arquivo
# for line in file.readline():
#     print(line.strip())

# for line in file.readlines():
#     print(line)                

# while len(linha := file.readline()):
#     print(linha)

file.close()