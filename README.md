# PROYECTOFINAL
Predicción en la variación de los precios de los apartamentos en Bogotá D.C.

Se realizó un modelo de predicción de la tasa de variación anual en el precio de los apartamanetos, con el fin de definir una desición de compra para los clientes de la palicación.

Para la realización del modelo de regresión se ejecuto en Google Colab, y se descargo el modelo entrenado de decision tree regression.

Luego se realizó un API por medio de FLASK, posteriormente se diseño una interfaz gráfica con ayuda de streamlit, finalmente se realizó un despliegue en Heroku.

Para ejecutar este proyecto se debe realizar lo siguiente:

1. Abrir el Jupyter Notebook Proyecto en Analitica Aplicada y ejecutar todo el código.
2. Obtener el archivo .plk.
3. Ejecutar el archivo API.
4. Ejecutar el archivo InterfazGrafica.
5. En la terminal ejecutar el siguiente codigo: streamlit run InterfazGrafica.py
6. Finalmente, pronosticar.

Para el despliegue en Heroku tiene que crear 3 diferentes archivos, los cuales se encuentran en el repositorio:

1. setup.sh
2. requirements
3. Procfile

Con el fin de que se haga una conexión entre Heroku y Github para el despliegue de la aplicación.

