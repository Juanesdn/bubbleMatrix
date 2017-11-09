import time
import random
import re

from decorators import *


@profile # Retorna la memoria utilizada por esta funcion y por las funciones ejecutadas dentro de esta
def MatrizRecursiva(n, m, matriz):
    '''
    Confirma que la matriz generada recursivamente contenga burbujas
    '''

    leer_coordenada = True

    field = [] # Campos de la matriz

    generarMatrizRecursiva(matriz, field, n, m, 0, 0)

    mostrarMatrizRecursiva(matriz, n, m, 0, 0) # Escribe la matriz

    while(leer_coordenada):

        x, y = leerCoordenadas(0, 0)

        if (matriz[x][y] == "x" and validarBurbuja(matriz, x, y,n, m)):

            borradoRecursivo(matriz, x, y,n-1, m-1, False)
            mostrarMatrizRecursiva(matriz, n, m, 0, 0)
            leer_coordenada = False
        else:
            print("No hay burbujas en las coordenadas dadas, digite otra coordenada")

@profile
def MatrizIterativa(n, m, matriz):
    '''
    Confirma que la matriz generada iterativamente contenga burbujas
    '''

    matriz = generarMatrizIterativa(n, m)

    leer_coordenada = True

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) # Escribe la matriz
        for row in matriz]))

    while(leer_coordenada):

        x, y = leerCoordenadas(0, 0)

        if (matriz[x][y] == "x" and validarBurbuja(matriz, x, y, n, m)):

            borradoIterativo(matriz, x, y,n-1, m-1)
            
            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) # Escribe la matriz
            for row in matriz]))

            leer_coordenada = False
        else:
            print("No hay burbujas en las coordenadas dadas, digite otra coordenada")



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


@timer
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


@timer
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
            if(validarArriba(matriz, x, y)):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)

            if(validarDerecha(matriz, x, y)):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)

            if(validarAbajo(matriz, x, y)):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m, noHayX)

            if(validarIzquierda(matriz, x, y)):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True

        elif (x == 0 and y == 0):
            if(validarDerecha(matriz, x, y)):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)

            if(validarAbajo(matriz, x, y)):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y,n, m, noHayX )
            else:
                noHayX = True

        elif (x == 0 and y < m and y != 0):
            if(validarDerecha(matriz, x, y)):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)
            
            if(validarAbajo(matriz, x, y)):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m, noHayX)
                
            if(validarIzquierda(matriz, x, y)):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True


        elif (x == 0 and y == m):
            if(validarAbajo(matriz, x, y)):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m, noHayX)
            
            if(validarIzquierda(matriz, x, y)):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True


        elif(y == m and x != 0 and x != n):
            if(validarArriba(matriz, x, y)):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)

            if (validarAbajo(matriz, x, y)):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m , noHayX)

            if (validarIzquierda(matriz, x, y)):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True

        elif(y == m and x == n):
            if(validarArriba(matriz, x, y)):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)
            
            if(validarIzquierda(matriz, x, y)):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True

        
        elif(x == n and y != 0 and y != m):
            if(validarArriba(matriz, x, y)):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)

            if (validarDerecha(matriz, x, y)):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)
            
            if (validarIzquierda(matriz, x, y)):
                matriz[x][y-1] = "o"
                borradoRecursivo(matriz, x, y-1, n, m, noHayX)
            else:
                noHayX = True

        elif(x == n and y == 0):
            if(validarArriba(matriz, x, y)):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)
            
            if(validarDerecha(matriz, x, y)):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)
            else:
                noHayX = True


        elif (y == 0 and x != n and x != 0):
            if(validarArriba(matriz, x, y)):
                matriz[x-1][y] = "o"
                borradoRecursivo(matriz, x-1, y, n, m, noHayX)
            
            if(validarDerecha(matriz, x, y)):
                matriz[x][y+1] = "o"
                borradoRecursivo(matriz, x, y+1, n, m, noHayX)

            if(validarAbajo(matriz, x, y)):
                matriz[x+1][y] = "o"
                borradoRecursivo(matriz, x+1, y, n, m, noHayX)
            else:
                noHayX = True


