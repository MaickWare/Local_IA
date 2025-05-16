# audio_input.py
import sounddevice as sd
from scipy.io.wavfile import write

def grabar_audio(nombre_archivo="entrada.wav", duracion=5, fs=44100):
    print("🎤 Grabando audio...")
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(nombre_archivo, fs, audio)
    print("✅ Audio guardado:", nombre_archivo)
    return nombre_archivo
