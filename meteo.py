import requests
from keys import METEO_KEY

def meteo_ciudad(ciudad):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={METEO_KEY}&lang=es&units=metric"

    respuesta = requests.get(url)
    data = respuesta.json()

    try:
        temp_actual = data['main']['temp']
        temp_sensacion = data['main']['feels_like']
        humedad = data['main']['humidity']
        temp_minima = data['main']['temp_min']
        temp_maxima = data['main']['temp_max']
        cielos = data['weather'][0]['description']

        mensaje = f'''
En {ciudad} hay una temperatura de {round(temp_actual,1)} grados, con sensación de {round(temp_sensacion,1)}.
{cielos} con una humedad del {humedad} %.
Se esperan temperaturas mínima y máxima de {round(temp_minima,1)} y {temp_maxima,1} respectivamente
'''
        return mensaje
    except:
        return "Nombre de ciudad no válido"
    
ciudad = "Madrid"


print(meteo_ciudad(ciudad))
# print(meteo_ciudad(ciudad))