@timer
def borradoIterativo(matriz, x, y, n, m):
    coordenadas = []
    cont = 0
    contPos = 0
    hayX = True
    print (x)
    print(y)
    while(hayX):
        
        if (x != 0 and x != n and y != 0 and y != m):
            if(validarArriba(matriz, x, y)):
                coordenadas.append(str(x-1) + "," + str(y))

            if(validarDerecha(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y+1))

            if(validarAbajo(matriz, x, y)):
                coordenadas.append(str(x+1) + "," + str(y))

            if(validarIzquierda(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y-1))

        elif (x == 0 and y == 0):
            if(validarDerecha(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y+1))

            if(validarAbajo(matriz, x, y)):
                coordenadas.append(str(x+1) + "," + str(y))


        elif (x == 0 and y != m and y != 0):
            if(validarDerecha(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y+1))
            
            if(validarAbajo(matriz, x, y)):
                coordenadas.append(str(x+1) + "," + str(y))
                
            if(validarIzquierda(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y-1))



        elif (x == 0 and y == m):
            if(validarAbajo(matriz, x, y)):
                coordenadas.append(str(x+1) + "," + str(y))
            
            if(validarIzquierda(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y-1))


        elif(y == m and x != 0 and x != n):
            if(validarArriba(matriz, x, y)):
                coordenadas.append(str(x-1) + "," + str(y))

            if (validarAbajo(matriz, x, y)):
                coordenadas.append(str(x+1) + "," + str(y))

            if (validarIzquierda(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y-1))


        elif(y == m and x == n):
            if(validarArriba(matriz, x, y)):
                coordenadas.append(str(x-1) + "," + str(y))
            
            if(validarIzquierda(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y-1))

        
        elif(x == n and y != 0 and y != m):
            if(validarArriba(matriz, x, y)):
                coordenadas.append(str(x-1) + "," + str(y))

            if (validarDerecha(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y+1))
            
            if (validarIzquierda(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y-1))


        elif(x == n and y == 0):
            if(validarArriba(matriz, x, y)):
                coordenadas.append(str(x-1) + "," + str(y))
            
            if(validarDerecha(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y+1))


        elif (y == 0 and x != n and x != 0):
            if(validarArriba(matriz, x, y)):
                coordenadas.append(str(x-1) + "," + str(y))
            
            if(validarDerecha(matriz, x, y)):
                coordenadas.append(str(x) + "," + str(y+1))

            if(validarAbajo(matriz, x, y)):
                coordenadas.append(str(x-1) + "," + str(y))

        matriz[x][y] = "o"
        if (len(coordenadas) > 0):
            auxX = coordenadas[0]
            auxY = coordenadas[0]
            auxX = int(auxX[0])
            auxY = int(auxY[2])
            x = auxX
            y = auxY
            del coordenadas[0]
        else:
            hayX = False

        

def validarArriba(matriz, x, y):
    return matriz[x-1][y] == "x"


def validarAbajo(matriz, x, y):
    return matriz[x+1][y] == "x"


def validarDerecha(matriz, x, y):
    return matriz[x][y+1] == "x"


def validarIzquierda(matriz, x, y):
    return matriz[x][y-1] == "x"


def leerCoordenadas(x, y):
    leer_burbuja = True

    while(leer_burbuja):
            try:
                x = int(input("Digite la posicion en X de la burbuja "))
                y = int(input("Digite la posicion en Y de la burbuja "))

                leer_burbuja = False
                return x, y
            except Exception:
                print("Lo siento, solo acepto numeros")
        

def validarBurbuja(matriz, x, y, n, m):
    up = False
    right = False
    down = False
    left = False
    if (x != 0 and x != n and y != 0 and y != m):
            if(validarArriba(matriz, x, y)):
                up = True

            if(validarDerecha(matriz, x, y)):
                right = True

            if(validarAbajo(matriz, x, y)):
                down = True

            if(validarIzquierda(matriz, x, y)):
                left = True

    elif (x == 0 and y == 0):
        if(validarDerecha(matriz, x, y)):
            right = True

        if(validarAbajo(matriz, x, y)):
            down = True


    elif (x == 0 and y != m and y != 0):
        if(validarDerecha(matriz, x, y)):
            right = True
        
        if(validarAbajo(matriz, x, y)):
            down = True
            
        if(validarIzquierda(matriz, x, y)):
            left = True


    elif (x == 0 and y == m):
        if(validarAbajo(matriz, x, y)):
            down = True
        
        if(validarIzquierda(matriz, x, y)):
            left = True


    elif(y == m and x != 0 and x != n):
        if(validarArriba(matriz, x, y)):
            up = True

        if (validarAbajo(matriz, x, y)):
            down = True

        if (validarIzquierda(matriz, x, y)):
            left = True


    elif(y == m and x == n):
        if(validarArriba(matriz, x, y)):
            up = True
        
        if(validarIzquierda(matriz, x, y)):
            left = True

    
    elif(x == n and y != 0 and y != m):
        if(validarArriba(matriz, x, y)):
            up = True

        if (validarDerecha(matriz, x, y)):
            right = True
        
        if (validarIzquierda(matriz, x, y)):
            left = True


    elif(x == n and y == 0):
        if(validarArriba(matriz, x, y)):
            up = True
        
        if(validarDerecha(matriz, x, y)):
            right = True


    elif (y == 0 and x != n and x != 0):
        if(validarArriba(matriz, x, y)):
            up = True
        
        if(validarDerecha(matriz, x, y)):
            right = True

        if(validarAbajo(matriz, x, y)):
            down = True

    if(up or down or left or right):
        return True
    else:
        return False

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
