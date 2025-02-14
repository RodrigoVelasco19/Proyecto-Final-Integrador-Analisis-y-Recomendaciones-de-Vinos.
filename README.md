# Proyecto Final Integrador: Análisis y Recomendaciones de Vinos.
   <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Imagenes/main/Vino2.jpg" width="70%">

Este proyecto es el resultado de un análisis integral del dataset de reseñas de vinos de Kaggle (Wine Reviews). Se han aplicado técnicas de Exploración y Transformación de Datos (EDA y ETL), Machine Learning y Procesamiento de Lenguaje Natural (NLP) para extraer información valiosa y construir un sistema de recomendación de vinos basado en reseñas.

📊 Contenido del Proyecto

El proyecto está dividido en cuatro etapas principales:

🔍 1. Exploración y Limpieza de Datos (EDA & ETL)

      🔹 Carga del dataset desde la API de Kaggle.
      
      🔹 Análisis exploratorio para identificar valores nulos, duplicados e inconsistencias.
      
      🔹 Manejo de valores faltantes y justificación de las estrategias aplicadas.
      
      🔹 Visualización de distribuciones y patrones clave.
                 
📊 2. Análisis de Precios y Factores de Calidad

      🔹 Evaluación de la relación entre precio y puntuación de los vinos.
      
      🔹 Identificación de regiones y variedades de uva con mejor relación calidad-precio.
      
      🔹 Aplicación de técnicas de regresión para predecir el precio de un vino según sus características.

🧠 3. Análisis de Sentimiento en Reseñas (NLP)

      🔹 Limpieza de datos: eliminación de stopwords y lematización.
      
      🔹 Análisis de frecuencia de palabras en vinos bien puntuados vs. mal puntuados.
      
      🔹 Construcción de un modelo de análisis de sentimiento para clasificar reseñas como positivas o negativas.
      
      🔹 Visualización de resultados con nubes de palabras.
      
🍷 4. Sistema de Recomendación de Vinos

      🔹 Modelo basado en contenido: recomendaciones en función de similitudes en características como variedad, país y bodega.


🚀 Tecnologías Utilizadas

🔹 Python (Pandas, NumPy, Scikit-learn, NLTK)

🔹 Visualización (Matplotlib, Seaborn, WordCloud)

🔹 Machine Learning (Regresión, TF-IDF, Cosine Similarity, Modelos de Recomendación)

📂 Estructura del Repositorio

📂 Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos  
│── 📂 data               # Contiene los datasets utilizados en el análisis  
│   │── winemag-data-130k-v2.csv            # Dataset original de Kaggle  
│   │── winemag-data_first150k.csv          # Segundo dataset de Kaggle  
│   │── wine_reviews_cleaned.csv            # Dataset procesado después de EDA & ETL  
│  
│── 📂 notebooks          # Notebooks con el desarrollo del proyecto  
│   │── 01_EDA_ETL.ipynb                      # Exploración y limpieza de datos  
│   │── 02_Analisis_Precios_Calidad.ipynb     # Relación precio-calidad y predicción de precios  
│   │── 03_Analisis_Sentimiento_NLP.ipynb     # Análisis de sentimiento en reseñas  
│   │── 04_Modelo_Recomendacion.ipynb         # Modelos de recomendación de vinos  
│  
│── 📂 utils              # Funciones auxiliares utilizadas en los notebooks  
│   │── remove_stopwords.py                     # Función para eliminar stopwords de texto en inglés  
│   │── lemmatize_text.py     # Función para lematizar texto   
│   │── analizar_frecuencia_palabras.py   # Función para analizar las palabras más comunes   
│  
│── 📂 images             # Visualizaciones del proyecto     
│  
│── requirements.txt      # Lista de librerías necesarias para ejecutar el proyecto  
│── README.md             # Descripción del proyecto  

## Resumen y conclusiones

