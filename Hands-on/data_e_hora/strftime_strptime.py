"""
O Python também permite converter e formatar datas e horas.
Para isso, utilizamos os métodos 'strftime' (string format time) e
'strptime' (string parse time).



"""

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-15 14:30"
mascara_ptbr = '%d/%m/%Y'
mascara_en = '%Y-%m-%d %H:%M'
print(data_hora_atual.strftime(mascara_ptbr)) #formata tirando do formato US para o BR
#exibe a data e hora atual no formato brasileiro

################## STRPTIME ##################
# Converte uma string para um objeto datetime
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)


print(f"data_convertida = {type(data_convertida).__name__}")