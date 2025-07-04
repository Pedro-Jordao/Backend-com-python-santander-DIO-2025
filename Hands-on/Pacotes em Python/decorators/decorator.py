# Um decorador é uma função que recebe outra função como argumento e retorna uma nova função (modificada ou estendida).
# Decoradores são usados para adicionar funcionalidades a funções existentes de forma elegante e reutilizável.
def meu_decorador(funcao):
    def envelope():
        print("Antes da execução da função")
        funcao()
        print("Depois da execução da função")
    
    return envelope

# Exemplo de uso do açúcar sintático para aplicar o decorador
@meu_decorador
def ola_mundo():
    print("Olá, mundo!")

ola_mundo()


