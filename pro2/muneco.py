
# Cada dibujo representa una etapa del ahorcado.
# Se agrega una sola parte del muñeco en cada etapa.

dibujos = [
    # 0 errores: estructura vacía
    """
      ______
      |    |
      |
      |
      |
    __|__
    """,

    # 1 error: cabeza
    """
      ______
      |    |
      |    O
      |
      |
    __|__
    """,

    # 2 errores: cuerpo
    """
      ______
      |    |
      |    O
      |    |
      |
    __|__
    """,

    # 3 errores: brazo izquierdo
    """
      ______
      |    |
      |    O
      |   /|
      |
    __|__
    """,

    # 4 errores: brazo derecho
    """
      ______
      |    |
      |    O
      |   /|\\
      |
    __|__
    """,

    # 5 errores: pierna izquierda
    """
      ______
      |    |
      |    O
      |   /|\\
      |   /
    __|__
    """,

    # 6 errores: pierna derecha
    """
      ______
      |    |
      |    O
      |   /|\\
      |   / \\
    __|__
    """,

    # 7 errores: etapa final
    """
      ______
      |    |
      |    O
      |   /|\\
      |   / \\
    __|__
       FIN
    """
]


def mostrar_ahorcado(errores):
    # Validamos que errores sea un entero, no un booleano
    if not isinstance(errores, int) or isinstance(errores, bool):
        return "Error: los errores deben ser un número entero."

    # Evitamos índices negativos
    errores = max(0, errores)

    # Evitamos superar la cantidad de dibujos
    errores = min(errores, len(dibujos) - 1)

    # Devolvemos la etapa correspondiente
    return dibujos[errores]

# Prueba temporal: mostrar todas las etapas del muñeco
if __name__ == "__main__":
    for errores in range(len(dibujos)):
        print(f"\nETAPA: {errores} errores")
        print(mostrar_ahorcado(errores))