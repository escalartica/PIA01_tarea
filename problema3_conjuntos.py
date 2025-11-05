def operaciones_conjuntos(lista1, lista2):
    """
    Recibe dos listas de enteros y devuelve un diccionario con:
    - intersección: elementos comunes
    - unión: todos los elementos sin duplicados
    - diferencia simétrica: elementos que están en uno u otro conjunto, pero no en ambos
    """

    # Convierte las listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Calcula las operaciones
    interseccion = conjunto1 & conjunto2
    union = conjunto1 | conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2

    # Crea el diccionario con los resultados
    resultado = {
        "interseccion": sorted(list(interseccion)),
        "union": sorted(list(union)),
        "diferencia_simetrica": sorted(list(diferencia_simetrica))
    }

    return resultado


# --- Programa de prueba ---
if __name__ == "__main__":
    lista_a = [1, 2, 3, 4, 5]
    lista_b = [4, 5, 6, 7, 8]

    resultado = operaciones_conjuntos(lista_a, lista_b)

    print("Resultados de las operaciones con conjuntos:\n")
    for clave, valor in resultado.items():
        print(f"{clave.capitalize()}: {valor}")