1. Exploración y Limpieza de Datos (EDA & ETL)
   
   🔹 Los datos de partida para el proyecto son 2 datasets de Kaggle, cuya información es similar: cada fila representa un vino, y la información referida al mismo se distribuye en varias columnas: país de origen, reseña, puntaje, precio, etc.

   🔹 Se unió toda la información en un único dataframe concatenando la información original. A su vez, se decide eliminar las columnas que no aportan información relevante respecto a los objetivos definidos para el proyecto.

   🔹 El df resultante de la concatenación posee 280.901 filas. En base a la relevancia para los objetivos del proyecto, se conservaron las siguientes 7 columnas:

         country: País de origen del vino.

         description: Reseña escrita del vino. Puede incluir notas de sabor, aroma y recomendaciones.

         points: Puntuación del vino en una escala de 0 a 100, donde valores más altos indican mejor calidad.

         price: Precio del vino en dólares.

         province: Provincia o estado dentro del país donde se produce el vino.

         variety: Tipo de uva con la que se produce el vino (ej. Cabernet Sauvignon, Merlot, Malbec).

         winery: Nombre de la bodega que produce el vino.
   
   🔹 Se eliminaron las filas duplicadas y aquellas que poseian valores nulos.

   🔹 Para evitar distorsiones, se eliminaron los precios identificados como outliers.

      <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Boxplot%20precio.jpg" alt="Boxplot Precio" width="600">

   🔹 Por representar pocos valores y encontrarse dentro de la escala lógica, se mantuvieron las puntuaciones identificadas como outliers.

    <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Boxplot%20puntuación.jpg" alt="Boxplot Precio" width="600">  

    🔹 Se analizó la distribución de vinos en función de la puntuación (valores discretos).
   
     <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Distribución%20puntuación.jpg" alt="Boxplot Precio" width="600">  

    🔹 Se analizó la distribución de vinos en función del precio (valores continuos).
   
    <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Distribución%20precio.jpg" alt="Boxplot Precio" width="600">  

    🔹 Se analizó la correlación que existe entre la puntuación y el precio de los vinos.

    <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Correlación%20entre%20puntuación%20y%20precio.jpg" alt="Boxplot Precio" width="600">  

    🔹 Se analizó la distribución de vinos por país.
   
   <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Distribución%20por%20país.jpg" alt="Boxplot Precio" width="600">  

    🔹 Se analizó la distribución de vinos por variedad.
   
    <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Distribución%20por%20variedad.jpg" alt="Boxplot Precio" width="600">  

2. Análisis de Precios y Factores de Calidad

    🔹 Se analiza la distribución de calidad/precio en los distintos vinos.

     <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Distribución%20calidad-precio.jpg" alt="Boxplot Precio" width="600"> 

    🔹 Se analiza que regiones y variedades de uva presentar valores más elevados de este indicador.

     <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Distribución%20calidad-precio%20por%20pais.jpg" alt="Boxplot Precio" width="600"> 

     <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Distribución%20calidad-precio%20por%20variedad.jpg" alt="Boxplot Precio" width="600"> 

    🔹 Se generaron modelos para predecir el precio de un vino en base a las caracteristicas: puntuacion, pais, provincia y variedad.

      - Mediante un modelo de Regresión Lineal se obtuvo el siguiente rendimiento: Mean Squared Error (MSE)= 136.9 y R^2 Score =0.47.

      - Mediante un modelo de Random Forest se obtuvo el siguiente rendimiento: Mean Squared Error (MSE)= 127.6 y R^2 Score =0.50.
   
3. Análisis de Sentimiento en Reseñas (NLP)

    🔹 Mediante la aplicación de Procesamiento de Lenguaje Natural (NLP) sobre las descripciones de los vinos, se identificaron las palabras más frecuentes en los vinos mejor y peor valorados.

     <img src="https://raw.githubusercontent.com/RodrigoVelasco19/Proyecto-Final-Integrador-Analisis-y-Recomendaciones-de-Vinos./main/images/Nube%20de%20palabras%20descripción%20vinos%20mejor%20puntuados.jpg" alt="Boxplot Precio" width="600"> 

    🔹 Se elaboró un modelo de análisis de sentimiento de las descripciones de los vinos, para clasificar las mismas como positivas o negativas y como objetivas o subjetivas.

4. Sistema de Recomendación de Vinos

    🔹 Se generó un modelo de recomendación basado en contenido. Este le permite al usuario del código ingresar un vino específico o un determinado n° de vinos del dataset, y obtener los 5 vinos más similares recomendados con sus caracteristicas.

    🔹 Se utilizó la métrica NDCG (Normalized Discounted Cumulative Gain) para evaluar el rendimiento del modelo, obteniendo muy buenos resultados (NDCG=1 para las pruebas realizadas.
