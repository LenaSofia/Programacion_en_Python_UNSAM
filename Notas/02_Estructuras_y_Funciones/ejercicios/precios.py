# Ejercicio
precio_naranja = 0
f = open('../Data/precios.csv', 'rt')
for linea in f:
    if 'Naranja' in linea:
        linea = linea.split(',')
        precio_naranja = float(linea[1])
        break
f.close()
print('El precio de la naranaja es:', precio_naranja)

# ---------------------------------------------------------

# Extra que me pintó hacer

#fruta = input("Busque el precio de la fruta que quiere comprar: ").capitalize()
#precio_fruta = 0
#f = open('../Data/precios.csv', 'rt')
#for linea in f:
#    if fruta in linea:
#        linea = linea.split(',')
#        precio_fruta = float(linea[1])
#        break
#f.close()
#if precio_fruta != 0:
#    print('El precio de la', fruta, 'es:', precio_fruta)
#else:
#    print("Lo siento, no tenemos", fruta.lower())