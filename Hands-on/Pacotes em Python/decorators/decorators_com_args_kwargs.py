def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Antes da execução da função")
        funcao(*args, **kwargs)
        print("Depois da execução da função")
    return envelope

@meu_decorador
def ola_mundo(nome, idade):
    print(f"Olá, {nome}!")


ola_mundo("Guilherme", 101001)