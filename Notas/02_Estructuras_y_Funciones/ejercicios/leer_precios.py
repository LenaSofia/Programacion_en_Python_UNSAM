# Ejercicio 2.17: Diccionarios como contenedores

import csv

def leer_precio(nombre_archivo):
    ''''A partir de un conjunto de precios arma un diccionario donde las claves son los nombres de frutas y verduras
    y los valores sean los precios por cajón'''

    diccionario_frutas = {}

    with open(nombre_archivo, 'rt') as archivo:
        filas = csv.reader(archivo)
        for posicion, fila in enumerate(filas):
            try:
                diccionario_frutas[fila[0]] = fila[1]
            except IndexError:
                pass
    return diccionario_frutas

precios = leer_precio('../Data/precios.csv')

print(precios)
