#Geringoso rústico

cadena = input("Escriba aquí una palabra para geringosearla: ")
cadena_en_geringoso = ''
vocales = 'AaEeIiOoUu'

for letra in cadena:
    cadena_en_geringoso += letra
    if letra in vocales:
        cadena_en_geringoso += 'p' + letra.lower()

print("La palabra", cadena, "se dice", cadena_en_geringoso, "en geringoso")

# Input: Geringoso / Output: Geperipingoposopo
# Input: apa / Output: apapapa
# Input: boligoma / Output: bopolipigopomapa