"""
    Recibe una lista de enteros y devuelve otra lista:
    1. Sin números negativos.
    2. Sin valores duplicados.
    3. Ordenada de menor a mayor.
    """
    
def procesar_lista_enteros(lista):

    # 1. Eliminar negativos
    lista = [n for n in lista if n >= 0]

    # 2. Eliminar duplicados
    lista = list(set(lista))

    # 3. Ordenar
    lista.sort()

    return lista


# --- Prueba de ejemplo ---
if __name__ == "__main__":
    datos = [4, -1, 2, 4, 3, -5, 2]
    resultado = procesar_lista_enteros(datos)
    print("Lista original:", datos)
    print("Resultado final:", resultado)
