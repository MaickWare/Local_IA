from flask import Flask, request, jsonify, render_template
from gpt4all import GPT4All
import os
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

# Modelo
modelo = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf",
                 model_path=os.path.join(os.path.expanduser("~"), ".cache", "gpt4all"))
historial = []

# Voz
voz = pyttsx3.init()
voz.setProperty("rate", 160)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json()
    pregunta = data.get("mensaje")
    if not pregunta:
        return jsonify({"respuesta": "No recibí mensaje."}), 400

    historial.append(f"Usuario: {pregunta}")
    contexto = "\n".join(historial) + "\nIA:"
    respuesta = modelo.generate(contexto, max_tokens=200).strip()
    historial.append(f"IA: {respuesta}")

    return jsonify({"respuesta": respuesta})

@app.route("/voz", methods=["POST"])
def voz_endpoint():
    respuesta = request.json.get("texto")
    if not respuesta:
        return jsonify({"error": "Falta el texto"}), 400
    voz.say(respuesta)
    voz.runAndWait()
    return jsonify({"mensaje": "Reproducción completa"})

if __name__ == "__main__":
    app.run(debug=True)
