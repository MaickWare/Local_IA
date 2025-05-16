from audio_input import grabar_audio
from whisper_transcribe import transcribir_audio
from gpt_conversacion import obtener_respuesta
from tts_output import hablar

if __name__ == "__main__":
    while True:
        input("🎙️ Presiona ENTER para grabar tu pregunta...")
        archivo = grabar_audio()
        texto = transcribir_audio(archivo)
        respuesta = obtener_respuesta(texto)
        hablar(respuesta)
        print("\n👂 Esperando la siguiente pregunta...")
