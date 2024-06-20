from sklearn.pipeline import Pipeline, FeatureUnion
import pandas as pd
import numpy as np

class Data:
    def __init__(self, df):
        self.df = pd.read_csv('df')

    def filter_locations(self):
        locations_to_keep = [' Adelaide', 'Canberra', 'Cobar', 'Dartmoor', 'Melbourne', 'MelbourneAirport', 'MountGambier', 'Sydney', 'SydneyAirport' ]
        df = self.df[self.df['Location'].isin(locations_to_keep)]
        df = df.drop(['Location', 'Unnamed: 0'], axis=1)
        return df
        
class ImputacionMedianaPorDia:
    def __init__(self, variables):
        self.variables = variables

    def fit(self, df):
        self.medianas_por_dia = {variable: df.groupby('Date')[variable].median() for variable in self.variables}
        return self

    def transform(self, df):
        for variable in self.variables:
            df[variable] = df.apply(lambda row: self.medianas_por_dia[variable][row['Date']] if pd.isnull(row[variable]) else row[variable], axis=1)
        return df
    

class ImputacionMaxima:
    def __init__(self, variables):
        self.variables = variables
        
    def fit(self, df):
        self.maxima = {variable: np.maximum(df['WindSpeed3pm'], df['WindSpeed9am']) for variable in self.variables}
        return self

    def transform(self, df):
        for variable in self.variables:
            df[variable] = df.apply(lambda row: self.maxima[variable] if pd.isnull(row[variable]) else row[variable], axis=1)
        return df


class ImputacionModasPorDia:
    def __init__(self, variables):
        self.variables = variables

    def fit(self, df):
        self.modas_por_dia = {variable: df.groupby('Date')[variable].mode() for variable in self.variables}
        return self

    def transform(self, df):
        for variable in self.variables:
            df[variable] = df.apply(lambda row: self.modas_por_dia[variable][row['Date']] if pd.isnull(row[variable]) else row[variable], axis=1)
        return df
    

class ImputacionWindDir9am:
    def __init__(self, variables):
        self.variables = variables

    def transform(self, df):
        df.loc[df[self.variables].isna, 'WindDir9am'] = df.loc[df[self.variables].isna(), 'WindGustDir']
        return df


class ImputacionWindGustDir:
    def __init__(self, variables):
        self.variables = variables

    def transform(self, df):
        df[self.variables].fillna('N', inplace=True)
        return df
    

class DeterminarEstacion:
    def __init__(self, variables):
        self.variables = variables

    def convertir_a_datetime(self, df):
        # Convertir la columna de fechas a tipo datetime
        df[self.variables] = pd.to_datetime(df[self.variables])
        return df
    
    def determinar_estacion(self):
        # Extraer el mes
        mes = self.variables.month
        # Determinar la estación
        if 3 <= mes <= 5:
            return "Otoño"
        elif 6 <= mes <= 8:
            return "Invierno"
        elif 9 <= mes <= 11:
            return "Primavera"
        else:
            return "Verano"
    
    def asignar_estacion(self, df):
        # Aplicar la función determinar_estacion al DataFrame
        df['Estacion'] = df[self.date_column].apply(lambda x: self.determinar_estacion(x))
        return df


class TrainTest:
    def __init__(self, variable, split_date):
        self.variable = variable
        self.split_date = pd.to_datetime(split_date)

    def division(self, df):
        # Convertir la columna de fechas a tipo datetime si no lo está
        df[self.variable] = pd.to_datetime(df[self.variable])
        
        # Dividir el DataFrame en conjuntos de entrenamiento y prueba
        df_train = df.loc[df[self.variable] < self.split_date]
        df_test = df.loc[df[self.variable] >= self.split_date]
        
        return df_train, df_test


class ImputacionMedianaPorEstacion:
    def __init__(self, variables):
        self.variables = variables
        self.medianas_por_estacion_train = {}

    def fit(self, df_train, variables):
        # Calcular la mediana para cada variable por cada grupo en la columna 'Estacion' en el conjunto de entrenamiento
        self.medianas_por_estacion_train = {variable: df_train.groupby(self.variables)[variable].median() for variable in variables}

    def transformar_fila(self, fila, variables):
        for variable in variables:
            if pd.isnull(fila[variable]):
                fila[variable] = self.medianas_por_estacion_train[variable][fila[self.variables]]
        return fila

    def transform(self, df_train, df_test, variables):
        # Aplicar la función a cada fila del DataFrame
        df_train = df_train.apply(lambda fila: self.transformar_fila(fila, variables), axis=1)
        df_test = df_test.apply(lambda fila: self.transformar_fila(fila, variables), axis=1)
        return df_train, df_test


class AgruparDireccionesViento:
    def __init__(self, variables):
        self.variables = variables

    def determinar_viento(self, viento):
        if viento in ["NE", "ENE", "ESE"]:
            return "E"
        elif viento in ["SSE", "SE", "SSW"]:
            return "S"
        elif viento in ["NNE", "NNW", "NW"]:
            return "N"
        else:
            return "W"

    def fit(self):
        return self #este no se bien que va...

    def transform(self, df_train, df_test):
        for var in self.variables:
            df_train[f'{var}_agr'] = df_train[var].apply(lambda x: self.determinar_viento(x))
            df_train = df_train.drop(var, axis=1)
            df_test[f'{var}_agr'] = df_test[var].apply(lambda x: self.determinar_viento(x))
            df_test = df_test.drop(var, axis=1)
        return df_train, df_test

class CrearDummies:
    def __init__(self, variables):
        self.variables = variables

    def fit(self, df_train, df_test):
        return self

    def transform(self, df_train):
        for var in self.variables:
            dummies = pd.get_dummies(df_train[var], prefix=var, drop_first=True)
            df_train = df_train.drop(var, axis=1)
            df_train = pd.concat([df_train, dummies], axis=1)
        return df_train

class CrearDiferenciasYEliminar:
    def __init__(self, pares_columnas):
        self.pares_columnas = pares_columnas

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        for col1, col2 in self.pares_columnas:
            diff_col_name = f'{col1}_menos_{col2}'
            X[diff_col_name] = X[col1] - X[col2]
            X = X.drop([col1, col2], axis=1)
        return X