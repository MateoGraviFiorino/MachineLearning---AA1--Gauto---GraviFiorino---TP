import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo
model = joblib.load("modelo_entrenado.pkl")

# Función para realizar las transformaciones de datos necesarias
def preprocess_input(data):
    # Aquí se deben realizar las mismas transformaciones que en el notebook
    # por ejemplo: normalización, codificación, etc.
    # Esto es solo un ejemplo y debe adaptarse según el notebook original
    data = pd.DataFrame(data, index=[0])
    # Transformaciones necesarias...
    return data

# Título de la aplicación
st.title("Predicción de Lluvia en Australia")

# Formularios para ingresar los datos
st.header("Ingrese los datos para realizar la predicción")

input_data = {
    "Location": st.selectbox("Location", ["Adelaide", "Canberra", "Cobar", "Dartmoor", "Melbourne", "MelbourneAirport", "MountGambier", "Sydney", "SydneyAirport"]),
    "MinTemp": st.number_input("MinTemp"),
    "MaxTemp": st.number_input("MaxTemp"),
    "Rainfall": st.number_input("Rainfall"),
    "WindGustSpeed": st.number_input("WindGustSpeed"),
    "Humidity3pm": st.number_input("Humidity3pm"),
    "Pressure3pm": st.number_input("Pressure3pm"),
    "Temp3pm": st.number_input("Temp3pm"),
    # Agregar más campos según sea necesario...
}

# Botón para realizar la predicción
if st.button("Predecir"):
    # Preprocesar los datos de entrada
    data = preprocess_input(input_data)
    
    # Realizar la predicción
    prediction = model.predict(data)
    
    # Mostrar el resultado
    st.write(f"La predicción es: {prediction[0]}")

# Manejo de errores
try:
    # Intentar predecir
    pass
except Exception as e:
    st.error(f"Error en la predicción: {e}")
