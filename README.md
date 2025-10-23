# Sprint-7-Vehicles_us-DACR
Esta aplicación web fue desarrollada como parte del Sprint 7 del curso de análisis de datos. Utiliza Streamlit para crear una interfaz interactiva que permite explorar un conjunto de datos sobre vehículos usados en Estados Unidos.
El objetivo principal es ofrecer una herramienta visual y accesible para analizar variables como el precio, el kilometraje, el año de fabricación y la condición del vehículo.

Funcionalidades principales
- Vista previa del dataset: muestra las primeras filas del archivo vehicles_us.csv para familiarizarse con los datos.
- Histograma de precios: al hacer clic en un botón, se genera un gráfico que muestra la distribución de precios de los vehículos.
- Gráfico de dispersión: otro botón permite visualizar la relación entre el kilometraje y el precio, coloreado por la condición del vehículo.
- Interfaz interactiva: todos los gráficos se generan dinámicamente usando plotly-express y se integran en la app con st.plotly_chart().

