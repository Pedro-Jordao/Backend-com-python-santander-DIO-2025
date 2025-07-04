caminho = r'C:\Área de Trabalho\programing\DIO BOOTCAMPS\Backend com Python - Santander Bootcamp 2025\Hands-on\manipulação de arquivos\teste.txt'
file = open(caminho, 'w', encoding='utf-8')
file.write("Teste de escrita em arquivo\n")
file.writelines(['Python\n', 'Java\n', 'JavaScript\n']) #escreve uma string por vez, tendo a necessidade de utilizar o \n para pular linha
file.close()