# Proyecto Final Integrador: Análisis y Recomendaciones de Vinos.
Este proyecto es el resultado de un análisis integral del dataset de reseñas de vinos de Kaggle (Wine Reviews). Se han aplicado técnicas de Exploración y Transformación de Datos (EDA y ETL), Machine Learning y Procesamiento de Lenguaje Natural (NLP) para extraer información valiosa y construir un sistema de recomendación de vinos basado en reseñas.

📊 Contenido del Proyecto

El proyecto está dividido en cuatro etapas principales:

🔍 1. Exploración y Limpieza de Datos (EDA & ETL)

      🔹 Carga del dataset desde la API de Kaggle.
      
      🔹 Análisis exploratorio para identificar valores nulos, duplicados e inconsistencias.
Manejo de valores faltantes y justificación de las estrategias aplicadas.
Visualización de distribuciones y patrones clave.
Creación de nuevas variables (ej. segmentación de precios en rangos).
📊 2. Análisis de Precios y Factores de Calidad
Evaluación de la relación entre precio y puntuación de los vinos.
Identificación de regiones y variedades de uva con mejor relación calidad-precio.
Aplicación de técnicas de regresión para predecir el precio de un vino según sus características.
🧠 3. Análisis de Sentimiento en Reseñas (NLP)
Limpieza de datos: eliminación de stopwords, stemming y lematización.
Análisis de frecuencia de palabras en vinos bien puntuados vs. mal puntuados.
Construcción de un modelo de análisis de sentimiento para clasificar reseñas como positivas o negativas.
Visualización de resultados con nubes de palabras.
🍷 4. Sistema de Recomendación de Vinos
Modelo basado en contenido: recomendaciones en función de similitudes en características como variedad, país y bodega.
Modelo basado en filtrado colaborativo: recomendaciones según la similitud entre puntuaciones de usuarios.

🚀 Tecnologías Utilizadas

🔹 Python (Pandas, NumPy, Scikit-learn, NLTK)

🔹 Visualización (Matplotlib, Seaborn, WordCloud)

🔹 Machine Learning (Regresión, TF-IDF, Cosine Similarity, Modelos de Recomendación)
