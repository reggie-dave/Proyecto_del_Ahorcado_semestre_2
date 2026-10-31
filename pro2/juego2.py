
from pala import palabras
from muneco import mostrar_ahorcado
from estadisticas import estadisticas, guardar_estadisticas, racha
from estructuras import Pila, Cola
import os

def limpiar():
    os.system("cls") 
def iniciar_partida(nombre, dificultad, categoria):
    palabra = palabras(dificultad, categoria)
    palabra_mostrada = ["_" for _ in palabra]
    vidas = 7 if dificultad=="Facil" else 6 if dificultad=="Medio" else 5
    puntos = 0

    letras_correctas = Pila()
    letras_incorrectas = Cola()

    while vidas > 0 and "_" in palabra_mostrada:
        limpiar()
        print("\nJugador:", nombre, " | Puntos:", puntos, " | Vidas:", vidas, " | Racha:", racha)
        print("Palabra:", " ".join(palabra_mostrada))
        print("Letras incorrectas:", ", ".join(letras_incorrectas.items))
        print(mostrar_ahorcado(len(letras_incorrectas.items)))

        letra = input("Ingresa una letra: ").lower()
        if letra in letras_correctas.items or letra in letras_incorrectas.items:
            print("Ya usaste esa letra.")
            continue

        if letra in palabra:
            letras_correctas.apilar(letra)
            for i, l in enumerate(palabra):
                if l == letra:
                    palabra_mostrada[i] = letra
            puntos += 10
            print("¡Letra correcta!")
        else:
            letras_incorrectas.encolar(letra)
            vidas -= 1
            print("Letra incorrecta.")

    if "_" not in palabra_mostrada:
        print("\n🎉 ¡Ganaste! La palabra era:", palabra)
    else:
        print("\n💀 Perdiste. La palabra era:", palabra)
