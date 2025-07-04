from datetime import timedelta, datetime, date
tipo_carro= 'G'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
if tipo_carro == 'P':
    estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou às {data_atual} e ficará pronto às {estimada}')
elif tipo_carro == 'M':
    estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou às {data_atual} e ficará pronto às {estimada}')
elif tipo_carro == 'G':
    estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou às {data_atual} e ficará pronto às {estimada}')

print (date.today() - timedelta(days=1)) 

resultado = datetime(2023, 7, 10, 10, 30, 50) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())
