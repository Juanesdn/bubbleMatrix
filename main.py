from funciones import *

leer_pos = True

while(leer_pos):
    try:
        n = input("Inserte la cantidad de filas ")
        n = int(n)

        m = input("Inserte la cantidad de columnas ")
        m = int(m)

        leer_pos = False

    except Exception:
        print("Lo siento, solo acepto numeros")


generarMatrizIterativa(n, m)
