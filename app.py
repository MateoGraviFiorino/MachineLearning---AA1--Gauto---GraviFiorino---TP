import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Definir las columnas del DataFrame según el modelo entrenado
columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
           'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
           'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
           'Temp9am', 'Temp3pm', 'Location_Canberra', 'Location_Cobar',
           'Location_Dartmoor', 'Location_Melbourne', 'Location_MelbourneAirport',
           'Location_MountGambier', 'Location_Sydney', 'WindGustDir_ENE',
           'WindGustDir_ESE', 'WindGustDir_N', 'WindGustDir_NE', 'WindGustDir_NNE',
           'WindGustDir_NNW', 'WindGustDir_NW', 'WindGustDir_S', 'WindGustDir_SE',
           'WindGustDir_SSE', 'WindGustDir_SSW', 'WindGustDir_SW', 'WindGustDir_W',
           'WindGustDir_WNW', 'WindGustDir_WSW', 'RainToday_Yes', 'WindDir9am_ENE',
           'WindDir9am_ESE', 'WindDir9am_N', 'WindDir9am_NE', 'WindDir9am_NNE',
           'WindDir9am_NNW', 'WindDir9am_NW', 'WindDir9am_S', 'WindDir9am_SE',
           'WindDir9am_SSE', 'WindDir9am_SSW', 'WindDir9am_SW', 'WindDir9am_W',
           'WindDir9am_WNW', 'WindDir9am_WSW', 'WindDir3pm_ENE', 'WindDir3pm_ESE',
           'WindDir3pm_N', 'WindDir3pm_NE', 'WindDir3pm_NNE', 'WindDir3pm_NNW',
           'WindDir3pm_NW', 'WindDir3pm_S', 'WindDir3pm_SE', 'WindDir3pm_SSE',
           'WindDir3pm_SSW', 'WindDir3pm_SW', 'WindDir3pm_W', 'WindDir3pm_WNW',
           'WindDir3pm_WSW', 'Season_Otoño', 'Season_Primavera', 'Season_Verano']

# Crear un DataFrame vacío con las columnas definidas
df_input = pd.DataFrame(columns=columns)

# Cargar el modelo entrenado
pipeline_entrenado = joblib.load('best_model_c.joblib')

# Interfaz de usuario con Streamlit
st.title('Lluvia en Australia')
st.header('Ingrese las características para la predicción:')

# Widgets para la entrada de datos
location = st.selectbox('Ubicación', ['Canberra', 'Cobar', 'Dartmoor', 'Melbourne', 
                                      'MelbourneAirport', 'MountGambier', 'Sydney'])
min_temp = st.number_input('Temperatura mínima', value=0.0)
max_temp = st.number_input('Temperatura máxima', value=0.0)
rainfall = st.number_input('Precipitación', value=0.0)
evaporation = st.number_input('Evaporación', value=0.0)
sunshine = st.number_input('Horas de sol', value=0.0)
wind_gustspeed = st.number_input('Velocidad de ráfaga del viento', value=0.0)
wind_speed9am = st.number_input('Velocidad del viento a las 9am', value=0.0)
wind_speed3pm = st.number_input('Velocidad del viento a las 3pm', value=0.0)
humidity9am = st.number_input('Humedad a las 9am', value=0.0)
humidity3pm = st.number_input('Humedad a las 3pm', value=0.0)
pressure9am = st.number_input('Presión a las 9am', value=0.0)
pressure3pm = st.number_input('Presión a las 3pm', value=0.0)
cloud9am = st.number_input('Nubosidad a las 9am', value=0.0)
cloud3pm = st.number_input('Nubosidad a las 3pm', value=0.0)
temp9am = st.number_input('Temperatura a las 9am', value=0.0)
temp3pm = st.number_input('Temperatura a las 3pm', value=0.0)
rain_today = st.selectbox('Llovió hoy', ['No', 'Sí'])
wind_dir_9am = st.selectbox('Dirección del viento a las 9am', ['NW', 'W', 'NNE', 'ESE', 'E', 'ENE', 'WSW', 'NE', 'NNW', 'SE', 'S',
       'SW', 'WNW', 'N', 'SSW', 'SSE', 'No hay'])
wind_dir_3pm = st.selectbox('Dirección del viento a las 3pm', ['NW', 'W', 'NNE', 'ESE', 'E', 'ENE', 'WSW', 'NE', 'NNW', 'SE', 'S',
       'SW', 'WNW', 'N', 'SSW', 'SSE', 'No hay'])
season = st.selectbox('Estación', ['Otoño', 'Primavera', 'Verano'])

# Mapeo de valores para variables categóricas
location_map = {'Canberra': 1, 'Cobar': 1, 'Dartmoor': 1, 'Melbourne': 1, 'MelbourneAirport': 1,
                'MountGambier': 1, 'Sydney': 1}
rain_today_map = {'No': 0, 'Sí': 1}
wind_dir_map = {'NW': 1, 'W': 1, 'NNE': 1, 'ESE': 1, 'E': 1, 'ENE': 1, 'WSW': 1, 'NE': 1, 'NNW': 1, 'SE': 1, 'S': 1,
       'SW': 1, 'WNW': 1, 'N': 1, 'SSW': 1, 'SSE': 1, 'No hay': 0}
season_map = {'Otoño': 1, 'Primavera': 1, 'Verano': 1}

# Crear un diccionario con los datos de entrada
input_data = {
    'MinTemp': [min_temp],
    'MaxTemp': [max_temp],
    'Rainfall': [rainfall],
    'Evaporation': [evaporation],
    'Sunshine': [sunshine],
    'WindGustSpeed': [wind_gustspeed],
    'WindSpeed9am': [wind_speed9am],
    'WindSpeed3pm': [wind_speed3pm],
    'Humidity9am': [humidity9am],
    'Humidity3pm': [humidity3pm],
    'Pressure9am': [pressure9am],
    'Pressure3pm': [pressure3pm],
    'Cloud9am': [cloud9am],
    'Cloud3pm': [cloud3pm],
    'Temp9am': [temp9am],
    'Temp3pm': [temp3pm],
    'Location': [location_map.get(location, 0)],
    'RainToday': [rain_today_map.get(rain_today, 0)],
    'WindDir9am': [wind_dir_map.get(wind_dir_9am, 0)],
    'WindDir3pm': [wind_dir_map.get(wind_dir_3pm, 0)],
    'Season': [season_map.get(season, 0)]
}

# Convertir el diccionario a DataFrame
df_input = pd.DataFrame(input_data)

# Realizar la predicción
prediction = pipeline_entrenado.predict(df_input)

# Mostrar la predicción en Streamlit
st.write('Predicción:', prediction)
