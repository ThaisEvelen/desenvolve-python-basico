from datetime import datetime

agora = datetime.now()

data_formatada = agora.strftime("%d/%m/%Y")
hora_formatada = agora.strftime("%H:%M")

print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
