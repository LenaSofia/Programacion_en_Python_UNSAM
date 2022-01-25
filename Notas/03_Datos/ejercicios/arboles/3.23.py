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
#print(GENERAL_PAZ)
LOS_ANDES = leer_parque('../../../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
#print(LOS_ANDES)
CENTENARIO = leer_parque('../../../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
#print(CENTENARIO)


#%%

# Ejercicio 3.23

"""Combinando la función especies() con obtener_inclinaciones() escribí una función especimen_mas_inclinado(
lista_arboles) que, dada una lista de árboles devuelva la especie que tiene el ejemplar más inclinado y su inclinación.

Correlo para los tres parques mencionados anteriormente.

Resultados. Deberías obtener, por ejemplo, que en el Parque Centenario hay un Falso Guayabo inclinado 80 grados."""

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

mas_inclinado_GENERAL_PAZ = obtener_especimen_mas_inclinado(GENERAL_PAZ)
print(mas_inclinado_GENERAL_PAZ)

mas_inclinado_LOS_ANDES = obtener_especimen_mas_inclinado(LOS_ANDES)
print(mas_inclinado_LOS_ANDES)

mas_inclinado_CENTENARIO = obtener_especimen_mas_inclinado(CENTENARIO)
print(mas_inclinado_CENTENARIO)