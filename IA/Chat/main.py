import speech_recognition as sr
import pyttsx3
from gpt4all import GPT4All
import os
import threading
import tkinter as tk
from tkinter import scrolledtext

# Configuración del modelo
nombre_modelo = "mistral-7b-openorca.Q4_0.gguf"
ruta_modelo = os.path.join(os.path.expanduser("~"), ".cache", "gpt4all")

# Configuración de voz
voz = pyttsx3.init()
voces = voz.getProperty('voices')
# Selección de voz masculina en español (si está disponible)
for v in voces:
    if "spanish" in v.name.lower() and ("male" in v.name.lower() or "hombre" in v.name.lower()):
        voz.setProperty('voice', v.id)
        break
else:
    voz.setProperty('voice', voces[2].id)  # Español latino (Sabina)
voz.setProperty('rate', 160)

# Historial de la conversación
historial = []

# Inicializar modelo
modelo = GPT4All(model_name=nombre_modelo, model_path=ruta_modelo)

# Funciones de la interfaz
def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        escribir("🎤 Escuchando...")
        try:
            audio = r.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            escribir("⏱️ Tiempo de espera agotado.")
            return
    try:
        texto = r.recognize_google(audio, language="es-ES")
        escribir(f"👤 Tú: {texto}")
        procesar_pregunta(texto)
    except sr.UnknownValueError:
        escribir("🤷‍♂️ No entendí.")
    except sr.RequestError:
        escribir("❌ Error con el servicio de reconocimiento.")

def procesar_pregunta(entrada):
    historial.append(f"Usuario: {entrada}")
    contexto = "\n".join(historial) + "\nIA:"
    respuesta = modelo.generate(contexto, max_tokens=200).strip()
    historial.append(f"IA: {respuesta}")
    escribir(f"🤖 IA: {respuesta}")
    # Habla solo la respuesta
    threading.Thread(target=hablar, args=(respuesta,)).start()

def hablar(texto):
    voz.say(texto)
    voz.runAndWait()

def escribir(texto):
    chat.config(state='normal')
    chat.insert(tk.END, texto + "\n")
    chat.config(state='disabled')
    chat.see(tk.END)

def enviar_texto():
    entrada = entrada_usuario.get()
    entrada_usuario.delete(0, tk.END)
    if entrada:
        escribir(f"👤 Tú: {entrada}")
        procesar_pregunta(entrada)

def grabar_audio():
    threading.Thread(target=escuchar).start()

# Crear interfaz
ventana = tk.Tk()
ventana.title("IA Local con Voz")

chat = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, state='disabled', width=60, height=20)
chat.pack(padx=10, pady=10)

entrada_usuario = tk.Entry(ventana, width=50)
entrada_usuario.pack(padx=10, pady=5)
entrada_usuario.bind("<Return>", lambda event: enviar_texto())

frame_botones = tk.Frame(ventana)
frame_botones.pack()

boton_enviar = tk.Button(frame_botones, text="Enviar", command=enviar_texto)
boton_enviar.pack(side=tk.LEFT, padx=5)

boton_grabar = tk.Button(frame_botones, text="🎤 Hablar", command=grabar_audio)
boton_grabar.pack(side=tk.LEFT, padx=5)

escribir("🧠 IA lista. Puedes escribir o hablar.")
ventana.mainloop()
