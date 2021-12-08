precio_fruta = 0
costo_total = 0

f = open('../Data/camion.csv')
encabezado = next(f)

for linea in f:
    linea = linea.split(',')
    precio_fruta = int(linea[1]) * float(linea[2])
    costo_total += precio_fruta
f.close()

print("Costo total", costo_total)