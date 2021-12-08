import csv

def costo_camion(nombre_archivo):
    costo_total = 0
    archivo = open(nombre_archivo)
    next(archivo)
    lineas = csv.reader(archivo)
    for linea in lineas:
        try:
            precio_fruta = int(linea[1]) * float(linea[2])
            costo_total += precio_fruta
        except ValueError:
            print("Se omitió la linea", linea[0], "porque falta su precio")

    archivo.close()
    return print("Costo total", costo_total)

costo = costo_camion('D:\Python UNSAM\ejercicios_python\Data\missing.csv')

# Output:
# Se omitió la linea Mandarina porque falta su precio
# Se omitió la linea Naranja porque falta su precio
# Costo total 30381.15