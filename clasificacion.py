import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('weatherAUS.csv')

# Las localidades que queremos.
categorias_importantes = [' Adelaide', 'Canberra', 'Cobar', 'Dartmoor', 'Melbourne', 'MelbourneAirport', 'MountGambier', 'Sydney', 'SydneyAirport' ]
df_filtrado = df[df['Location'].isin(categorias_importantes)]
df_filtrado = df_filtrado.drop(['Location', 'Unnamed: 0'], axis = 1)

# Nulos mediana
def nulos_mediana(data, col):
    mediana = data.groupby(['Season'])[col].transform('median')
    data.loc[data[col].isnull(), col] = mediana

# SEGUIR PARTES DE LOS NULOS!!!



## DIVIDIR EN TRAIN Y EN TEST !! revisar
df_train = df_filtrado.loc[df_filtrado['Date'] < '2016-01-01']
df_test = df_filtrado.loc[df_filtrado['Date'] >= '2016-01-01']


## GENERAR DUMMIES 
def generar_dummies_personalizadas(df_train, df_test, columnas_multiple, columnas_simple):
    # Procesar columnas que tienen múltiples variables relacionadas (ej: WindGustDir)
    for col_base in columnas_multiple:
        # Crear dummies para cada variable base en el conjunto de entrenamiento y prueba
        dummies_train = pd.get_dummies(df_train[f'{col_base}_agr'], dtype=int, drop_first=True)
        dummies_test = pd.get_dummies(df_test[f'{col_base}_agr'], dtype=int, drop_first=True)
        
        # Renombrar las columnas dummies para agregar el prefijo de la columna base
        dummies_train = dummies_train.rename(columns=lambda x: f'{col_base}_{x}')
        dummies_test = dummies_test.rename(columns=lambda x: f'{col_base}_{x}')
        
        # Eliminar las columnas originales y las agregadas por la función agrupar_direcciones_viento
        df_train = df_train.drop([col_base, f'{col_base}_agr'], axis=1)
        df_test = df_test.drop([col_base, f'{col_base}_agr'], axis=1)
        
        # Concatenar las dummies con los DataFrames originales
        df_train = pd.concat([df_train, dummies_train], axis=1)
        df_test = pd.concat([df_test, dummies_test], axis=1)

    # Procesar columnas que tienen un único valor categórico binario (ej: RainToday)
    for col in columnas_simple:
        dummies_train = pd.get_dummies(df_train[col], dtype=int, drop_first=True)
        dummies_test = pd.get_dummies(df_test[col], dtype=int, drop_first=True)
        
        # Renombrar la columna dummy a simplemente el nombre de la variable original
        dummies_train = dummies_train.rename(columns={'Yes': col})
        dummies_test = dummies_test.rename(columns={'Yes': col})
        
        # Eliminar las columnas originales
        df_train = df_train.drop(col, axis=1)
        df_test = df_test.drop(col, axis=1)
        
        # Concatenar las dummies con los DataFrames originales
        df_train = pd.concat([df_train, dummies_train], axis=1)
        df_test = pd.concat([df_test, dummies_test], axis=1)
    
    return df_train, df_test

dummies_multiples = ['WindGustDir', 'WindDir9am', 'WindDir3pm']
dummies_simples = ['RainToday'] # RainTomorrow?


## ELIMINAR LAS VARIABLES ESTACION Y DATE
df_train = df_train.drop('Estacion', axis=1)
df_test = df_test.drop('Estacion', axis=1)
df_train = df_train.drop('Date', axis=1)
df_test = df_test.drop('Date', axis=1)


## CREAR DIFERENCIA DE VARIABLES
def crear_diferencias_y_eliminar(df_train, df_test, pares_columnas):
    for col1, col2 in pares_columnas:
        # Crear la nueva columna de diferencia para el conjunto de entrenamiento
        diff_col_name = f'{col1}_menos_{col2}'
        df_train[diff_col_name] = df_train[col1] - df_train[col2]
        
        # Crear la nueva columna de diferencia para el conjunto de prueba
        df_test[diff_col_name] = df_test[col1] - df_test[col2]
        
        # Eliminar las columnas originales
        df_train = df_train.drop([col1, col2], axis=1)
        df_test = df_test.drop([col1, col2], axis=1)
    
    return df_train, df_test

diff_variables = [('Pressure9am', 'Pressure3pm'), ('WindSpeed9am', 'WindSpeed3pm'), ('MaxTemp', 'MinTemp'), 
                  ('Temp3pm', 'Temp9am'), ('Humidity9am', 'Humidity3pm')]


## ESTANDARIZAMOS 
scaler = StandardScaler() # Creamos el objeto scaler
df_scaled_train = scaler.fit_transform(df_train) 
df_scaled_test = scaler.transform(df_test) 

# Los convertimos a DataFrame porque si no son objetos de numpy
df_scaled_train = pd.DataFrame(df_scaled_train, columns=df_train.columns)
df_scaled_test = pd.DataFrame(df_scaled_test, columns=df_test.columns)