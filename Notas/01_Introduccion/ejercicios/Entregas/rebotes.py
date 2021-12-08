# rebotes.py
# Archivo de ejemplo

altura_inicio = 100

for vuelta in range(0, 10):
    altura_inicio = altura_inicio * (3/5)
    vuelta += 1
    print(vuelta, round(altura_inicio, 4))