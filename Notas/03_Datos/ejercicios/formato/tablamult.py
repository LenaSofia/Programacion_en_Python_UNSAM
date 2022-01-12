numeros = [0,1,2,3,4,5,6,7,8,9]

encabezado = '     '
tablas = ''

for numero in numeros:
    encabezado += f' {numero:^3}'
encabezado += f'\n{"-"*len(encabezado)}'

for numero in numeros:
    numero_puntos = f'{numero}:'
    tablas += f' {numero_puntos:<4s} {"0":^3s} {numero:^3d} '

    for numero_interno in numeros:
        nuevo_numero = numero_interno
        nuevo_numero += numero_interno
        tablas += f'{nuevo_numero:^3d} '

    tablas += '\n'

print(encabezado)
print(tablas)