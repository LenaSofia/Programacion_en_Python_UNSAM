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

# Ejercicio 3.21

"""Escribí una función obtener_alturas(lista_arboles, especie) que, dada una lista de árboles como la anterior y una
especie de árbol (un valor de la columna 'nombre_com' del archivo), devuelva una lista con las alturas (columna
'altura_tot') de los ejemplares de esa especie en la lista.

Observación: Acá sí, fijate de devolver las alturas como números (de punto flotante) y no como cadenas de caracteres.
Podés hacer esto modificando leer_parque.

Usala para calcular la altura promedio y altura máxima de los 'Jacarandá' en los tres parques mencionados.

Resultados de alturas de Jacarandás en tres parques:

Medida	General Paz	Los Andes	Centenario
max	16.0	25.0	18.0
prom	10.2	10.54	8.96"""

def obtener_alturas(lista_arboles, especie):

    alturas = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))

    return alturas

jacaranda_GENERAL_PAZ = obtener_alturas(GENERAL_PAZ, "Jacarandá")
jacaranda_GENERAL_PAZ_max_altura = max(jacaranda_GENERAL_PAZ)
print(jacaranda_GENERAL_PAZ_max_altura)
jacaranda_GENERAL_PAZ_prom_altura = (sum(jacaranda_GENERAL_PAZ)/len(jacaranda_GENERAL_PAZ))
print(jacaranda_GENERAL_PAZ_prom_altura)

jacaranda_LOS_ANDES = obtener_alturas(LOS_ANDES, "Jacarandá")
jacaranda_LOS_ANDES_max_altura = max(jacaranda_LOS_ANDES)
print(jacaranda_LOS_ANDES_max_altura)
jacaranda_LOS_ANDES_prom_altura = (sum(jacaranda_LOS_ANDES)/len(jacaranda_LOS_ANDES))
print(jacaranda_LOS_ANDES_prom_altura)

jacaranda_CENTENARIO = obtener_alturas(CENTENARIO, "Jacarandá")
jacaranda_CENTENARIO_max_altura = max(jacaranda_CENTENARIO)
print(jacaranda_CENTENARIO_max_altura)
jacaranda_CENTENARIO_prom_altura = (sum(jacaranda_CENTENARIO)/len(jacaranda_CENTENARIO))
print(jacaranda_CENTENARIO_prom_altura)