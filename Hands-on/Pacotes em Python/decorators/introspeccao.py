#É a capacidade de um objeto saber sobre si mesmo, como seus atributos e métodos.
# Ou seja, saber sobre seus próprios atributos e métodos em tempo de execução.
import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)  # Preserva o nome e a docstring da função original para que não seja perdida a capacidade de introspecção
    def envelope(*args, **kwargs):
        print("Antes da execução da função")
        resultado = funcao(*args, **kwargs)
        print("Depois da execução da função")
        return resultado
    return envelope

@meu_decorador
def ola_mundo(nome, idade):
    print(f"Olá, {nome}!")
    return nome.upper()


resultado = ola_mundo("Guilherme", 101001)
print( resultado)