#AUTORES -> PABLO FAJARDO ID:725804 - JOHAN CASTILLO ID:726154

def cifrado_sustitucion(mensaje):
    tabla_equivalencia = {
        'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y',
        'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S',
        'M': 'D', 'N': 'F', 'Ñ': 'G', 'O': 'H', 'P': 'J', 'Q': 'K',
        'R': 'L', 'S': 'Ñ', 'T': 'Z', 'U': 'X', 'V': 'C', 'W': 'V',
        'X': 'B', 'Y': 'N', 'Z': 'M'
    }

    mensaje_encriptado = ''
    for letra in mensaje:
        if letra.upper() in tabla_equivalencia:
            letra_encriptada = tabla_equivalencia[letra.upper()]
            if letra.isupper():
                mensaje_encriptado += letra_encriptada
            else:
                mensaje_encriptado += letra_encriptada.lower()
        else:
            mensaje_encriptado += letra

    return mensaje_encriptado


# Obtener el mensaje desde la consola
mensaje_original = input("Ingrese el mensaje a encriptar: ")

# Aplicar el cifrado de sustitución al mensaje ingresado
mensaje_cifrado = cifrado_sustitucion(mensaje_original)

# Imprimir el resultado
print("Mensaje original:", mensaje_original)
print("Mensaje cifrado:", mensaje_cifrado)
