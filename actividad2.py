import random
import math

# EJERCICIO 1

import random
def ejercicio1():
    lista = []
    i=0
    while(i<15):
        lista.insert(i, random.randint(1,100))
        i += 1
        
    return lista

# EJERCICIO 2

lista = ejercicio1()
def ejercicio2(lista, numero):
    size=len(lista)
    
    for i in range(0,size):
        lista[i] /= numero
    
    return lista

# EJERCICIO 3

import math

lista = ejercicio1()
lista2 = ejercicio2(lista, 10)

def ejercicio3(lista2):
    truncar = lambda x: math.trunc(x)
    lista3 = list(map(truncar, lista2))
    return lista3

# EJERCICIO 4

def ejercicio4(num1, num2):
    
    return math.factorial(num1), math.gcd(num1, num2)

# EJERCICIO 5

lista4 = [1,2,3,1,4,2,5,7,4,3,1]

def ejercicio5(lista4):
    seen = set()
    listaSinRepetidos = []
    
    for item in lista4:
        if item not in seen:
            seen.add(item)
            listaSinRepetidos.append(item)
    
    return listaSinRepetidos

print(ejercicio5(lista4))