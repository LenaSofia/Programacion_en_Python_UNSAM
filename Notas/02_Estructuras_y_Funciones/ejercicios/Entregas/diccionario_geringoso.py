def geringosear(claves):

    diccionario = {}

    for clave in claves:
        valor = ''
        for letra in clave:
            valor += letra
            if letra in 'AaEeIiOoUu':
                valor += 'p' + letra.lower()
        diccionario[clave] = valor

    return diccionario

print(geringosear(['banana', 'manzana', 'mandarina']))

# Output: {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}

