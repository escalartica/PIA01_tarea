import string

def frecuencia_palabras(lista_palabras, ruta_fichero):
    """
    Recibe una lista de palabras y la ruta a un fichero de texto.
    Devuelve un diccionario con la frecuencia de aparición de
    esas palabras en el texto (en minúsculas y sin puntuación).
    """
    frecuencias = {}

    # Leer el contenido del archivo
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        texto = f.read().lower()  # convierte a minúsculas

    # Elimina signos de puntuación
    for signo in string.punctuation:
        texto = texto.replace(signo, "")

    # Convierte el texto en una lista de palabras
    palabras_texto = texto.split()

    # Calcula la frecuencia 
    for palabra in lista_palabras:
        frecuencias[palabra] = palabras_texto.count(palabra.lower())

    # Ordena el diccionario por palabra (clave)
    frecuencias_ordenadas = dict(sorted(frecuencias.items()))

    return frecuencias_ordenadas


# --- Programa de prueba ---
if __name__ == "__main__":
    # Creamos un archivo de texto 
    with open("texto_prueba.txt", "w", encoding="utf-8") as f:
        f.write("Hola mundo. Seguimos completando datos. Este es el segundo ejercicio del manejo de datos con Python. ")

    palabras = ["hola", "mundo", "datos", "python"]

    resultado = frecuencia_palabras(palabras, "texto_prueba.txt")

    print("\nFrecuencia de palabras:\n")
    for palabra, frecuencia in resultado.items():
        print(f"{palabra}: {frecuencia}")
