#solucion_de_errores.py


#Ejercicios de errores en el código

#%%

#Ejercicio 3.1. Función tiene_a()

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

print(tiene_a('UNSAM 2020'))

print(tiene_a('abracadabra'))

print(tiene_a('La novela 1984 de George Orwell'))


# Comentario: El error era semántico y se ubicada en dos lugares, por un lado en las "a", daod que solo eran válidas
# las "a" en minúscula y sin acentuar, cuando pretendíamos que tomara todas las "a" posibles. Y por otro lado por la
# ubicación del "return False", que generaba que, si la primera letra de la frase ingresada era una a, devolviera True,
# y en caso contrario devolviera False y saliera del código (es decir que no siguiera recorriendo la oración en busca
# de otra "a"

#    Lo corregí cambiando: 'if expresion[i] == "a"' por 'if expresion[i] in lista_a'
#    (siendo lista_a = ["a", "á", "A", "Á", "ä", "Ä"]).

# Lo corregí cambiando de lugar el 'return False' y el 'i += 1'

#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    lista_a = ["a", "á", "A", "Á", "ä", "Ä"]
    while i < n:
        if expresion[i] in lista_a:
            return True
        else:
            i += 1
    return False

print(tiene_a('UNSAM 2020'))

print(tiene_a('abracadabra'))

print(tiene_a('La novela 1984 de George Orwell'))




#%%


#Ejercicio 3.2. Función tiene_a(), nuevamente

def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#Comentario: El error era de sintaxis, le faltaban algunos ":" y decía "Falso" en vez de "False".
# Además sólo tomaba la "a" (como en el caso anterior).

# Código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    lista_a = ["a", "á", "A", "Á", "ä", "Ä"]
    while i<n:
        if expresion[i] in lista_a:
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))




#%%


#Ejercicio 3.3. Función tiene_uno()

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#Comentario: El error era semántico y estaba en que la función sólo acepta datos del tipo str y estabamos ingresando
# un dato del tipo int, lo que hice fue convertirlo a str antes de empezar a usarlo (dentro de la función).

# Código corregido:

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))




#%%

#Ejercicio 3.4. Alcances:

def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# Comentario: le faltaba el return c

# Código corregido:

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")




#%%

# Ejercicio 3.5: pisando memoria:

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# Comentario: el problema era que estaba pisando todos los registros anteriores con el nuevo registro porque no cambiaba
# la referencia, por lo que siempre apuntaba al mismo lugar y el último registro pisaba todos los anteriores generando
# que todos cambies y se vuelvan iguales al último. Lo modifiqué agregando un .copy() en camion.append(registro.copy())
# para que no reemplace la referencia sino que copie su contenido y lo ubique en un nuevo lugar en memoria

# Código corregido

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro.copy())
    return camion

camion = leer_camion('../../Data/camion.csv')
pprint(camion)
