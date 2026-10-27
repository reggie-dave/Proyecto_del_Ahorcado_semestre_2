
# Importamos las funciones de los otros módulos
from pala import palabras
from muneco import mostrar_ahorcado, dibujos
from estadisticas import registrar_resultado


# Vidas disponibles según la dificultad
VIDAS_POR_DIFICULTAD = {
    "facil": 7,
    "medio": 5,
    "dificil": 3
}

# Categorías permitidas
CATEGORIAS_VALIDAS = ("animales", "tecnologia", "frutas")


def validar_nombre(nombre, numero):
    # Comprobamos que el nombre sea texto
    if not isinstance(nombre, str):
        print("El nombre debe ser texto.")
        return False

    nombre = nombre.strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return False

    if len(nombre) > 30:
        print("El nombre no puede superar los 30 caracteres.")
        return False

    # Solo permitimos letras y espacios
    if not all(letra.isalpha() or letra.isspace() for letra in nombre):
        print("El nombre solo puede contener letras y espacios.")
        return False

    # Contamos únicamente las letras
    cantidad_letras = sum(letra.isalpha() for letra in nombre)

    if cantidad_letras < 5:
        print(f"El nombre del jugador {numero} debe tener al menos 5 letras.")
        return False

    return True


def crear_jugador(nombre, dificultad, categoria):
    # Obtenemos una palabra para el jugador
    palabra = palabras(dificultad, categoria)

    if not isinstance(palabra, str) or not palabra.strip():
        raise ValueError("No se obtuvo una palabra válida.")

    palabra = palabra.strip().lower()

    # Comprobamos que la palabra contenga letras
    if not any(letra.isalpha() for letra in palabra):
        raise ValueError("La palabra seleccionada no es válida.")

    # Ocultamos las letras y conservamos otros caracteres
    oculta = [
        letra if not letra.isalpha() else "_"
        for letra in palabra
    ]

    return {
        "nombre": nombre.strip(),
        "palabra": palabra,
        "oculta": oculta,
        "vidas": VIDAS_POR_DIFICULTAD[dificultad],
        "puntos": 0,
        "letras_usadas": set(),
        "errores": 0,
        "terminado": False,
        "gano": False
    }


def calcular_etapa(jugador):
    # Calculamos cuántas vidas ha perdido
    vidas_iniciales = VIDAS_POR_DIFICULTAD[
        jugador["dificultad"]
    ]

    errores = jugador["errores"]
    etapas_totales = len(dibujos) - 1

    # Si perdió todas las vidas, mostramos la última etapa
    if jugador["vidas"] <= 0:
        return etapas_totales

    # Adaptamos el dibujo a la dificultad
    etapa = (errores * etapas_totales) // vidas_iniciales

    return min(max(etapa, 0), etapas_totales)


def mostrar_estado(jugador):
    print("\n" + "=" * 35)
    print("Turno de:", jugador["nombre"])
    print("Puntos:", jugador["puntos"])
    print("Vidas restantes:", jugador["vidas"])

    # Calculamos la etapa apropiada para sus vidas
    etapa = calcular_etapa(jugador)
    print(mostrar_ahorcado(etapa))

    print("Palabra:", " ".join(jugador["oculta"]))

    if jugador["letras_usadas"]:
        letras = ", ".join(sorted(jugador["letras_usadas"]))
        print("Letras usadas:", letras)
    else:
        print("Letras usadas: Ninguna")


def jugar_turno(jugador):
    # Mostramos el estado antes de pedir una letra
    mostrar_estado(jugador)

    letra = input(
        jugador["nombre"] + ", escriba una letra: "
    ).strip().lower()

    # Validamos la entrada
    if not letra:
        print("La entrada no puede estar vacía.")
        return False

    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida. Escriba una sola letra.")
        return False

    # Evitamos repetir letras
    if letra in jugador["letras_usadas"]:
        print("Ya utilizó esa letra. Intente con otra.")
        return False

    jugador["letras_usadas"].add(letra)

    # Comprobamos si la letra está en la palabra
    if letra in jugador["palabra"]:
        print("¡Correcto! Encontró una letra.")
        jugador["puntos"] += 10

        # Revelamos todas las apariciones
        for indice, caracter in enumerate(jugador["palabra"]):
            if caracter == letra:
                jugador["oculta"][indice] = letra

    else:
        print("Letra incorrecta.")
        jugador["vidas"] -= 1
        jugador["errores"] += 1

    # Comprobamos si completó la palabra
    if "_" not in jugador["oculta"]:
        jugador["terminado"] = True
        jugador["gano"] = True

        # Damos puntos adicionales por las vidas restantes
        jugador["puntos"] += jugador["vidas"] * 5

        print("\n¡Felicidades,", jugador["nombre"] + "!")
        print("Adivinó la palabra:", jugador["palabra"])
        print("Puntos finales:", jugador["puntos"])

    # Comprobamos si perdió todas las vidas
    elif jugador["vidas"] <= 0:
        jugador["vidas"] = 0
        jugador["terminado"] = True
        jugador["gano"] = False

        print("\nSe quedó sin vidas,", jugador["nombre"] + ".")
        print("La palabra era:", jugador["palabra"])

    return True


