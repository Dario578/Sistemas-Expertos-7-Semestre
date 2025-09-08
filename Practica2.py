# ======================================================
# 🤖 Chat IA Aprendiz en Python
# Algoritmo: Sistema experto con adquisición de conocimiento
# ======================================================

import json   # Para manejar la base de conocimiento en formato JSON
import os     # Para verificar si ya existe un archivo de conocimiento

# ------------------------------------------------------
# Nombre del archivo donde se guardará el conocimiento
# ------------------------------------------------------
FILE = "knowledge.json"

# ------------------------------------------------------
# Si el archivo NO existe, se crea uno con respuestas básicas
# ------------------------------------------------------
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({
            "hola": "Hola, ¿cómo estás?",
            "como estas": "Muy bien, ¿y tú?",
            "de que te gustaria hablar": "Podemos hablar de cocina, tecnología o lo que quieras."
        }, f, indent=4)

# ------------------------------------------------------
# Cargar el conocimiento desde el archivo
# ------------------------------------------------------
with open(FILE, "r") as f:
    knowledge = json.load(f)

# ------------------------------------------------------
# Bienvenida del chat
# ------------------------------------------------------
print("=== 🤖 Chat IA Aprendiz ===")
print("Escribe 'salir' para terminar.\n")

# ------------------------------------------------------
# Bucle principal del chat
# ------------------------------------------------------
while True:
    # Entrada del usuario
    user_input = input("Tú: ").lower()  # Todo en minúsculas para facilitar búsqueda
    
    # Condición de salida
    if user_input == "salir":
        print("Bot: ¡Hasta luego! 👋")
        break

    # Si el input existe en la base de conocimiento → Responde
    if user_input in knowledge:
        print("Bot:", knowledge[user_input])
    else:
        # Si no existe la respuesta → Pedir al usuario que enseñe una nueva
        print("Bot: No conozco esa respuesta 🤔")
        new_response = input("¿Qué debería responder a eso? ")

        # Guardar el nuevo conocimiento
        knowledge[user_input] = new_response
        with open(FILE, "w") as f:
            json.dump(knowledge, f, indent=4)

        print("Bot: ¡Gracias! Aprendí algo nuevo. ✅")
