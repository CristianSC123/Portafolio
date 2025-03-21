from django.shortcuts import render
import requests
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('distiluse-base-multilingual-cased')

def generar_embedding(texto):
    return model.encode(texto).tolist()
