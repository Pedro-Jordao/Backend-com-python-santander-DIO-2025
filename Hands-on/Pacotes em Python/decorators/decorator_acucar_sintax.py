def gritar(funcao):
    def envelope():
        resultado = funcao()  # Chama a função original para obter o resultado
        return resultado.upper()
    
    return envelope

@gritar
def saudacao():
    return "Bom dia!"

print(saudacao())  # Saída: BOM DIA!