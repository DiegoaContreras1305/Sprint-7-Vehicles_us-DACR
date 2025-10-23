import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("vehicles_us.csv")


st.header("Análisis de vehículos en EE.UU.")


st.subheader("Vista previa del conjunto de datos")
st.write(df.head())


if st.button("Mostrar histograma de precios"):
    fig = px.histogram(df, x="price", nbins=50, title="Distribución de precios de vehículos")
    st.plotly_chart(fig)

if st.button("Mostrar gráfico de dispersión: Precio vs Kilometraje"):
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        color="condition",
        title="Relación entre precio y kilometraje",
        labels={"odometer": "Kilometraje", "price": "Precio"}
    )
    st.plotly_chart(fig_scatter)


