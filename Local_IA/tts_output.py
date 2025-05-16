import pyttsx3

def hablar(texto):
    print("🔊 Reproduciendo respuesta...")
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Velocidad
    engine.setProperty('voice', 'spanish')  # Voz en español si está disponible
    engine.say(texto)
    engine.runAndWait()