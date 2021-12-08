#cadena = input("Escriba aquí una palabra para geringosearla: ")
#cadena_en_geringoso = cadena

#for letra in cadena:
#    if letra == 'a':
#       cadena_en_geringoso = cadena_en_geringoso.replace('a', 'apa')
#    elif letra == 'e':
#        cadena_en_geringoso = cadena_en_geringoso.replace('e', 'epe')
#    elif letra == 'i':
#        cadena_en_geringoso = cadena_en_geringoso.replace('i', 'ipi')
#    elif letra == 'o':
#        cadena_en_geringoso = cadena_en_geringoso.replace('o', 'opo')
#    elif letra == 'u':
#        cadena_en_geringoso = cadena_en_geringoso.replace('u', 'upu')

#print("La palabra", cadena, "se dice", cadena_en_geringoso, "en geringoso")

#cadena = input("Escriba aquí una palabra para geringosearla: ")
#cadena_en_geringoso = cadena

#for letra in cadena:
#    cadena_en_geringoso = cadena.replace('a', 'apa')
#    cadena_en_geringoso = cadena_en_geringoso.replace('e', 'epe')
#    cadena_en_geringoso = cadena_en_geringoso.replace('i', 'ipi')
#    cadena_en_geringoso = cadena_en_geringoso.replace('o', 'opo')
#    cadena_en_geringoso = cadena_en_geringoso.replace('u', 'upu')

#print("La palabra", cadena, "se dice", cadena_en_geringoso, "en geringoso")

#-----------------------------------------------------------------------------------------------------------------------
#cadena = input("Escriba aquí una palabra para geringosearla: ")
#cadena_en_geringoso = cadena
#vocales = 'AaEeIiOoUu'

#for letra in cadena:
#    if letra in vocales:
#        cadena_en_geringoso = cadena_en_geringoso.replace(letra, letra + 'p' + letra)
#print("La palabra", cadena, "se dice", cadena_en_geringoso, "en geringoso")

#-----------------------------------------------------------------------------------------------------------------------

'''cadena = input("Escriba aquí una palabra para geringosearla: ")
cadena_en_geringoso = ''
vocales = 'AaEeIiOoUu'

for letra in cadena:
    if letra in vocales:
        cadena_en_geringoso += letra + 'p' + letra
    else:
        cadena_en_geringoso += letra
print("La palabra", cadena, "se dice", cadena_en_geringoso, "en geringoso")'''

#----------------------------------------------------------------------------------------

cadena = input("Escriba aquí una palabra para geringosearla: ")
cadena_en_geringoso = ''
vocales = 'AaEeIiOoUu'

for letra in cadena:
    cadena_en_geringoso += letra
    if letra in vocales:
        cadena_en_geringoso += 'p' + letra

print("La palabra", cadena, "se dice", cadena_en_geringoso, "en geringoso")