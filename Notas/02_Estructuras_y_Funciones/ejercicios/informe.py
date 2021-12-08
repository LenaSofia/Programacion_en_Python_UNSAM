# Ejercicio informe.py N°2.15

import csv

def leer_camion(nombre_archivo):
    '''Lee los nombres, cantidad de cajones y precios de frutas y verduras de un archivo y guarda cada fila
    de información como una tupla dentro de una lista (camion)'''
    camion = []

    with open(nombre_archivo, 'rt') as archivo:
        filas = csv.reader(archivo)
        encabezado = next(filas)
        for posicion, fila in enumerate(filas):
            try:
                lote = (fila[0], int(fila[1]), float(fila[2]))
                camion.append(lote)
            except ValueError:
                print('Faltan datos en la línea', posicion, 'del archivo.')
    return camion

camion = leer_camion('../Data/camion.csv')
print(camion)