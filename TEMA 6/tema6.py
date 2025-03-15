# TEMA 6 - ASPECTOS AVANZADOS

'''
Expresiones regulares



'''

import re

mensaje = 'Esto es una prueba'
mensaje = re.split(' ', mensaje)
print(mensaje[1])

mensaje = 'Esto es una prueba'
mensaje = re.findall('una', mensaje)
print(len(mensaje))