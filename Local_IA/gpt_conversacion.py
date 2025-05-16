# gpt_conversacion.py
import openai
from config import openai_api_key

openai.api_key = openai_api_key

def obtener_respuesta(texto_usuario):
    print("🤖 Enviando texto a GPT...")
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente conversacional amistoso."},
            {"role": "user", "content": texto_usuario}
        ]
    )
    texto_ia = respuesta["choices"][0]["message"]["content"]
    print("🧠 Respuesta de GPT:", texto_ia)
    return texto_ia
