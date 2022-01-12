numeros = [0,1,2,3,4,5,6,7,8,9]

encabezado = '     '
tablas = ''

for numero in numeros:
    encabezado += f' {numero:^3}'
encabezado += f'\n{"-"*len(encabezado)}'

for numero in numeros:
    numero_puntos = f'{numero}:'
    tablas += f' {numero_puntos:<4s} {"0":^3s} {numero:^3d} '
    nuevo_numero = numero

    for i in range(0,8):
        nuevo_numero += numero
        tablas += f'{nuevo_numero:^3d} '

    tablas += '\n'

print(encabezado)
print(tablas)