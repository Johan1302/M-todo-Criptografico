#AUTORES -> PABLO FAJARDO ID:725804 - JOHAN CASTILLO ID:726154

def descifrado_sustitucion(mensaje_cifrado):
    tabla_equivalencia = {
        'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y',
        'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S',
        'M': 'D', 'N': 'F', 'Ñ': 'G', 'O': 'H', 'P': 'J', 'Q': 'K',
        'R': 'L', 'S': 'Ñ', 'T': 'Z', 'U': 'X', 'V': 'C', 'W': 'V',
        'X': 'B', 'Y': 'N', 'Z': 'M'
    }

    mensaje_descifrado = ''
    for letra in mensaje_cifrado:
        if letra.upper() in tabla_equivalencia.values():
            for key, value in tabla_equivalencia.items():
                if letra.upper() == value:
                    if letra.isupper():
                        mensaje_descifrado += key
                    else:
                        mensaje_descifrado += key.lower()
        else:
            mensaje_descifrado += letra

    return mensaje_descifrado


# Obtener el mensaje cifrado desde la consola
mensaje_cifrado = input("Ingrese el mensaje cifrado: ")

# Aplicar el descifrado de sustitución al mensaje cifrado ingresado
mensaje_descifrado = descifrado_sustitucion(mensaje_cifrado)

# Imprimir el resultado
print("Mensaje cifrado:", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)
