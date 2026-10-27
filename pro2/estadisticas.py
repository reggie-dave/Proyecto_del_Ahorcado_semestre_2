
import json
import os

# Archivo donde se guardan las estadísticas
ARCHIVO_ESTADISTICAS = "estadisticas.json"

# Datos iniciales
estadisticas = {
    "partidas_jugadas": 0,
    "victorias": 0,
    "derrotas": 0,
    "puntuacion_maxima": 0,
    "mejor_racha": 0
}

racha = 0


def cargar_estadisticas():
    # Cargamos los datos guardados si el archivo existe
    global estadisticas, racha

    if not os.path.exists(ARCHIVO_ESTADISTICAS):
        guardar_estadisticas()
        return

    try:
        with open(ARCHIVO_ESTADISTICAS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, dict):
            raise ValueError("El archivo no contiene un diccionario válido.")

        # Validamos cada dato cargado
        for clave in estadisticas:
            valor = datos.get(clave, 0)

            if type(valor) is int and valor >= 0:
                estadisticas[clave] = valor
            else:
                estadisticas[clave] = 0

    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        print("No se pudieron cargar las estadísticas.")
        print("Se utilizarán los valores iniciales.")

    # La racha actual empieza en cero al abrir el programa
    racha = 0


def guardar_estadisticas():
    # Guardamos los datos en el archivo JSON
    try:
        with open(ARCHIVO_ESTADISTICAS, "w", encoding="utf-8") as archivo:
            json.dump(
                estadisticas,
                archivo,
                indent=4,
                ensure_ascii=False
            )
    except (OSError, TypeError, ValueError) as error:
        print("Error al guardar las estadísticas:", error)


def registrar_resultado(victoria, puntos):
    # Validamos los datos recibidos
    global racha

    if type(victoria) is not bool:
        raise TypeError("La victoria debe ser True o False.")

    if type(puntos) is not int or puntos < 0:
        raise ValueError("Los puntos deben ser un entero no negativo.")

    # Registramos la partida
    estadisticas["partidas_jugadas"] += 1

    if victoria:
        estadisticas["victorias"] += 1
        racha += 1

        # Actualizamos la mejor racha
        estadisticas["mejor_racha"] = max(
            estadisticas["mejor_racha"],
            racha
        )
    else:
        estadisticas["derrotas"] += 1
        racha = 0

    # Actualizamos la puntuación máxima
    estadisticas["puntuacion_maxima"] = max(
        estadisticas["puntuacion_maxima"],
        puntos
    )

    guardar_estadisticas()


def reiniciar_estadisticas():
    # Reiniciamos todos los contadores
    global estadisticas, racha

    estadisticas = {
        "partidas_jugadas": 0,
        "victorias": 0,
        "derrotas": 0,
        "puntuacion_maxima": 0,
        "mejor_racha": 0
    }

    racha = 0
    guardar_estadisticas()

    print("Estadísticas reiniciadas correctamente.")


def mostrar_estadisticas():
    # Mostramos las estadísticas en la terminal
    print("\n=== ESTADÍSTICAS ===")

    for clave, valor in estadisticas.items():
        print(f"{clave}: {valor}")

    print(f"Racha actual: {racha}")


# CORRECCIONES:
# - Se agregó registrar_resultado(), necesaria para multijugador.py.
# - Se registran victorias, derrotas, puntos y rachas.
# - Se validan los datos cargados del archivo JSON.
# - Se conserva el formato de estadísticas utilizado por juego.py.
