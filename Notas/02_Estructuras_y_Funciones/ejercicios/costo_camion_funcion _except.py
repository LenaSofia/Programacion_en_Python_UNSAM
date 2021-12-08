def costo_camion(nombre_archivo):
    costo_total = 0
    archivo = open(nombre_archivo)
    encabezado = next(archivo)
    for linea in archivo:
        linea = linea.split(',')
        try:
            precio_fruta = int(linea[1]) * float(linea[2])
            costo_total += precio_fruta
        except ValueError:
            print("Se omitió la linea", linea[0], "porque falta su precio")

    archivo.close()
    return print("Costo total", costo_total)

costo = costo_camion('../Data/missing.csv')
