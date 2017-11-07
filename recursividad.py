import time
import random
import re

from decorators import *




@timer
@profile # Retorna la memoria utilizada por esta funcion y por las funciones ejecutadas dentro de esta
def MatrizRecursiva(n, m, matriz):
    '''
    Confirma que la matriz generada recursivamente contenga burbujas
    '''

    leer_burbuja = True
    bubbles = False # Por default la matriz no contiene burbujas

    field = [] # Campos de la matriz
    generarMatrizRecursiva(matriz, field, n, m, 0, 0)

    while(bubbles == False):

        if(validarBurbujas(matriz, n, m)):   # Valida que la matriz contenga burbujas
            bubbles = True

        else:
            matriz = [] # Reinicio la matriz
            field = [] # Reinicio los campos de la matriz
            generarMatrizRecursiva(matriz, field, n, m, 0, 0) # Si no contiene burbujas vuelve a generar la matriz

    mostrarMatrizRecursiva(matriz, n, m, 0, 0) # Escribe la matriz

    while(leer_burbuja):
        try:
            x = int(input("Digite la posicion en X de la burbuja "))
            y = int(input("Digite la posicion en Y de la burbuja "))

            leer_burbuja = False

        except Exception:
            print("Lo siento, solo acepto numeros")

    borradoRecursivo(matriz, x, y,n-1, m-1, False)
    mostrarMatrizRecursiva(matriz, n, m, 0, 0)

@profile
def MatrizIterativa(n, m, matriz):
    '''
    Confirma que la matriz generada iterativamente contenga burbujas
    '''

    matriz = generarMatrizIterativa(n, m)

    leer_burbuja = True
    bubbles = False # Por default la matriz no contiene burbujas

    while(bubbles == False):

        if(validarBurbujas(matriz, n, m)): # Valida que la matriz contenga burbujas
            bubbles = True
            
        else:
            matriz = generarMatrizIterativa(n, m) # Si no contiene burbujas vuelve a generar la matriz

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) # Escribe la matriz
        for row in matriz]))

      while(leer_burbuja):
        try:
            x = int(input("Digite la posicion en X de la burbuja "))
            y = int(input("Digite la posicion en Y de la burbuja "))

            leer_burbuja = False

        except Exception:
            print("Lo siento, solo acepto numeros")


def validarBurbujas(matriz, n, m):
    '''
    Valido si la matriz contiene burbujas
    '''

    contieneBurbujas = False
    cant_burbujas = 0

    for i in range(0, n-1):
        for j in range(0, m-1):

            # Valido que haya si quiera una burbuja en la matriz iterando en cada posicion posible

            if (i == 0 and j == 0):
                if (matriz[i+1][j] == "x" or matriz[i][j+1] == "x"):
                    cant_burbujas += 1
                
            if (i == 0 and j != 0 and j != m):
                if (matriz[i+1][j] == "x" or matriz[i][j+1] == "x" or matriz[i][j-1] == "x"):
                    cant_burbujas += 1

            if (i == 0 and j == m):
                if (matriz[i-1][j] == "x" or matriz[i][j-1] == "x"):
                    cant_burbujas += 1

            if (i == n and j == 0):
                if (matriz[i-1][j] == "x" or matriz[i][j+1] == "x"):
                    cant_burbujas += 1

            if(i == n and j != m and j != 0):
                if (matriz[i][j-1] == "x" or matriz[i][j+1] == "x" or matriz[i-1][j] == "x"):
                    cant_burbujas += 1

            if(i == n and j == m):
                if (matriz[i-1][j] == "x" or matriz[i][j-1] == "x"):
                    cant_burbujas += 1

            if(j == 0 and i != 0 and i != n):
                if(matriz[i-1][j] == "x" or matriz[i][j+1] == "x" or matriz[i+1][j] == "x"):
                    cant_burbujas += 1
            
            if(j == m and i != 0 and i != n):
                if(matriz[i-1][j] == "x" or matriz[i][j-1] == "x" or matriz[i+1][j] == "x"):
                    cant_burbujas += 1

            if(i != 0 and i != n and j != 0 and j != m):
                if(matriz[i-1][j] == "x" or matriz[i][j+1] == "x" or matriz[i+1][j] == "x" 
                    or matriz[i][j-1] == "x"):
                    cant_burbujas += 1
                

    if (cant_burbujas > 0):
        # Si hay mas de 1 burbuja la matriz puede continuar.
        return True

    else:
        return False


