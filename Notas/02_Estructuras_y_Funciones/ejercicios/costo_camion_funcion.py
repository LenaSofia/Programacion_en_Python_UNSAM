def costo_camion(nombre_archivo):
    costo_total = 0
    archivo = open(nombre_archivo)
    for linea in archivo:
        linea = linea.split(',')
        if linea[1].isnumeric():
            precio_fruta = int(linea[1]) * float(linea[2])
            costo_total += precio_fruta
    archivo.close()
    return print("Costo total", costo_total)

costo = costo_camion('../Data/camion.csv')
