# Ejercicio 3.18

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

# 3.24

"""Volvé a combinar las funciones anteriores para escribir la función especie_promedio_mas_inclinada(lista_arboles)
que, dada una lista de árboles devuelva la especie que en promedio tiene la mayor inclinación y el promedio calculado..

Resultados. Deberías obtener, por ejemplo, que los Álamos Plateados del Parque Los Andes tiene un promedio de
inclinación de 25 grados.

Preguntas extras: ¿Qué habría que cambiar para obtener la especie con un ejemplar más inclinado de toda la ciudad y
no solo de un parque? ¿Podrías dar la latitud y longitud de ese ejemplar? ¿Y dónde se encuentra (lat,lon) el ejemplar
más alto? ¿De qué especie es? """

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


def obtener_especie_promedio_mas_inclinada(lista_arboles):

    arbol_mas_inclinado = {}
    promedio_inclinacion_especie = {}
    especie_mas_inclinada_promedio = {}

    especies_en_parque = especies(lista_arboles)

    for especie in especies_en_parque:
        arbol_mas_inclinado[especie] = obtener_inclinaciones(lista_arboles, especie)
        promedio_inclinacion_especie[especie] = sum(arbol_mas_inclinado[especie]) / len(arbol_mas_inclinado[especie])

    especie_mas_inclinada_promedio[max(promedio_inclinacion_especie, key=promedio_inclinacion_especie.get)] = \
        max(dict.values(promedio_inclinacion_especie))

    return especie_mas_inclinada_promedio

mas_inclinado_GENERAL_PAZ = obtener_especie_promedio_mas_inclinada(GENERAL_PAZ)
print(mas_inclinado_GENERAL_PAZ)

mas_inclinado_LOS_ANDES = obtener_especie_promedio_mas_inclinada(LOS_ANDES)
print(mas_inclinado_LOS_ANDES)

mas_inclinado_CENTENARIO = obtener_especie_promedio_mas_inclinada(CENTENARIO)
print(mas_inclinado_CENTENARIO)

