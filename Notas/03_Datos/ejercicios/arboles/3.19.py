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

#%%

# Ejercicio 3.19

"""Escribí una función especies(lista_arboles) que tome una lista de árboles como la generada en el ejercicio anterior 
y devuelva el conjunto de especies (la columna 'nombre_com' del archivo) que figuran en la lista.

Sugerencia: Usá el comando set como en la Sección 2.5."""

def especies(lista_arboles):

    especies = []

    for diccionario in lista_arboles:
        especies.append(diccionario['nombre_com'])

    especies_unicos = sorted(set(especies))

    return especies_unicos

especies_GENERAL_PAZ = especies(GENERAL_PAZ)
print(especies_GENERAL_PAZ)