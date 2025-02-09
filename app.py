import pandas as pd
import plotly.express as px
import streamlit as st
ruta_csv = r"C:\Users\ldijo\MisProyectos\Carros\vehicles_us.csv"     
car_data = pd.read_csv(ruta_csv) # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)