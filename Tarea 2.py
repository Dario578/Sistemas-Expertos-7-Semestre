# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 20:50:36 2025

@author: jdari
"""

# ======================================================
# 🔹 Inteligencia Artificial de Recetas de Cocina
# Algoritmo: Filtrado basado en contenido con Scoring
# ======================================================

# Base de datos de recetas (puedes ampliarla)
recetas = [
    {
        "nombre": "Pollo guisado",
        "ingredientes": ["pollo", "tomate", "cebolla", "ajo"],
        "instrucciones": "Dorar el pollo, añadir jitomate, cebolla y ajo, cocinar a fuego lento."
    },
    {
        "nombre": "Ensalada fresca",
        "ingredientes": ["lechuga", "tomate", "pepino", "cebolla"],
        "instrucciones": "Cortar las verduras y mezclar con aderezo."
    },
    {
        "nombre": "Sopa de verduras",
        "ingredientes": ["zanahoria", "calabacita", "tomate", "cebolla", "ajo"],
        "instrucciones": "Hervir agua, añadir verduras picadas y sazonar."
    },
    {
        "nombre": "Tacos de pollo",
        "ingredientes": ["pollo", "tortilla", "cebolla", "cilantro"],
        "instrucciones": "Desmenuzar el pollo, servir en tortilla y añadir cebolla con cilantro."
    },
    {
        "nombre": "Pasta con salsa de tomate",
        "ingredientes": ["pasta", "tomate", "ajo", "queso"],
        "instrucciones": "Cocer la pasta y añadir salsa hecha con jitomate, ajo y queso."
    }
]

# ------------------------------------------------------
# Función de búsqueda de recetas con "IA básica"
# ------------------------------------------------------
def buscar_recetas(ingredientes_usuario, base_recetas):
    resultados = []
    for receta in base_recetas:
        # Coincidencias entre lo que tiene el usuario y la receta
        match = len(set(ingredientes_usuario) & set(receta["ingredientes"]))
        if match > 0:  # Solo mostrar recetas con al menos 1 coincidencia
            score = match / len(receta["ingredientes"])
            resultados.append((receta["nombre"], score, receta["instrucciones"]))
    
    # Ordenar de mayor a menor porcentaje de coincidencia
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados

# ------------------------------------------------------
# Programa principal
# ------------------------------------------------------
if __name__ == "__main__":
    print("=== 🍳 Bienvenido al recomendador de recetas ===")
    print("Escribe los ingredientes que tienes (separados por coma).")
    entrada = input("👉 Ingredientes: ").lower()
    
    # Convertir la entrada a lista limpia
    ingredientes_usuario = [ing.strip() for ing in entrada.split(",")]
    
    # Buscar recetas
    recetas_encontradas = buscar_recetas(ingredientes_usuario, recetas)
    
    # Mostrar resultados
    if recetas_encontradas:
        print("\n✅ Recetas encontradas:\n")
        for nombre, score, instrucciones in recetas_encontradas:
            print(f"🍽️ {nombre}  ({round(score*100, 1)}% coincidencia)")
            print(f"   ➡️ {instrucciones}\n")
    else:
        print("\n❌ No encontré recetas con esos ingredientes, intenta con otros.")
