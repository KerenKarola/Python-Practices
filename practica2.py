import pandas as pd


df = pd.read_csv('usuarios_incompleto.csv')

df['company'] = df['company'].fillna('Other')
df['car'] = df['car'].fillna('Unknown')
df['favorite_app'] = df['favorite_app'].fillna('Whatsapp')
df['avatar'] = df['avatar'].fillna('https://robohash.org/default.png?size=50x50&set=set1')
df['active'] = df['active'].fillna('False')
df['is_admin'] = df['is_admin'].fillna('False')
df['department'] = df['department'].fillna('Other')
df['gender'] = df['gender'].fillna('Other')

df.to_csv('usuarios_incompleto.csv', index=False)
