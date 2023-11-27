import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
import json
from streamlit_lottie import st_lottie
from PIL import Image

#    "feature1": 2024,
#    "feature2": 1,
#    "feature3": 8497486,
#    "feature4": 4725562,
#    "feature5": 4025149,
#    "feature6": 2147195,
#    "feature7": 2721594,
#    "feature8": 1240789,
#    "feature9": 1315881,
#    "feature10": 81.92,
#    "feature11": 68.75,
#    "feature12": 61.74,
#    "feature13": 31.48,
#    "feature14": 33.15,
#    "feature15": 10226,
#    "feature16": 320028.9,
#    "feature17": 1.26,
#    "feature18": 0.35,
#    "feature19": 4.15,
#    "feature20": 1.42,
#    "feature21": 388.474,
#    "feature22": 1028638,
#    "feature23": 1165000,
#    "feature24": 8.18569,
#    "feature25": 0,
#    "feature26": 10


Val3 = 8497486
Val4 = 4725562
Val5 = 4025149
Val6 = 2147195
Val7 = 2721594
Val8 = 1240789
Val9 = 1315881
Val10 = 81.92
Val11 = 68.75
Val12 = 61.74
Val13 = 31.48
Val14 = 33.15
Val15 = 10226
Val16 = 320028.9
Val17 = 1.26
Val18 = 0.35
Val19 = 4.15
Val20 = 1.42
Val21 = 388.474
Val22 = 1028638
Val24 = 8.18569
Val25 = 0
Val26 = 10


# Función para cargar animaciones Lottie desde una URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Esta función permite configurar la página predeterminada para establecer el modo ancho
st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide")

# Agrega esta línea para mostrar la barra de herramientas
st.experimental_set_query_params(**{"show_toolbar": True})

