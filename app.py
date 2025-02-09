import pandas as pd
import plotly.express as px
import streamlit as st

data_path = 'vehicles_us.csv'
car_data = pd.read_csv(data_path)

st.title('Datos de carros')

st.write("Elije una de las graficas.")

show_histogram = st.checkbox("Mostrar histograma del odómetro")
show_scatter = st.checkbox("Mostrar gráfico de dispersión entre precio y odómetro")

if show_histogram:
    st.write("### Histograma del Odómetro")
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución del Kilometraje")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write("### Gráfico de Dispersión: Precio vs Odómetro")
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Kilometraje y Precio", 
                             labels={"odometer": "Kilometraje", "price": "Precio"}, opacity=0.5)
    st.plotly_chart(fig_scatter, use_container_width=True)
