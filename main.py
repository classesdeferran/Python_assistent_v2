from audio_a_text import audio_a_text
from text_a_audio import audio_PC
from dia_actual import pedir_dia_actual
import pyjokes
import datetime
from meteo import meteo_ciudad
import webbrowser
import pywhatkit
import wikipedia

nombre_assistente = "Hal"

def quitar_acentos(text):
    dicc_vocales = {"á" : "a", "é" : "e", "í" : "i","ó" : "o","ú" : "u",}
    for acento in dicc_vocales:
        if acento in text:
            text = text.replace(acento, dicc_vocales[acento] )
    return text

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

        elif "qué tiempo hace en" in peticion:
            ciudad = peticion.replace("qué tiempo hace en ", "")
            ciudad = quitar_acentos(ciudad.lower())
            # print(ciudad)
            audio_PC(meteo_ciudad(ciudad))
            continue

        elif "abre youtube" in peticion:
            audio_PC("Ahora mismo abro Youtube")
            webbrowser.open("https://www.youtube.com/")
            continue

        elif "reproduce" in peticion:
            audio_PC("¡A mi también me gusta!")
            titulo = peticion.replace("reproduce ", "")
            pywhatkit.playonyt(titulo)
            continue

        elif "busca en wikipedia" in peticion:
            busqueda = peticion.replace("busca en wikipedia ", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(busqueda, sentences=1)
            resultado = "Según wikipedia:\n" + resultado
            audio_PC(resultado)
            continue

        elif "cuéntame un chiste" in peticion:
            audio_PC(pyjokes.get_joke("es"))
            continue

        elif (f"fin del programa") in peticion:
            audio_PC("Programa finalizado")
            break

centro_peticiones()