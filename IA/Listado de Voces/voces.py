import pyttsx3

voz = pyttsx3.init()
voces = voz.getProperty('voices')

for i, v in enumerate(voces):
    print(f"Índice: {i}")
    print(f" - ID: {v.id}")
    print(f" - Nombre: {v.name}")
    print(f" - Idioma(s): {v.languages}")
    print(f" - Género: {v.gender if hasattr(v, 'gender') else 'N/A'}")
    print("-" * 30)
