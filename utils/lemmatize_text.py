# -*- coding: utf-8 -*-
"""lemmatize_text.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OfnJ1CpQFKJVkv96MLhcxEcf-CqeO3LX
"""

import nltk
nltk.download('wordnet')
import textblob
from textblob import Word

def lemmatize_text(text):
    return " ".join([Word(word).lemmatize() for word in text.split()])