# Extra

"""Preguntas extras: ¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado de toda la ciudad y
no solo de un parque? ¿Podrías dar la latitud y longitud de ese ejemplar? ¿Y dónde se encuentra (lat,lon) el ejemplar
más alto? ¿De qué especie es? """

#%%

import csv


def leer_archivo(nombre_archivo):

    archivo_dict = []

    with open(nombre_archivo, 'rt', encoding='utf8') as archivo_abierto:

        archivo = csv.reader(archivo_abierto)

        encabezados = next(archivo)

        for line in archivo:
            line_dict = dict(zip(encabezados, line))
            archivo_dict.append(line_dict)

    return archivo_dict


# Prueba:

archivo = leer_archivo('../../../Data/arbolado-en-espacios-verdes.csv')

#%%

# 3.24

def especies(lista_arboles):

    especies = []

    for diccionario in lista_arboles:
        especies.append(diccionario['nombre_com'])

    especies_unicos = sorted(set(especies))

    return especies_unicos


def obtener_inclinaciones(lista_arboles, especie):

    inclinaciones = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))

    return inclinaciones


def obtener_especimen_mas_inclinado(lista_arboles):

    arbol_mas_inclinado = {}
    especimen_mas_inclinado = {}

    especies_en_parque = especies(lista_arboles)

    for especie in especies_en_parque:
        arbol_mas_inclinado[especie] = max(obtener_inclinaciones(lista_arboles, especie))

    especimen_mas_inclinado[max(arbol_mas_inclinado, key=arbol_mas_inclinado.get)] = max(dict.values(arbol_mas_inclinado))

    return especimen_mas_inclinado


def buscar_lat_y_long(archivo, arbol):

    nombre_arbol = list(arbol.keys())[0]
    inclinacion_arbol = list(arbol.values())[0]

    arbol_lat_long = dict()

    for ejemplar in archivo:
        if ejemplar['nombre_com'] == nombre_arbol and float(ejemplar['inclinacio']) == inclinacion_arbol:
            arbol_lat_long['nombre_com'] = ejemplar['nombre_com']
            arbol_lat_long['inclinacio'] = ejemplar['inclinacio']
            arbol_lat_long['lat'] = ejemplar['lat']
            arbol_lat_long['long'] = ejemplar['long']

    return arbol_lat_long

especimen_mas_inclinado = obtener_especimen_mas_inclinado(archivo)

ubicacion_especimen_mas_inclinado = buscar_lat_y_long(archivo, especimen_mas_inclinado)
print(ubicacion_especimen_mas_inclinado)
