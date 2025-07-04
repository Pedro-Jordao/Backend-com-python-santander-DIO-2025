"""
módulo pytz: permite trabalhar com fusos horários de forma fácil e intuitiva.
Instalação: pip install pytz

Exemplo de uso:
- Importar o módulo pytz.
- Criar um objeto timezone com o fuso horário desejado.
- Converter uma data/hora para o fuso horário especificado.
- Exibir a data/hora convertida.
"""
from datetime import datetime, timezone, timedelta

import pytz
data = datetime.now(pytz.timezone('Europe/London'))

print (data)

'''
também é possível fazer isso com o próprio datetime, porém o pytz é mais enxuto e completo
bem como, é menos verboso

'''
# timezone com o datetime

data1= datetime.now(timezone(timedelta(hours=2)))
data2 = datetime.now(timezone(timedelta(hours=-3)))

print (data1)
print (data2)