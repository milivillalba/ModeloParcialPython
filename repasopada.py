import pandas as pd
import matplotlib.pyplot as plt

#leer el archivo csv
df= pd.read_csv('edades.csv')

#converti ela columna ages a data time

df['age']= pd.to_datetime(df['age'], dayfirst=True)

#calcular edades con los años restandole al ano nuevo el ano que nacio
df['edad']= pd.Timestamp.now().year - (df['age']).dt.year

#almacenas las edades mayores a 25 en la variable mayores
mayores= df[df['edad'] >25]

#ordenar las edades de forma ascedentes
ordenar_edades= mayores.sort_values(by='edad')

#determinar cuantas edades existen de cada una 
#primero declarar un dicionario vacio para ir almacenado las cantidad de edades
cantidad_edades={}

#iterar sobre la listas de las edades 
for edad in ordenar_edades['edad']:
    #verificar si ya esta almacenada esa edad en el dicionario
    if edad in cantidad_edades:
     cantidad_edades[edad] += 1
    else:
        cantidad_edades[edad] = 1

#dicionario para mostar las colunas
mostra_discionario={
    'edades': cantidad_edades.keys(),
    'cantidades': cantidad_edades.values()
 }

#datafrime para las columnas
data_frime= pd.DataFrame(mostra_discionario)

print(data_frime)

#graficar 

plt.plot(data_frime['edades'], data_frime['cantidades'])
plt.title("grafico de edada y ejeje")
plt.xlabel('Edades')
plt.ylabel('cantidad de edades')
plt.show()


