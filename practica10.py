import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('adult_data.csv')
# Previsualizar
print(df.head())

# Dimensión del dataframe
print(df.shape)

# Contar
print(df.count())

# Obtener los nombres de las columnas en una lista
col_names = df.columns.tolist()
# Iterar sobre la lista
for column in col_names:
    print("Valores nulos en <" + column + ">:" + str(df[column].isnull().sum()))

#Reemplazar
d = {'Male' : 'M', 'Female' : 'F'}
df[ 'gender' ] = df[ 'gender' ].apply(lambda x:d[x])
print(df['gender'].head())

#Condición
d = {'<=50K' : '49', '>50K' : '51'}
df[ 'income' ] = df[ 'income' ].apply(lambda x:d[x])
print(df['income'].head())

ct = pd.crosstab(df['gender'], df['income']).plot(kind = 'bar')
plt.xlabel("Género")
plt.ylabel("Ingreso")
for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')
plt.show()
