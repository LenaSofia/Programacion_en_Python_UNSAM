from collections import Counter
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
                record = dict(zip(encabezado, fila))
                record['cajones'] = int(record['cajones'])
                record['precio'] = float(record['precio'])
                camion.append(record)
            except ValueError:
                print('Faltan datos en la línea', posicion, 'del archivo.')
    return camion

camion = leer_camion('../../../Data/camion.csv')

print(camion)

#%%

tenencias = Counter()

for s in camion:
    tenencias[s['nombre']] += s['cajones']

print(tenencias)


#%%


camion2 = leer_camion('../../../Data/camion2.csv')

tenencias2 = Counter()

for s in camion2:
    tenencias2[s['nombre']] += s['cajones']

print(tenencias2)


#%%


tenencias_total = tenencias + tenencias2

print(tenencias_total)
