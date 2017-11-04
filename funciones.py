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
    matriz = []
    field = []

    for i in range(0, n):
        field = []
        for j in range(0, m):
            rnd = random.choice('ox')
            field.append(rnd)
        matriz.append(field)

    
    
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matriz]))

