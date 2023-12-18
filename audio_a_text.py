# Cal instal·lar també pyaudio:
# pip install pyaudio

# Instal·lar aquesta versió de SpeechRecognition:
# pip install SpeechRecognition==3.10.0   
import speech_recognition as sr


def audio_a_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Micro ok")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="ca" )
            print("Has dit :", text)
            return text
        except sr.UnknownValueError:
            print("No t'he entès. Ho pots repetir, si us plau?")
            return "Error"
        except sr.RequestError:
            print("Ha falla la transcipció a text")
            return "Error"
        except Exception:
            print("Error greu")
            return "Error"
        
audio_a_text()
