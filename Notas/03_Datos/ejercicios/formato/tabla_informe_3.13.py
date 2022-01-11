# Ejercicio 3.13: Recolectar datos

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


def leer_precios(nombre_archivo):
    """Toma un .csv con datos de frutas/verduras y su precio por kilo y convierte esos datos en un diccionario,
    dónde la fruta/verdura es la clave y el precio es el valor"""

    precios = dict()

    with open(nombre_archivo, 'rt') as archivo:
        filas = csv.reader(archivo)

        for posicion, fila in enumerate(filas):
            try:
                precios[fila[0]] = fila[1]
            except:
                print('Faltan datos en la línea', posicion, 'del archivo.')

    return precios


precios_camion = leer_precios('../../../Data/precios.csv')
print(precios_camion)

def hacer_informe(lista_cajones, diccionario_precios):
    '''Recibe una lista de cajones y un diccionario con precios como input y devuelve una lista de tuplas
    (Nombre, Cajones, Precio, Cambio -"Cambio" es la variación respecto al precio cobrado por el productor-)'''

    informe = []

    encabezado = (" Nombre     Cajones     Precio     Cambio  ")
    print(encabezado)

    lineas = ("---------- ---------- ---------- ----------")
    print(lineas)

    for tupla in lista_cajones:
        tupla = list(tupla)
        tupla.append(float(precios_camion[tupla[0]]) - tupla[2])
        tupla = tuple(tupla)
        informe.append(tupla)

        print(f' {tupla[0]:<10s} {tupla[1]:>7d}    {tupla[2]:>8.2f}   {tupla[3]:>8.2f}  ')
    return informe

informe = hacer_informe(camion, precios_camion)