#Funções em python podem retornar outras funções
def calcular(operacao):
    def soma(x, y): #função interna
        return x + y
    
    def subtracao(x, y): #função interna
        return x - y
    
    if operacao == "+":
        return soma # Aqui, a função soma é retornada sem ser chamada, para que seja possível usá-la depois
    elif operacao == "-":
        return subtracao # Aqui, a função subtração é retornada sem ser chamada, para que seja possível usá-la depois
    else:
        raise ValueError("Operação inválida. Use '+' ou '-'.")

def intervalo ():

    print( "@" * 50, "\n")
# Execução do código

intervalo()
resultado = calcular("+")(5, 3)
print(f"Resultado da soma: {resultado}")

intervalo()
resultado = calcular("-")(5, 3)
print(f"Resultado da subtração: {resultado}")

intervalo()
resultado = calcular("+")
# Esse exemplo mostra que é possível armazenar a função retornada e usá-la depois,
# sem dar os parâmetros da função interna, somente o fazendo quando necessário.
print(f"Função de soma: {resultado(5, 3)}")