# EJERCICIO 1

import pandas as pd

def ejercicio1(ruta):
    df = pd.read_csv(ruta)
    return df

# EJERCICIO 2

def ejercicio2(df):
    df_filtrado = df[(df['Age'] < 35) & (df['Pclass'] == 3)]
    return df_filtrado

# EJERCICIO 3 

def ejercicio3(df):
    total_pasajeros = len(df)
    supervivientes = df[df['Survived'] == 1]
    porcentaje_supervivientes = (len(supervivientes) / total_pasajeros) * 100
    return porcentaje_supervivientes

# EJERCICIO 4

def ejercicio4(df):
    total_pasajeros = len(df)
    hombres = len(df[df['Sex'] == 'male'])
    mujeres = len(df[df['Sex'] == 'female'])
    
    porcentaje_hombres = round((hombres / total_pasajeros) * 100, 2)
    porcentaje_mujeres = round((mujeres / total_pasajeros) * 100, 2)
    
    return (porcentaje_hombres, porcentaje_mujeres)

# EJERCICIO 5

def ejercicio5(df):
    pasajeros_clase = df['Pclass'].value_counts().sort_index()
    return pasajeros_clase.tolist()
