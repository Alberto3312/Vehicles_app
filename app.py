import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

# crear header
st.header('Análisis de Datos de Vehículos en EE.UU.')

# crear boton para construir histograma usando las funciones st.write y st.plotly_chart
if st.button('Construir Histograma'):
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# crear boton para construir grafico de dispersion usando las funciones st.write y st.plotly_chart
if st.button('Construir Gráfico de Dispersión'):
    st.write('Gráfico de Dispersión de "odometer" vs "price"')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)