def iniciar_multijugador(dificultad, categoria, nombre1, nombre2):
    print("\n===== MODO MULTIJUGADOR =====")

    # Validamos la dificultad
    if not isinstance(dificultad, str):
        print("La dificultad debe ser texto.")
        return

    dificultad = dificultad.strip().lower()

    if dificultad not in VIDAS_POR_DIFICULTAD:
        print("Dificultad inválida.")
        return

    # Validamos la categoría
    if not isinstance(categoria, str):
        print("La categoría debe ser texto.")
        return

    categoria = categoria.strip().lower()

    if categoria not in CATEGORIAS_VALIDAS:
        print("Categoría inválida.")
        return

    # Validamos los nombres
    if not validar_nombre(nombre1, 1):
        return

    if not validar_nombre(nombre2, 2):
        return

    # Impedimos nombres iguales
    if nombre1.strip().casefold() == nombre2.strip().casefold():
        print("Los jugadores deben tener nombres diferentes.")
        return

    # Creamos los jugadores y sus palabras
    try:
        jugador1 = crear_jugador(nombre1, dificultad, categoria)
        jugador2 = crear_jugador(nombre2, dificultad, categoria)
    except (ValueError, TypeError, KeyError, IndexError) as error:
        print("No se pudo iniciar la partida:", error)
        return

    # Guardamos la dificultad en cada jugador para calcular el dibujo
    jugador1["dificultad"] = dificultad
    jugador2["dificultad"] = dificultad

    print("Cada jugador tendrá su propia palabra.")
    print("Cada letra correcta vale 10 puntos.")
    print("Las vidas restantes dan puntos adicionales al ganar.")
    print("Las entradas inválidas no hacen perder el turno.")

    jugadores = [jugador1, jugador2]
    turno = 0

    # Alternamos los turnos mientras haya jugadores activos
    try:
        while not all(jugador["terminado"] for jugador in jugadores):
            jugador = jugadores[turno]

            # Saltamos a los jugadores que ya terminaron
            if jugador["terminado"]:
                turno = (turno + 1) % 2
                continue

            # Solo cambiamos de turno si la entrada fue válida
            intento_valido = jugar_turno(jugador)

            if intento_valido:
                turno = (turno + 1) % 2

    except (EOFError, KeyboardInterrupt):
        print("\nPartida cancelada.")
        return

    # Mostramos los resultados finales
    print("\n" + "=" * 35)
    print("       RESULTADOS FINALES")
    print("=" * 35)

    for jugador in jugadores:
        print("\nJugador:", jugador["nombre"])
        print("Palabra:", jugador["palabra"])
        print("Puntos:", jugador["puntos"])
        print("Vidas restantes:", jugador["vidas"])

        if jugador["gano"]:
            print("Resultado: Victoria")
        else:
            print("Resultado: Derrota")

        # Registramos las estadísticas de cada jugador
        try:
            registrar_resultado(
                jugador["gano"],
                jugador["puntos"]
            )
        except (OSError, TypeError, ValueError, KeyError) as error:
            print(
                f"No se pudieron guardar las estadísticas de "
                f"{jugador['nombre']}: {error}"
            )

    # Declaramos ganador únicamente si ganó una partida
    if jugador1["gano"] and not jugador2["gano"]:
        print("\n¡Ganó", jugador1["nombre"] + "!")

    elif jugador2["gano"] and not jugador1["gano"]:
        print("\n¡Ganó", jugador2["nombre"] + "!")

    elif jugador1["gano"] and jugador2["gano"]:
        if jugador1["puntos"] > jugador2["puntos"]:
            print("\n¡Ganó", jugador1["nombre"], "por puntos!")
        elif jugador2["puntos"] > jugador1["puntos"]:
            print("\n¡Ganó", jugador2["nombre"], "por puntos!")
        else:
            print("\n¡Empate! Ambos ganaron y obtuvieron los mismos puntos.")

    else:
        # Ninguno ganó, aunque uno tenga más puntos
        print("\nAmbos jugadores perdieron.")

        if jugador1["puntos"] > jugador2["puntos"]:
            print(jugador1["nombre"], "obtuvo más puntos, pero no ganó.")
        elif jugador2["puntos"] > jugador1["puntos"]:
            print(jugador2["nombre"], "obtuvo más puntos, pero no ganó.")
        else:
            print("Ambos terminaron con los mismos puntos.")
