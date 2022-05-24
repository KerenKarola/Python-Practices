import pandas as pd
import matplotlib.pyplot as plt


#Crosstab


df = pd.read_csv('movie_metadata.csv')
df = df[['num_critic_for_reviews','movie_title']]

#Crear un cruce entre columnas y filas a traves de un plot topo bar
ct = pd.crosstab(df['num_critic_for_reviews'],df['movie_title']).plot(kind='bar')

plt.title('Gráfica géneros')

plt.xlabel('Género')
plt.ylabel('Departamento')

#Mostrar la cantidad de cada barra
for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()