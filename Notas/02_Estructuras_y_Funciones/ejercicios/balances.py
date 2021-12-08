# balances, ejercicio 2.18

'''Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en
precios.csv son los precios de venta en el lugar de descarga del camión.

Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa
informe_diccionario.py (usando las funciones leer_camion() y leer_precios()) y completá el programa para que con los
precios del camión (Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó el camión,
lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla
un balance con estos datos.

Ayuda: hubo una ganancia de algo más de quince mil pesos.'''

# Definición de variables
costo_frutas = {}
ganancia_frutas = {}
costo_total_camion = 0
ganancia_total_camion = 0

# Importo librerías
import csv
import pprint


#Defino funciones

def leer_camion(nombre_archivo):

    '''Lee los nombres, cantidad de cajones y precios de frutas y verduras de un archivo y los agrupa en una lista
    que contiene filas.
    Cada fila es un diccionario que utiliza como claves "nombre", "cajones" y "precios", como valor estos datos'''

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


#Llamo a las funciones

camion = leer_camion('../Data/camion.csv')

precios = leer_precio('../Data/precios.csv')

# Recorro la lista "camion" que contiene filas, cada una de las cuáles es un diccionario. Por cada fila creo
# primero un nuevo diccionario llamado "valor_frutas" en el que asigno los nombres de cada fruta como clave y
# el número de cajones multiplicado por el precio de los cajones como valor. Luego creo un segundo diccionario llamado
# "ganancia_frutas" al que le asigno como clave los nombres de las frutas y como valor la cantidad de cajones
# que cargué en "camion" multiplicada por los precios de venta de esas frutas (en el diccionario precios)

'''for fila in camion:
    costo_frutas[fila.get('nombre')] = int(fila.get('cajones')) * float(fila.get('precio'))
    costo_total_camion += costo_frutas[fila.get('nombre')]

    ganancia_frutas[fila.get('nombre')] = int(fila.get('cajones')) * float(precios[fila.get('nombre')])
    ganancia_total_camion += ganancia_frutas[fila.get('nombre')]'''

for fila_camion in camion:

    costo_frutas[fila_camion['nombre']] = int(fila_camion['cajones']) * float(fila_camion['precio'])
    costo_total_camion += costo_frutas[fila_camion['nombre']]

    ganancia_frutas[fila_camion['nombre']] = int(fila_camion['cajones']) * float(precios[fila_camion['nombre']])
    ganancia_total_camion += ganancia_frutas[fila_camion['nombre']]

print(costo_frutas)
print(ganancia_frutas)
print(costo_total_camion)
print(ganancia_total_camion)

saldo_verduleria = ganancia_total_camion - costo_total_camion

print('El saldo total de la verdulería fue de:', saldo_verduleria)