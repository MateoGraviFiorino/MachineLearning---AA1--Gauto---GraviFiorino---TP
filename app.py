import streamlit as st
import numpy as np
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from adecuar import adecuar, scaler

st.title('Lluvia en Australia')

# Cargar los modelos entrenados
#pipeline_entrenado_c = joblib.load('best_model_c.joblib')
#modelo_clasificacion = joblib.load('clasificacion.joblib')
#pipeline_entrenado_d = joblib.load('best_model_r.joblib')
#modelo_regresion = joblib.load('regresion.joblib')


modelo_clasificacion = joblib.load('best_model_c.joblib')
modelo_regresion = joblib.load('best_model_r.joblib')

# Entrada de datos
st.header('Ingrese las características para la predicción:')
location = st.selectbox('Ubicación',
    ['Adelaide', 'Canberra', 'Cobar', 'Dartmoor',
    'Melbourne', 'MelbourneAirport', 'MountGambier',
    'Sydney', 'SydneyAirport'])

min_temp = st.number_input('Temperatura mínima', value=0.0)
max_temp = st.number_input('Temperatura máxima', value=0.0)
rainfall = st.number_input('Precipitación', value=0.0)
wind_speed = st.number_input('Velocidad del viento', value=0.0)
pressure_9am = st.number_input('Presión 9am', value=0.0)
season = st.selectbox('Estación', ['Primavera', 'Verano', 'Invierno','Otoño'])

evaporation = st.number_input('Evaporación', value=0.0)
temp_3pm = st.number_input('Temperatura a las 3pm', value=0.0)
humedad_3pm = st.number_input('Humedad a las 3pm', value=0.0)
temp_9am = st.number_input('Temperatura a las 9am', value=0.0)
cloud_9am = st.number_input('Nubosidad 9am', value=0.0)

rain_today = st.selectbox('¿Llovió hoy?', ['Yes','No'])

wind_dir_3pm = st.selectbox('Dirección del viento a las 3pm',['NW', 'W', 'NNE', 'ESE', 'E', 'ENE', 'WSW', 'NE','NNW', 'SE', 'S', 'SW', 'WNW', 'N', 'SSW','SSE'])
humedad_9am = st.number_input('Humedad 9am', value=0.0)
wind_gustspeed = st.number_input('Velocidad del viento ráfaga', value=0.0)
presion_3pm = st.number_input('Presión 3pm', value=0.0)
cloud_3pm = st.number_input('Nubosidad 3pm', value=0.0)

wind_dir = st.selectbox('Dirección del viento', ['NW', 'W', 'NNE', 'ESE', 'E', 'ENE', 'WSW', 'NE','NNW', 'SE', 'S', 'SW', 'WNW', 'N', 'SSW','SSE'])
wind_dir_9am = st.selectbox('Dirección del viento 9am', ['NW', 'W', 'NNE', 'ESE', 'E', 'ENE', 'WSW', 'NE','NNW', 'SE', 'S', 'SW', 'WNW', 'N', 'SSW','SSE'])
sunshine = st.number_input('Horas de sol', value=0.0)
wind_speed3pm = st.number_input('Velocidad del viento a las 3pm', value=0.0)
wind_speed9am = st.number_input('Velocidad del viento a las 9am', value=0.0)
rainfall_tomorrow = st.number_input('¿Lloverá mañana?', value=0.0)

input = { 
    'Location': [location], 
    'MinTemp': [min_temp], 
    'MaxTemp': [max_temp], 
    'Rainfall': [rainfall], 
    'Evaporation': [evaporation],
    'Sunshine': [sunshine],
    'WindGustDir': [wind_dir], 
    'WindGustSpeed': [wind_gustspeed], 
    'WindDir9am': [wind_dir_9am], 
    'WindDir3pm':[wind_dir_3pm], 
    'WindSpeed9am':[wind_speed9am],
    'WindSpeed3pm':[wind_speed3pm],
    'Humidity9am':[humedad_9am], 
    'Humidity3pm':[humedad_3pm],
    'Pressure9am':[pressure_9am], 
    'Pressure3pm': [presion_3pm], 
    'Cloud9am':[cloud_9am],
    'Cloud3pm': [cloud_3pm], 
    'Temp9am':[temp_9am],
    'Temp3pm':[temp_3pm], 
    'RainToday':[rain_today],
    'Season':[season]
}


# Botón para realizar la predicción
if st.button("Predecir"):
    try:
        # Realizar la predicción
        df_adecuado = adecuar(input, scaler)
        prediction_clasificacion = modelo_clasificacion.predict(df_adecuado)
        prediction_regresion = modelo_regresion.predict(df_adecuado)
        
        # Mostrar el resultado
        st.subheader('Predicción Modelo Clasificación:')
        st.write(f"La predicción es: {prediction_clasificacion[0]}")
        
        st.subheader('Predicción Modelo Regresión:')
        st.write(f"La predicción es: {prediction_regresion[0]}")
    except Exception as e:
        st.error(f"Error en la predicción: {e}")
