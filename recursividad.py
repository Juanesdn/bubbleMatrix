import time
import random

from decorators import *


def MatrizRecursiva(n, m):
    '''
    Confirma que la matriz generada recursivamente contenga burbujas
    '''
    matriz = []
    field = []

    generarMatrizRecursiva(matriz, field, n, m, 0, 0)

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in matriz]))

def MatrizIterativa(n, m):
    '''
    Confirma que la matriz generada iterativamente contenga burbujas
    '''
    matriz = generarMatrizIterativa(n, m)

    bubbles = False

    while(bubbles == False):

        if(validarBurbujas(matriz, n, m)):
            bubbles = True
        else:
            matriz = generarMatrizIterativa(n, m)

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in matriz]))


def validarBurbujas(matriz, n, m):
    '''
    Valido si la matriz contiene burbujas
    '''
    contieneBurbujas = False
    cant_burbujas = 0

    for i in range(0, n-1):
        for j in range(0, m-1):

            if (i == 0 and j == 0):
                if (matriz[i+1][j] == "x" and matriz[i][j+1] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1
                
            if (i == 0 and j != 0 and j != m):
                if (matriz[i+1][j] == "x" and matriz[i][j+1] == "x" and matriz[i][j-1] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1

            if (i == 0 and j == m):
                if (matriz[i-1][j] == "x" and matriz[i][j-1] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1

            if (i == n and j == 0):
                if (matriz[i-1][j] == "x" and matriz[i][j+1] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1

            if(i == n and j != m and j != 0):
                if (matriz[i][j-1] == "x" and matriz[i][j+1] == "x" and matriz[i-1][j] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1

            if(i == n and j == m):
                if (matriz[i-1][j] == "x" and matriz[i][j-1] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1

            if(j == 0 and i != 0 and i != n):
                if(matriz[i-1][j] == "x" and matriz[i][j+1] == "x" and matriz[i+1][j] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1
            
            if(j == m and i != 0 and i != n):
                if(matriz[i-1][j] == "x" and matriz[i][j-1] == "x" and matriz[i+1][j] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1

            if(i != 0 and i != n and j != 0 and j != m):
                if(matriz[i-1][j] == "x" and matriz[i][j+1] == "x" and matriz[i-1][j] == "x" 
                    and matriz[i][j-1] == "x"):
                    print("en la posicion: (" + str(i) + ", " + str(j) + ")" )
                    cant_burbujas += 1
                

    if (cant_burbujas > 0):
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


@timer
def generarMatrizRecursiva(matriz ,field, n, m, i, j):
    '''
    Genera una matriz de manera recursiva
    '''

    if (i < n):
        if(j < m):
            rnd = random.choice('ox')
            field.append(rnd)
            generarMatrizRecursiva(matriz, field,n, m, i, j+1)
        else:
            matriz.append(field)
            field = []
            generarMatrizRecursiva(matriz, field, n, m, i+1, j-m)



def main():
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


    #MatrizIterativa(n, m)
    MatrizRecursiva(n, m)

if __name__ == "__main__":
    main()
