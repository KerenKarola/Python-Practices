
import pandas as pd


df = pd.read_csv('users_data.csv')

#Reemplazar el texto de un campo por otra cosa
#df['gender'] = df['gender'].replace('Other','O')

#Devolver la suma de los datos duplicados
df.duplicated().sum()
df = df.drop_duplicates(keep='last', subset=['first_name'])
#df.to_csv('usuarios_completo.csv', index=False)
