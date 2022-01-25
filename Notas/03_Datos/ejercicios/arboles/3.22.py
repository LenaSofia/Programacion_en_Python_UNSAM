# 3.18

# Ejercicio 3.18

"""Ejercicio 3.18: Lectura de los árboles de un parque
Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de diccionarios
con la información del parque especificado. La lista debe tener un diccionario por cada árbol del parque elegido.
Dicho diccionario debe tener los datos correspondientes a un árbol (recordá que cada fila del csv corresponde a un árbol).

Sugerencia: basate en la función leer_camion() y usá también el comando zip como hiciste en el Ejercicio 3.9 para
combinar el encabezado del archivo con los datos de cada fila. Inicialmente no te preocupes por los tipos de datos
de cada columna, pero cuando empieces a operar con una columna modificá esta función para que ese dato sea del tipo
adecuado para operar.

Observación: La columna que indica el nombre del parque en el que se encuentra el árbol se llama 'espacio_ve'
en el archivo CSV.

Probá con el parque "GENERAL PAZ" para tener un ejemplo de trabajo, debería darte una lista con 690 árboles."""

import csv


def leer_parque(nombre_archivo, parque):
    archivo_dict = []
    parque_dict = []

    with open(nombre_archivo, 'rt', encoding='utf8') as archivo_abierto:

        archivo = csv.reader(archivo_abierto)

        encabezados = next(archivo)

        for line in archivo:
            line_dict = dict(zip(encabezados, line))
            archivo_dict.append(line_dict)

    for diccionario in archivo_dict:
        if diccionario['espacio_ve'] == parque:
            parque_dict.append(diccionario)

    return parque_dict


# Prueba:

GENERAL_PAZ = leer_parque('../../../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
LOS_ANDES = leer_parque('../../../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
CENTENARIO = leer_parque('../../../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')


#%%

# Ejercicio 3.22

"""Escribí una función obtener_inclinaciones(lista_arboles, especie) que, dada una especie de árbol y una lista de 
árboles como la anterior, devuelva una lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa 
especie. """

def obtener_inclinaciones(lista_arboles, especie):

    inclinaciones = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))

    return inclinaciones

