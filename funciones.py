import time
import random

from decorators import *


@timer
def generarMatrizRecursiva():
    '''
    Genera una matriz de manera recursiva
    '''

    return None

@timer
def generarMatrizIterativa(n, m):
    '''
    Genera una matriz de manera iterativa
    '''
    matriz = generarMatriz(n, m)

    bubbles = False

    while(bubbles == False):

        if(validarBurbujas(matriz, n, m)):
            bubbles = True
        else:
            matriz = generarMatriz(n, m)

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matriz]))


def validarBurbujas(matriz, n, m):
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

def generarMatriz(n, m):
    matriz = []
    field = []

    for i in range(0, n):
        field = []
        for j in range(0, m):
            rnd = random.choice('ox')
            field.append(rnd)
        matriz.append(field)
    
    return matriz
