import pandas as pd 


#Empieza a leer el archivo csv
df = pd.read_csv('users_data.csv')

#Imprimir los campos nulos del dataframe
#print(df.insull())

#Llenar los campos vacíos de una columna
df['lenguage'] = df['lenguage'].fillna('Other')

#Guardar una copia con las columnas modificadas
df.to_csv('users_modify.csv', index=False)


#df.plot(kind = 'scatter', x= 'Duration', y='Calories')
#print(df)
#plt.show()