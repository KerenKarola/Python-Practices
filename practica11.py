
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('banco.csv')

#Previsualiación
#print(df.head())


#Dimensión del df
#print(df.shape)

#Obtener datos nulos
# col_names= df.columns.tolist()

# for column in col_names:
#       print("Valores nulos en <" + column + ">: " + str(df[column].isnull().sum()))

#El siguiente método imprime información sobre un DataFrame incluyendo 
#el tipo de índice y las columnas, los valores no nulos y el uso de memoria
#df.info()

#Analiza tanto series numéricas como de objetos
#así como conjuntos de columnas DataFrame de tipos de datos mixtos.

#Esto devuelve una Serie con el tipo de datos de cada columna. El índice del resultado son las columnas del DataFrame original,
#así como las columnas con tipos mixtos se almacenan con el dtype del objeto.
#print(df.dtypes)


#print(df.count())

#print(df.duplicated())
#Suma los datos duplicados
#df.duplicated().sum()


#Analiza tanto series numéricas como de objetos,
#así como conjuntos de columnas DataFrame de tipos de datos mixtos.
#Print(df.describe())


#El siguiente método puede comprobar qué valores son nulos junto al método sum() 
# que permite sumar los valores nulos por columna.
#df.isnull().sum()