# Código para eliminar el foot
st.markdown("""
<style>
.st-emotion-cache-cio0dv.ea3mdgi1
{
    visibility: hidden;
}
.st-emotion-cache-10pw50.ea3mdgi1
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# Imágenes y animaciones
lottie_coding_1 = load_lottieurl("https://lottie.host/1898be60-3e8a-42ad-b557-b7072c0be749/XJ4uSAlxCX.json")
lottie_coding_2 = load_lottieurl("https://lottie.host/e23c345e-b12a-4e22-b756-7b531f144c9f/7pDjMnqgOr.json")
lottie_coding_3 = load_lottieurl("https://lottie.host/c966c511-8450-465f-b05c-ae1525674ab2/YhRbetg7gC.json")
imagen1 = Image.open("Objetivo8.jpg")
imagen2 = Image.open("Objetivo9.jpg")

# Contenido principal de la aplicación
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hola bienvenido! :wave:")
        st.title("Proyecto en analítica de datos")
        st.write("Integrantes: ")
        st.markdown("""
          >- David Andrés Zacipa
          >- Nicolás Sanchez Salom
          >- Jhoan Nicolás Pinzón
        """)

    with right_column:
        st_lottie(lottie_coding_2, height=500, key="coding")

with st.container():
    st.write("---")
    st.header("Modelo de predicción de la tasa de variación anual de los precios de los apartamentos en Bogotá")
    st.write(
        "¿Quieres saber si es un buen momento para comprar o vender una vivienda en Bogotá? Esta página web te permite estimar el precio de una vivienda según sus características y el año en que deseas adquirirla o venderla. Además, podrás comparar los precios de diferentes zonas de la ciudad y ver las tendencias históricas y futuras. ¡Empieza a explorar esta página web y toma decisiones más informadas y rentables sobre tu patrimonio! ")

with st.container():
    # st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Nuestros objetivos de desarrollo sostenible son los siguientes")

        with right_column:
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(imagen1)
                st.image(imagen2)

with st.container():
    st.write("---")
    st.markdown("""Si el valor del pronóstico está por encima de 10% *NO* es recomendable comprar apartamentos en ese año.
  >Por otro lado, si el dato del pronostico es menor a 10% *SI* es recomendable la compra de apartamentos  
  """)

# Sección de configuración y preguntas en el Sidebar
st.sidebar.title("Configuración y Preguntas")

# Campos iniciales en el Sidebar
Val1 = st.sidebar.number_input("Introduzca el año en el que quiere comprar la vivienda", max_value=2050, min_value=2005,
                               value=2024)
Val2 = st.sidebar.number_input("Introduzca el trimestre en el que quiere comprar la vivienda, trimestre va desde 1 a 4",
                               max_value=4, min_value=1, value=1)

Val23 = st.sidebar.number_input("""Introduzca el salario minimo actual""", value=1165000)

# Checkbox para preguntas adicionales
show_additional_questions = st.sidebar.checkbox("¿Quiere que su pronóstico sea más exacto?")

if show_additional_questions:
    # Preguntas adicionales solo se muestran si el checkbox está marcado

    Val3 = st.sidebar.number_input(
        "Introduzca el dato que le dio La Gran Encuesta Integrada de Hogares (GEIH) realizada por el Dane",
        value=8497486)
    Val4 = st.sidebar.number_input(
        "Introduzca el número de personas que están disponibles para trabajar en la economía Bogotana", value=4725562)
    Val5 = st.sidebar.number_input(
        "Introduzca la fuerza de trabajo comprende a las personas que tienen un empleo remunerado", value=4025149)

    Val6 = st.sidebar.number_input("""Introduzca la población fuera fuerza laboral.
      >Son aquellas que no están empleadas ni buscando activamente empleo.
      >En términos más sencillos, son individuos que no forman parte de
      >la fuerza laboral activa en un momento dado.
      """, value=2147195)
    Val7 = st.sidebar.number_input("""Introduzca los ocupados asalariados.
      >se refiere a las personas que tienen empleo y reciben un salario como compensación por su trabajo.
      """, value=2721594)

    Val8 = st.sidebar.number_input("""Introduzca los ocupados NO asalariados.
      >se refiere a personas que tienen empleo, pero no reciben un salario regular de un empleador. En lugar de eso, estas personas pueden estar involucradas en diferentes formas de empleo que no implican un contrato salarial típico.
      """, value=1240789)

    Val9 = st.sidebar.number_input("Introduzca el número de empleos informales en Colombia, según datos del DANE",
                                   value=1315881)
    Val10 = st.sidebar.number_input("Introduzca el porcentaje de la población en edad de trabajar", value=81.92)
    Val11 = st.sidebar.number_input("""Introduzca la tasa global participación.
      >La tasa global de participación es un indicador que representa el porcentaje de personas en edad de trabajar (población en edad activa) que están participando activamente en la fuerza laboral mediante la búsqueda de empleo o el empleo mismo
      """, value=68.75)
    Val12 = st.sidebar.number_input("Introduzca la tasa de ocupación del año actual", value=61.74)

    Val13 = st.sidebar.number_input("""Introduzca la tasa fuerza potencial del trabajo.
      >Personas que, aunque no están empleadas en el momento, podrían incorporarse al mercado laboral si las condiciones mejoraran o si se presentaran oportunidades adecuadas.
      """, value=31.48)
    Val14 = st.sidebar.number_input("""Introduzca la tasa Informalidad DANE
      >se refiere a la proporción de empleados que trabajan en el sector informal de la economía en comparación con el empleo total.
      """, value=33.15)
    Val15 = st.sidebar.number_input("""Introduzca las compraventas del año actual
      >se refiere al término legal que se refiere al contrato por el cual una parte (el vendedor) se compromete a transferir la propiedad de un bien o servicio a otra parte (el comprador) a cambio de un precio acordado.
      """, value=10226)
    Val16 = st.sidebar.number_input("""Introduzca PIB Precios corrientes
      >El PIB de precios corrientes es una medida del Producto Interno Bruto que valora los bienes y servicios producidos en una economía a los precios actuales de mercado.
      """, value=320028.9)
    Val17 = st.sidebar.number_input("""Introduzca la variación Anual Precios Constantes del 2015
      >La variación anual de precios constantes se refiere a la medida de cambio en el valor de una variable económica, como el Producto Interno Bruto (PIB), corrigiendo los efectos de la inflación.
      """, value=1.26)
    Val18 = st.sidebar.number_input("""Introduzca la variación trimestral Precios constantes del 2015
      >se refiere a la medida del cambio en el valor de una variable económica, como el Producto Interno Bruto (PIB),
      ajustada por la variación en los precios y evaluada en términos reales en relación con el trimestre anterior.
      """, value=0.35)
    Val19 = st.sidebar.number_input("""Introduzca la variación anual precios corrientes
      >Se refiere a la medida del cambio en el valor de una variable económica,
      >como el Producto Interno Bruto (PIB), sin ajustar por la variación en los precios y
      >evaluada en términos nominales en relación con el año anterior.
      """, value=4.15)
    Val20 = st.sidebar.number_input("""Introduzca la variación trimestral precios corrientes
      >se refiere a la medida del cambio en el valor de una variable económica, como el Producto Interno Bruto (PIB),
      >sin ajustar por la variación en los precios y evaluada en términos nominales en relación con el trimestre anterior.
      """, value=1.42)
    Val21 = st.sidebar.number_input("""Introduzca el número de contribuyentes del año actual
      """, value=388.474)

    Val22 = st.sidebar.number_input("""Introduzca el valor aporte voluntario
      >Se refiere a las contribuciones adicionales que una persona realiza a su cuenta de pensiones voluntarias.
      """, value=1028638)

    Val24 = st.sidebar.number_input("""Introduzca el porcentaje de personas desempleadas en Bogotá
      >
      """, value=8.18569)

    Val25 = st.sidebar.number_input("""Introduzca la Variación vs Año anterior
      >Se refiere a la diferencia porcentual entre un valor o indicador en un periodo específico y el mismo periodo del año anterior.
      """, value=0)
    Val26 = st.sidebar.number_input("""Introduzca el número de casas Variación Anual
      >Se refiere a la diferencia porcentual entre el precio medio de las viviendas en un año específico y el precio medio en el mismo periodo del año anterior.
      """, value=10)


# Definir la función de predicción
def get_prediction(data):
    url = "https://127.0.0.1/predict/API/nn"
    payload = json.dumps({
        "feature": {

            "feature1": Val1,
            "feature2": Val2,
            "feature3": Val3,
            "feature4": Val4,
            "feature5": Val5,
            "feature6": Val6,
            "feature7": Val7,
            "feature8": Val8,
            "feature9": Val9,
            "feature10": Val10,
            "feature11": Val11,
            "feature12": Val12,
            "feature13": Val13,
            "feature14": Val14,
            "feature15": Val15,
            "feature16": Val16,
            "feature17": Val17,
            "feature18": Val18,
            "feature19": Val19,
            "feature20": Val20,
            "feature21": Val21,
            "feature22": Val22,
            "feature23": Val23,
            "feature24": Val24,
            "feature25": Val25,
            "feature26": Val26

            #    "feature1": 2024,
            #    "feature2": 1,
            #    "feature3": 8497486,
            #    "feature4": 4725562,
            #    "feature5": 4025149,
            #    "feature6": 2147195,
            #    "feature7": 2721594,
            #    "feature8": 1240789,
            #    "feature9": 1315881,
            #    "feature10": 81.92,
            #    "feature11": 68.75,
            #    "feature12": 61.74,
            #    "feature13": 31.48,
            #    "feature14": 33.15,
            #    "feature15": 10226,
            #    "feature16": 320028.9,
            #    "feature17": 1.26,
            #    "feature18": 0.35,
            #    "feature19": 4.15,
            #    "feature20": 1.42,
            #    "feature21": 388.474,
            #    "feature22": 1028638,
            #    "feature23": 1165000,
            #    "feature24": 8.18569,
            #    "feature25": 0,
            #    "feature26": 10
        }
    })

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()  # Esto generará una excepción si la respuesta tiene un código de error HTTP
        return response.json()['prediction']
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return f"Error: Problema con la solicitud al servidor. {e}"
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        return "Error: Respuesta no válida del servidor. Detalles {str(e)}"

    # response = requests.post(api_url, json=data)
    # print(response.text)  # Agrega esta línea para imprimir la respuesta
    try:
        return response.json()['prediction']
    except json.JSONDecodeError:
        return "Error: Respuesta no válida del servidor."


# Botón para realizar la predicción
if st.sidebar.button("Pronosticar"):
    # Construir el diccionario con los datos para la predicción
    input_data = {"Val1": Val1, "Val2": Val2, "Val3": Val3, "Val4": Val4, "Val5": Val5}

    if show_additional_questions:
        # Agregar las otras preguntas solo si el checkbox está marcado
        input_data.update({
            "Val6": Val6,
            "Val7": Val7,
            "Val8": Val8,
            "Val9": Val9,
            "Val10": Val10,
            "Val11": Val11,
            "Val12": Val12,
            "Val13": Val13,
            "Val14": Val14,
            "Val15": Val15,
            "Val16": Val16,
            "Val17": Val17,
            "Val18": Val18,
            "Val19": Val19,
            "Val20": Val20,
            "Val21": Val21,
            "Val22": Val22,
            "Val23": Val23,
            "Val24": Val24,
            "Val25": Val25,
            "Val26": Val26
        })

    # Obtener la predicción de la API
    prediction = get_prediction(input_data)
    st.success(f"La predicción es: {prediction}")