import csv
import pprint

'''def costo_camion(nombre_archivo):
    costo_total = 0
    archivo = open(nombre_archivo)
    encabezado = next(archivo)
    for n_linea, linea in enumerate(archivo, start=1):
        linea = linea.split(',')
        try:
            precio_fruta = int(linea[1]) * float(linea[2])
            costo_total += precio_fruta
        except ValueError:
            print(f'Fila {n_linea}: No pude interpretar: {linea}')
    print("El costo total es:", costo_total)
    archivo.close()
    return costo_total

costo = costo_camion('../Data/missing.csv')'''

'''f = open('../Data/camion.csv')
filas = csv.reader(f)
encabezados = next(filas)
fila = next(filas)
lista = []

for fila in filas:
    lista.append(list(zip(encabezados, fila)))

pprint.pprint(lista)'''

def costo_camion(nombre_archivo):
    costo_total = 0
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    print(f'El número de cajones es de {ncajones} y el precio por cajon es de {precio}')
    return costo_total

#costo = costo_camion('../../Data/missing.csv')
#print(costo)


#fecha = costo_camion('../../Data/fecha_camion.csv')
#print(fecha)
