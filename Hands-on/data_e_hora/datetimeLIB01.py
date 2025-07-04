import datetime
from datetime import datetime as dt, time
print (datetime.datetime.now())  # Exibe a data e hora atual
print (datetime.date.today())     # Exibe a data atual
print (datetime.time(12, 30))      # Exibe um horário específico (12:30)
print(datetime.date.today()) # Exibe a data atual


data_hora = datetime.datetime(2023, 7, 10, 10, 30, 50)
print(data_hora)  # Exibe a data e hora especificada

print (dt.today())

hora = time(12, 30)
print(hora)  # Exibe o horário especificado (12:30)

#exibe o horario atual
hora_atual = dt.now().time()
print(hora_atual) 




### timedelta ###
#criando data e hora
