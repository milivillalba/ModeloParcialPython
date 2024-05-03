import pandas as pd
import matplotlib.pyplot as plt

#leer el archivo csv
df = pd.read_csv('edades.csv')

# convertir la columna age a datetime
df["age"] = pd.to_datetime(df["age"], dayfirst=True)

# calcular año actual/  Resta el año de nacimiento de cada persona del año actual para calcular su edad.
df['edad'] = pd.Timestamp.now().year - (df['age']).dt.year

mayores = df[df['edad'] > 25] 

#Ordenar de forma acedente las edades
ordenar_acedente = mayores.sort_values(by='edad')

#crear un dicionario vacio para almacenar las cantidad de s edades.
lista_edades = {}

# Iterar sobre cada valor de la columna 'edad' en el DataFrame 'ordenar_acedente'
for edad in ordenar_acedente['edad']:
    # Verificar si la edad actual ya está en el diccionario 'lista_edades'
    if edad in lista_edades:
        # Si la edad ya está en el diccionario, incrementar su conteo en 1
        lista_edades[edad] += 1
    else:    # Si la edad no está en el diccionario, agregarla con un conteo inicial de 1
        lista_edades[edad] = 1

# Creè un diccionario con dos claves: 'edad' y 'cantidad'
diccionario = {
    'edad': lista_edades.keys(), # Clave 'edad': Contiene todas las edades presentes en el diccionario 'lista_edades'
    'cantidad': lista_edades.values() ,  # Clave 'cantidad': Contiene las cantidades de cada edad presente en el diccionario 'lista_edades'
}

df_edades_ordenadas = pd.DataFrame(diccionario)

print(df_edades_ordenadas)

#GRAFICAR
plt.plot(df_edades_ordenadas['edad'],df_edades_ordenadas['cantidad'])
plt.title("Grafico de edades y cantidad")
plt.xlabel("Edades")
plt.ylabel("Cantidad de edades")
plt.show()
