from gpt4all import GPT4All
import os

# Define nombre y ruta del modelo
nombre_modelo = "mistral-7b-openorca.Q4_0.gguf"
ruta_modelo = os.path.join(os.path.expanduser("~"), ".cache", "gpt4all")

# Asegúrate de que la ruta existe
os.makedirs(ruta_modelo, exist_ok=True)

# Descarga el modelo
GPT4All.download_model(model_filename=nombre_modelo, model_path=ruta_modelo)

# Carga el modelo para probarlo
modelo = GPT4All(model_name=nombre_modelo, model_path=ruta_modelo)
modelo.open()

respuesta = modelo.chat_completion(
    messages=[{"role": "user", "content": "Hola, ¿cómo estás?"}]
)

print("🧠 Respuesta de prueba:", respuesta['choices'][0]['message']['content'])
