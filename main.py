from audio_a_text import audio_a_text
from text_a_audio import audio_PC
from dia_actual import pedir_dia_actual
import pyjokes
import datetime

nombre_assistente = "Hal"

def centro_peticiones():

    while True:

        peticion = audio_a_text().lower()
        print("La petición es", peticion)

        if "qué día es hoy" in peticion:
            print(pedir_dia_actual())
            audio_PC(pedir_dia_actual())
            continue

        elif "qué hora es" in peticion:
            hora = datetime.datetime.now()
            hora = f"En este momento son las {hora.hour} con {hora.minute} y {hora.second} segundos"
            audio_PC(hora)
            continue

        elif "cuéntame un chiste" in peticion:
            audio_PC(pyjokes.get_joke("es"))
            continue

        elif (f"{nombre_assistente.lower()} fin del programa") in peticion:
            audio_PC("Programa finalizado")
            break

centro_peticiones()