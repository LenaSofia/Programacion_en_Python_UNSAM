#def geringosear(claves):

#    diccionario = {}

#    for clave in claves:
#        valor = ''
#        for letra in clave:
#            valor += letra
#            if letra in 'AaEeIiOoUu':
#                valor += 'p' + letra.lower()
#        diccionario[clave] = valor

#    return diccionario

#print(geringosear(['banana', 'manzana', 'mandarina']))

# Output: {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}

#-----------------------------------------------------------------------------------------------------------------------

palabra_geringoso = ''
diccionario = {}

def armarDiccionario(lista_palabras):
    for palabra in lista_palabras:
        def geringosear(palabra):
            for letra in palabra:
                palabra_geringoso += letra
                if letra in "AaEeIiOoUu":
                    palabra_geringoso += 'p' + letra.lower()
        diccionario[palabra] = palabra_geringoso
        return diccionario


armarDiccionario(['banana', 'pera'])