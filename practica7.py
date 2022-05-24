import pandas as pd
import matplotlib.pyplot as plt


#Crosstab


df = pd.read_csv('users_completo.csv')
df = df[['gender','is_admin']]

#Crear un cruce entre columnas y filas a traves de un plot topo bar
ct = pd.crosstab(df['gender'],df['is_admin']).plot(kind='bar')

plt.title('Administradores')

plt.xlabel('Género')
plt.ylabel('Admin')

#Mostrar la cantidad de cada barra
for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()