@timer
def generarMatrizIterativa(n, m):
    '''
    Genera una matriz de manera iterativa
    '''
    matriz = []
    field = []

    for i in range(0, n):
        field = []
        for j in range(0, m):
            rnd = random.choice('ox')
            field.append(rnd)
        matriz.append(field)

    return matriz



def generarMatrizRecursiva(matriz ,field, n, m, i, j):
    '''
    Genera una matriz de manera recursiva
    '''

    if (i < n):
        if(j < m):
            rnd = random.choice('ox') # Genero un valor random del string
            field.append(rnd) # Lo adjunto al campo
            generarMatrizRecursiva(matriz, field,n, m, i, j+1) # vuelvo a llamar a la funcion
        else:
            matriz.append(field) # Lo adjunto a la matriz
            field = [] # Reinicio el campo
            generarMatrizRecursiva(matriz, field, n, m, i+1, j-m) # vuelvo a llamar a la funcion 
    field = [] # reinicio el campo para que cuando salga sea 0 



def mostrarMatrizRecursiva(matriz, n, m, i, j):
    '''
    Muestra la matriz de manera recursiva
    '''

    if (i < n):
        if(j < m):
            print('{:4}'.format(matriz[i][j])),
            mostrarMatrizRecursiva(matriz, n, m, i, j+1)
        else:
            print
            mostrarMatrizRecursiva(matriz, n, m, i+1, j-m)


@timer
def borradoRecursivo(matriz, x, y, n , m , noHayX):
    # TODO: buscar la manera de validar si no hay X en todos los casos

    if (noHayX):
        matriz[x][y] = "o"
    else:
        if (x != 0 and x != n and y != 0 and y != m):
            if(matriz[x-1][y] == "x"):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)

            if(matriz[x][y+1] == "x"):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)

            if(matriz[x+1][y] == "x"):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m, noHayX)

            if(matriz[x][y-1] == "x"):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)

            else:
                noHayX = True

        elif (x == 0 and y == 0):
            if(matriz[x][y+1]) == "x":
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)
            else:
                noHayX = True

        elif (x == 0 and y < m and y != 0):
            if(matriz[x][y+1] == "x"):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)
            
            if(matriz[x+1][y] == "x"):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m, noHayX)
                
            if(matriz[x][y-1] == "x"):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True


        elif (x == 0 and y == m):
            if(matriz[x][y-1] == "x"):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True


        elif(y == m and x != 0 and x != n):
            if(matriz[x-1][y] == "x"):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)

            if (matriz[x+1][y] == "x"):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m , noHayX)

            if (matriz[x][y-1] == "x"):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True

        elif(y == m and x == n):
            if(matriz[x-1][y] == "x"):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)
            
            if(matriz[x][y-1] == "x"):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True

        
        elif(x == n and y != 0 and y != m):
            if(matriz[x-1][y] == "x"):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)

            if (matriz[x][y+1] == "x"):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)
            
            if (matriz[x][y-1] == "x"):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True

        elif(x == n and y == 0):
            if(matriz[x-1][y] == "x"):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)
            
            if(matriz[x][y+1] == "x"):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)
            else:
                noHayX = True


        elif (y == 0 and x != n and x != 0):
            if(matriz[x-1][y] == "x"):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)
            
            if(matriz[x][y+1] == "x"):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)

            if(matriz[x+1][y] == "x"):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m, noHayX)
            else:
                noHayX = True






#def verificarAdyacente(matriz, x, y, n, m):
#    if ((x < 0 or y < 0) or (x > n and y >m) )


def main():

    # Booleanos para leer las variables por si no digitan lo requerido
    leer_pos = True
    leer_op = True
    leer_burbuja = True

    # Regular expressions para confirmar que lo escrito sea o un numero o una palabra
    num_pattern = re.compile("[1-2]")
    string_pattern = re.compile("[A-Za-z]+")

    while(leer_pos):
        try:
            n = input("Inserte la cantidad de filas: ")
            n = int(n)

            m = input("Inserte la cantidad de columnas: ")
            m = int(m)

            leer_pos = False

        except Exception:
            print("Lo siento, solo acepto numeros")


    while(leer_op):

        option = input("de que manera desea crear la matriz? \n 1. Recursividad \n 2. Iteratividad \n")
        option = str(option)

        if (num_pattern.match(option) or string_pattern.match(option)):
            matriz = []

            if(option.lower() == "recursividad" or option == "1"):
                MatrizRecursiva(n, m, matriz)

            elif (option.lower() == "iteratividad" or option == "2"):
                MatrizIterativa(n, m, matriz)

            leer_op = False
            
        else:
            print("Lo siento, no entendi")
    


if __name__ == "__main__":
    main()
