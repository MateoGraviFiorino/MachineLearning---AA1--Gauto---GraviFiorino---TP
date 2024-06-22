import streamlit as st
import joblib
import pandas as pd
from adecuar import adecuar

st.title('Lluvia en Australia')

# Cargar el modelo entrenado
pipeline_entrenado = joblib.load('best_model_c.joblib')
pipeline_entrenado_r = joblib.load('best_model_r.joblib')

# Entrada de datos
st.header('Ingrese las características para la predicción:')
location = st.selectbox('Ubicación', ['Canberra', 'Sydney', 'Melbourne', 'Adelaide', 'MountGambier',
                                      'Cobar', 'MelbourneAirport', 'Dartmoor'])
min_temp = st.number_input('Temperatura mínima', value=0.0)
max_temp = st.number_input('Temperatura máxima', value=0.0)
rainfall = st.number_input('Precipitación', value=0.0)
wind_speed = st.number_input('Velocidad del viento', value=0.0)
pressure_9am = st.number_input('Presion 9am', value=0.0)
season = st.selectbox('Estacion', ['Primavera', 'Verano', 'Otoño', 'Invierno'])
evaporation = st.number_input('Evaporacion', value=0.0)
temp_3pm = st.number_input('Temperatura a las 3pm', value=0.0)
humedad_3pm = st.number_input('Humedad a las 3pm', value=0.0)
temp_9am = st.number_input('Temperatura a las 9am', value=0.0)
cloud_9am = st.number_input('Nubosidad 9am', value=0.0)
rain_today = st.selectbox('Llovio hoy', ['Si', 'No'])
wind_dir_3pm = st.selectbox('Direccion del viento 3pm', ['NW', 'W', 'NNE', 'ESE', 'E', 'ENE', 'WSW', 'NE', 'NNW', 'SE', 'S', 'SW', 'WNW', 'N', 'SSW', 'SSE', 'No hay'])
humedad_9am = st.number_input('Humedad 9am', value=0.0)
wind_gustspeed = st.number_input('Velocidad del viento gust', value=0.0)
presion_3pm = st.number_input('Presion 3pm', value=0.0)
cloud_3pm = st.number_input('Nubosidad 3pm', value=0.0)
wind_dir = st.selectbox('Direccion del viento', ['NW', 'ENE', 'SSE', 'SE', 'E', 'S', 'N', 'WNW', 'ESE', 'NE', 'NNE', 'NNW', 'SW', 'W', 'WSW', 'nan', 'SSW'])
wind_dir_9am = st.selectbox('Direccion del viento 9am', ['NW', 'W', 'NNE', 'ESE', 'E', 'ENE', 'WSW', 'NE', 'NNW', 'SE', 'S', 'SW', 'WNW', 'N', 'SSW', 'SSE', 'No hay'])
sunshine = st.number_input('Sol', value=0.0)
wind_speed3pm = st.number_input('Viento 3pm', value=0.0)
rainfall_tomorrow = st.number_input('Rain Fall tomorrow', value=0.0)

# Crear DataFrame de entrada
input_data = pd.DataFrame({
    'Location': [location],
    'MinTemp': [min_temp],
    'MaxTemp': [max_temp],
    'Rainfall': [rainfall],
    'WindGustSpeed': [wind_speed],
    'Pressure9am': [pressure_9am],
    'Season': [season],
    'Evaporation': [evaporation],
    'Temp3pm': [temp_3pm],
    'Humidity3pm': [humedad_3pm],
    'Temp9am': [temp_9am],
    'Cloud9am': [cloud_9am],
    'RainToday': [rain_today],
    'WindDir3pm': [wind_dir_3pm],
    'Humidity9am': [humedad_9am],
    'wind_gustspeed': [wind_gustspeed],
    'Pressure3pm': [presion_3pm],
    'Cloud3pm': [cloud_3pm],
    'WindGustDir': [wind_dir],
    'WindDir9am': [wind_dir_9am],
    'Sunshine': [sunshine],
    'WindSpeed3pm': [wind_speed3pm]
})


input_data = adecuar(input_data)
# Predicciones
prediccion_c = pipeline_entrenado.predict(input_data)
prediccion_d = pipeline_entrenado_r.predict(input_data)

# Mostrar las predicciones
st.subheader('Predicción Modelo Clasificacion:')
st.write(prediccion_c)

st.subheader('Predicción Modelo Regresion:')
st.write(prediccion_d)


