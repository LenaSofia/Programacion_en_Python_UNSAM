frase_t = ''
frase = input("Introduzca una frase aquí para pasarla a lenguaje inclusivo: ")
palabras = frase.split(' ')
for palabra in palabras:
    if palabra[-1] == 'o':
        palabra = palabra[:-1] + 'e'
    elif len(palabra) > 1 and palabra[-2] == 'o':
        palabra = palabra[:-2] + 'e' + palabra[-1:]
    elif len(palabra) > 2 and palabra[-3] == 'o' and palabra[-1] in ',.;:¿?¡!':
        palabra = palabra[:-3] + 'e' + palabra[-2:]

    if len(frase_t) == 0:
        frase_t += palabra
    else:
        frase_t += ' ' + palabra


print(frase_t)


