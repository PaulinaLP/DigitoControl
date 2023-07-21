# -*- coding: utf-8 -*-

def calcularDigitoControl(referencia):

    primera_parte = referencia[:7] + referencia[14:]
    segunda_parte = referencia[7:14] + referencia[14:]
    
    # Paso 2: Convertir las letras a números según el mapeo
    conversion_table = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'Ñ': 15, 'O': 16, 'P': 17,
        'Q': 18, 'R': 19, 'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25,
        'Y': 26, 'Z': 27
    }
    primera_parte_numeros = [conversion_table[letra] if letra in conversion_table else int(letra) for letra in primera_parte]
    segunda_parte_numeros = [conversion_table[letra] if letra in conversion_table else int(letra) for letra in segunda_parte]
    
    # Paso 3: Multiplicar cada número por los valores según su posición
    valores_multiplicacion = [13, 15, 12, 5, 4, 17, 9, 21, 3, 7, 1]
    primera_parte_multiplicada = [num * valores_multiplicacion[i] for i, num in enumerate(primera_parte_numeros)]
    segunda_parte_multiplicada = [num * valores_multiplicacion[i] for i, num in enumerate(segunda_parte_numeros)]
    
    # Paso 4: Sumar todos los valores obtenidos en cada lista
    suma_primera_parte = sum(primera_parte_multiplicada)
    suma_segunda_parte = sum(segunda_parte_multiplicada)
    
    # Paso 5: Obtener el resto al dividir por 23
    resto_primera_parte = suma_primera_parte % 23
    resto_segunda_parte = suma_segunda_parte % 23
    
    # Paso 6: Convertir los restos en letras según la tabla de conversión
    tabla_letras = {
        0: 'M', 1: 'Q', 2: 'W', 3: 'E', 4: 'R', 5: 'T', 6: 'Y', 7: 'U', 8: 'I',
        9: 'O', 10: 'P', 11: 'A', 12: 'S', 13: 'D', 14: 'F', 15: 'G', 16: 'H',
        17: 'J', 18: 'K', 19: 'L', 20: 'B', 21: 'Z', 22: 'X'
    }
    primer_digito_control = tabla_letras[resto_primera_parte]
    segundo_digito_control = tabla_letras[resto_segunda_parte]
    return primer_digito_control, segundo_digito_control
