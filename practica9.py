import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movie_metadata.csv')

#Previsualiación
#print(df.head())


#Dimensión del df
#print(df.shape)

#Contabilizar cada columna
#print(df.count())

#Obtener los datos nulos de cada columna
#col_names= df.columns.tolist()

# for column in col_names:
#       print("Valores nulos en <" + column + ">: " + str(df[column].isnull().sum()))


#Agrupar clase y sexo la suma de los sobrevivientes
# pclass = df.groupby(['Pclass','Num_critic_for_reviews'])['Movie_title'].sum()
# print(pclass)

#Cruce de tablas
# ct = pd.crosstab(df['color'],df['genres']).plot(kind='bar')

# plt.xlabel('Color')
# plt.ylabel('Géneros')

# for barra in ct.containers:
#       ct.bar_label(barra, label_type='edge')

# plt.show()
