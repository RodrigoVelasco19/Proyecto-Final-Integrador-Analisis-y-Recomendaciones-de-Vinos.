# -*- coding: utf-8 -*-
"""remove_stopwords.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ebi1qjxh72evfQzSCCfj7XwoiIdYbyr-
"""

# Función para eliminar stopwords de un texto en inglés

import nltk
from nltk.corpus import stopwords

# Descargar stopwords de NLTK
nltk.download('stopwords')

# Definir stopwords en inglés
stop_words = set(stopwords.words('english'))

# Eliminación de Stopwords
def remove_stopwords(text):
    words = text.split()  # Tokenizar manualmente
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)