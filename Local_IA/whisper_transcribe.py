# whisper_transcribe.py
from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="int8")

def transcribir_audio(nombre_archivo):
    print("📝 Transcribiendo con faster-whisper...")
    segments, info = model.transcribe(nombre_archivo)
    texto = ""
    for segment in segments:
        texto += segment.text + " "
    print("📜 Texto transcrito:", texto.strip())
    return texto.strip()
