def buscar_precio(fruta):
    archivo = open('../Data/precios.csv', 'rt')

    precio_fruta = 0

    for linea in archivo:
        if (fruta.capitalize() + ',') in linea:
            linea = linea.split(',')
            precio_fruta = float(linea[1])
            break

    if precio_fruta != 0:
        print('El precio de un cajón de', fruta, 'es:', precio_fruta)
    else:
        print(fruta, 'no figura en el listado de precios')
    archivo.close()

buscar_precio('frambuesa')
