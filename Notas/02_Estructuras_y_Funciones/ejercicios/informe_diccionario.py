# Ejercicio informe.py N°2.16

import csv
import pprint

def leer_camion(nombre_archivo):
    '''Lee los nombres, cantidad de cajones y precios de frutas y verduras de un archivo y los agrupa en un
    diccionario utilizando "nombre", "cajones" y "precios" como clave y los correspondientes datos como valor'''
    camion = []
    mercaderia = {}

    with open(nombre_archivo, 'rt') as archivo:
        filas = csv.reader(archivo)
        encabezado = next(filas)
        for posicion, fila in enumerate(filas):
            try:
                 mercaderia['nombre'] = fila[0]
                 mercaderia['cajones'] = fila[1]
                 mercaderia['precio'] = fila[2]
                 camion.append(mercaderia.copy())
            except ValueError:
                print('Faltan datos en la línea', posicion, 'del archivo.')
    return camion

camion = leer_camion('../Data/camion.csv')

pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
pp.pprint(camion)
