import pyttsx3

def audio_PC(text):
    engine = pyttsx3.init()

    # para ver las voces accesibles
    for voz in engine.getProperty('voices'):
        print(voz)


    # ajustar la velocidad
    engine.setProperty('rate', 200)
    # ajustar el volumen
    engine.setProperty('volume', 1)

    engine.say(text)
    engine.runAndWait()

# text = "Hola, ¿cómo estás?"
# audio_PC(text)

