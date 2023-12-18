from audio_a_text import audio_a_text
from text_a_audio import audio_PC
from dia_actual import pedir_dia_actual
import pyjokes

nombre_assistente = "Robin"

def centro_peticiones():

    while True:

        peticion = audio_a_text().lower()
        print("La petición es", peticion)

        if f"qué día es hoy" in peticion:
            print(pedir_dia_actual())
            audio_PC(pedir_dia_actual())
            continue

        elif "cuéntame un chiste" in peticion:
            audio_PC(pyjokes.get_joke("es"))
            continue

        elif (f"fin del programa") in peticion:
            audio_PC("Programa finalizado")
            break

centro_peticiones()