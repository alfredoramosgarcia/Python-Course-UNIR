# -*- coding: utf-8 -*-

# EJERCICIO 1

def ejercicio_1(dni):
    letra = ''
    LETRAS = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    resto = dni % 23
    letra = LETRAS[resto]
        
    return letra


print(ejercicio_1(3103568))

# EJERCICIO 2

def ejercicio_2(precio):
    IVA = 0.21
    precio_total = precio + (precio*IVA)
    return round(precio_total, 2)

print(ejercicio_2(23.5684))

# EJERCICIO 3

def ejercicio_3(diametro):
    PI = 3.1415
    area = PI * ((diametro/2) ** 2)
    return area

print(ejercicio_3(10))

# EJERCICIO 4

def ejercicio_4(n, m):
    cociente = n // m
    resto = n % m
    return cociente, resto

print(ejercicio_4(5, 2))

# EJERCICIO 5

def ejercicio_5(producto1, producto2):
    PESO_1 = 147
    PESO_2 = 2400
    
    peso_total = (producto1 * PESO_1) + (producto2 * PESO_2)
    return peso_total

print(ejercicio_5(1, 2))


