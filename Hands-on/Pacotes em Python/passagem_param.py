def mensagem(nome):
    print('executando mensagem')
    return f'Olá, {nome}!'

def mensagem_completa(nome):
    print ('executando mensagem completa')
    return f'Olá, {nome}! Como você está?'

def executar (funcao):
    print('executando função')
    return funcao('Guilherme')


executar(mensagem) #exibe: executando função & executando mensagem

