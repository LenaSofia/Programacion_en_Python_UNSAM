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

# %%

# Ejercicio 3.20

"""Usando contadores como en el Ejercicio 3.11, escribí una función contar_ejemplares(lista_arboles) que, 
dada una lista como la que generada con leer_parque(), devuelva un diccionario en el que las especies (recordá, 
es la columna 'nombre_com' del archivo) sean las claves y tengan como valores asociados la cantidad de ejemplares en 
esa especie en la lista dada. 

Luego, combiná esta función con leer_parque() y con el método most_common() para informar las cinco especies más 
frecuentes en cada uno de los siguientes parques: 

'GENERAL PAZ'
'ANDES, LOS'
'CENTENARIO'
Resultados de cantidad por especie en tres parques:

General Paz	Los Andes	Centenario
Casuarina: 97	Jacarandá: 117	Plátano: 137
Tipa blanca: 54	Tipa blanca: 28	Jacarandá: 45
Eucalipto: 49	Ciprés: 21	Tipa blanca: 42
Palo borracho rosado: 44	Palo borracho rosado: 18	Palo borracho rosado: 41
Fenix: 40	Lapacho: 12	Fresno americano: 38"""


def contar_ejemplares(lista_arboles):

    from collections import Counter

    contador_arboles_parque = Counter()

    for ejemplar in lista_arboles:
        contador_arboles_parque[ejemplar['nombre_com']] += 1

    return contador_arboles_parque


def encontrar_especies_mas_comunes(nombre_archivo, parque):

    lista_arboles = leer_parque(nombre_archivo, parque)

    total_arboles_parque = contar_ejemplares(lista_arboles)

    ejemplares_mas_comunes = total_arboles_parque.most_common(5)

    return ejemplares_mas_comunes


GENERAL_PAZ = encontrar_especies_mas_comunes('../../../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
print(GENERAL_PAZ)

LOS_ANDES = encontrar_especies_mas_comunes('../../../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
print(LOS_ANDES)

CENTENARIO = encontrar_especies_mas_comunes('../../../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
print(CENTENARIO)