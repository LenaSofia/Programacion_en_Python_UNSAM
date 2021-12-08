# rebotes.py
# Archivo de ejemplo

'''altura_inicio = 100
altura_salto = 100
contador = 0

while contador < 10:
    altura_inicio = altura_salto
    altura_salto = altura_inicio * (3/5)
    contador += 1
    print("\nVuelta", contador,
          "\n La altura de inicio "
          "fue:", altura_inicio,
          "\n La altura del salto fue:", altura_salto
          )'''

'''altura_inicio = 100
contador = 0

while contador < 10:
    print("Vuelta", contador+1)
    print(round(altura_inicio, 4))
    altura_inicio = altura_inicio * (3/5)
    print(round(altura_inicio, 4), "\n")
    contador += 1'''


#Juan, recursividad
'''def saltar(altura,vueltas):
    if(vueltas >= 10):
        return vueltas
    print(round(altura,4), vueltas)
    vueltas += 1
    saltar(altura * (3/5), vueltas)
saltar(100,0)'''



