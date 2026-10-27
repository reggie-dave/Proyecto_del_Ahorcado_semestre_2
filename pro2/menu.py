
# Importamos las funciones de los demás módulos
from juego2 import iniciar_partida
from estadisticas import (
    mostrar_estadisticas,
    reiniciar_estadisticas,
    cargar_estadisticas
)
from instrucciones import mostrar_instrucciones
from chistes import chiste_uno, chiste_dos
from multijugador import iniciar_multijugador

# Solicita un nombre y comprueba que sea válido
def solicitar_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip()

        if not nombre:
            print("El nombre no puede estar vacío.")
            continue

        if len(nombre) > 30:
            print("El nombre no puede superar los 30 caracteres.")
            continue

        if not all(letra.isalpha() or letra.isspace() for letra in nombre):
            print("El nombre solo puede contener letras y espacios.")
            continue

        # Cuenta únicamente las letras del nombre
        cantidad_letras = sum(letra.isalpha() for letra in nombre)

        if cantidad_letras < 5:
            print("El nombre debe tener al menos 5 letras.")
            continue

        return nombre


# Solicita una dificultad válida
def solicitar_dificultad():
    while True:
        dificultad = input(
            "Dificultad (Facil/Medio/Dificil): "
        ).strip().lower()

        if dificultad in ("facil", "medio", "dificil"):
            return dificultad

        print("Dificultad inválida. Escribe Facil, Medio o Dificil.")


# Solicita una categoría válida
def solicitar_categoria():
    while True:
        categoria = input(
            "Categoría (Animales/Tecnologia/Frutas): "
        ).strip().lower()

        if categoria in ("animales", "tecnologia", "frutas"):
            return categoria

        print("Categoría inválida. Escribe Animales, Tecnologia o Frutas.")


# Muestra el menú principal del programa
def menu():
    try:
        # Carga las estadísticas guardadas al iniciar
        cargar_estadisticas()
    except (OSError, ValueError, TypeError) as error:
        print("No se pudieron cargar las estadísticas:", error)

    while True:
        print("\n=== JUEGO DEL AHORCADO ===")
        print("1. Jugar individual")
        print("2. Jugar multijugador")
        print("3. Estadísticas")
        print("4. Instrucciones")
        print("5. Reiniciar estadísticas")
        print("6. Chistes de programadores")
        print("7. Salir")

        try:
            opcion = input("Selecciona una opción: ").strip()

            # Evita aceptar una opción vacía
            if not opcion:
                print("No puede dejar la opción vacía.")
                continue

            # Inicia el juego individual
            elif opcion == "1":
                nombre = solicitar_nombre("Nombre del jugador: ")
                dificultad = solicitar_dificultad()
                categoria = solicitar_categoria()
                iniciar_partida(nombre, dificultad, categoria)

            # Inicia el juego de dos jugadores
            elif opcion == "2":
                dificultad = solicitar_dificultad()
                categoria = solicitar_categoria()
                nombre1 = solicitar_nombre("Nombre del jugador 1: ")

                # Solicita otro nombre si los dos son iguales
                while True:
                    nombre2 = solicitar_nombre("Nombre del jugador 2: ")

                    if nombre1.casefold() != nombre2.casefold():
                        break

                    print("Los jugadores deben tener nombres diferentes.")

                iniciar_multijugador(
                    dificultad,
                    categoria,
                    nombre1,
                    nombre2
                )

            # Muestra las estadísticas
            elif opcion == "3":
                mostrar_estadisticas()

            # Muestra las instrucciones
            elif opcion == "4":
                mostrar_instrucciones()

            # Reinicia las estadísticas después de confirmar
            elif opcion == "5":
                confirmar = input(
                    "¿Seguro que desea reiniciar las estadísticas? (s/n): "
                ).strip().lower()

                if confirmar == "s":
                    reiniciar_estadisticas()
                    print("Estadísticas reiniciadas.")
                elif confirmar == "n":
                    print("Operación cancelada.")
                else:
                    print("Respuesta inválida. Escribe s o n.")

            # Muestra los chistes de programadores
            elif opcion == "6":
                chiste_uno()
                chiste_dos()

            # Finaliza el programa
            elif opcion == "7":
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida. Selecciona un número del 1 al 7.")

        except (EOFError, KeyboardInterrupt):
            # Controla las interrupciones del teclado
            print("\nOperación cancelada. Regresando al menú.")


# Ejecuta el menú al abrir este archivo directamente
if __name__ == "__main__":
    menu()
