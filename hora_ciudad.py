import requests
from keys import METEO_KEY
import datetime

def timezone(ciudad):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={METEO_KEY}&lang=es&units=metric"

    respuesta = requests.get(url)
    data = respuesta.json()

    try:
        return data['timezone']
    except:
        return "Nombre de ciudad no válido"
    
def obtener_hora_ciudad(ciudad):
    hora_utc = datetime.datetime.utcnow()
    zona_horaria = timezone(ciudad)
    # print("timezone es ", zona_horaria)
    desplazamiento = datetime.timedelta(seconds=zona_horaria)
    hora_real = hora_utc + desplazamiento
    # print("hora_real ", hora_real)
    return f"Ahora en {ciudad} son las {hora_real.strftime('%H:%M')}"
    
ciudad = "los Angeles"
print(obtener_hora_ciudad(ciudad))
# print(meteo_ciudad(ciudad))