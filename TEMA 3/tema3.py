# TEMA 3 - PROGRAMACION BASICA 

'''
Estructuras de datos en python:
    - Listas: mutables
    - Tuplas: inmutables
    - Diccionario: estructuras clave-valor
    - Conjuntos: Colecciones no ordenadas de elementos
'''
#Listas

lista = list()

lista.insert(0,1)
lista.insert(0,2)
lista.insert(0,3)


# Diccionarios
diccionario = {
    'clave1': 'Uno',
    'clave2': 'Dos'
}

print(diccionario['clave1'])
diccionario['clave1'] = 335
print(diccionario['clave1']*69)

diccionario2 = dict()
print(diccionario)

# Conjuntos

conjunto = set()

print(conjunto)

'''
Ejecuciones condicionales


if(EXPRESION_LOGICA):
    SENTENCIA_1
    SENTENCIA_2
else:
    SENTENCIA_3
'''

print("Introduzca un numero: ")

number = int(input())

if(number>5):
    print("El numero es ayor que 5")
else:
    print("El numero es menor o igual que 5")

'''
Ejecuciones iterativas

WHILE
-----
while(EXPRESION_LOGICA):
    SENTENCIA_1
    SENTENCIA_2
else:
    SENTENCIA_3
    
FOR
-----

for VARIABLE in OBJETO
    SENTENCIA_1
    SENTENCIA_2
else:
    SENTENCIA_3
    
    
'''

for elemento in diccionario:
    print(elemento)
    
for i in range(0, len(lista), 1):
    print(lista[i])
    
# SENTENCIAS EXTRAS
# break: rompe el bucle cuando se ejecute
# continue: nos saltamos una interaccion del bucle sin que se rompa


'''
Iteradores

iter(OBJETO) -> crea un iterador de un objeto
con cada next(iterador) pasa al siguiente iterador del objeto
'''

cadena = 'Hola que tal'

iterador = iter(cadena)
print(next(iterador))
next(iterador)
print(cadena[iterador])