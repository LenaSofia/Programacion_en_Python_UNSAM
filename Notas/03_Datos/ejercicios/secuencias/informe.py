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
            record = dict(zip(encabezado, fila))
            try:
                lote = (record['nombre'], int(record['cajones']), float(record['precio']))
                camion.append(lote)
            except ValueError:
                print('Faltan datos en la línea', posicion, 'del archivo.')
    return camion

camion = leer_camion('../../../Data/camion.csv')
print(camion)

fecha_camion = leer_camion('../../../Data/fecha_camion.csv')
print(fecha_camion)