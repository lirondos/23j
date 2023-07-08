import os
import string
import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    # Eliminar puntuación y convertir a minúsculas
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text

def remove_stopwords(text):
    # Tokenizar el texto en palabras
    tokens = nltk.word_tokenize(text)

    # Obtener la lista de palabras vacías en español (puedes ajustar el idioma si es necesario)
    stop_words = set(stopwords.words('spanish'))

    # Filtrar las palabras vacías del texto
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Unir las palabras filtradas en un solo texto
    filtered_text = ' '.join(filtered_tokens)

    return filtered_text

def calculate_similarity(documents):
    # Preprocesar y eliminar palabras vacías de los documentos
    preprocessed_documents = [preprocess_text(doc) for doc in documents]
    filtered_documents = [remove_stopwords(doc) for doc in preprocessed_documents]

    # Crear un vectorizador TF-IDF
    vectorizer = TfidfVectorizer()

    # Construir la matriz TF-IDF de términos de documentos
    tfidf_matrix = vectorizer.fit_transform(filtered_documents)

    # Calcular la matriz de similitud del coseno
    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix

# Ruta de la carpeta que contiene los archivos .txt
folder_path = "RUTA A LA CARPETA"

# Leer los archivos .txt y obtener los contenidos
documents = []
document_names = []
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            documents.append(content)
            document_names.append(os.path.splitext(file_name)[0])  # Eliminar la extensión del nombre del archivo

# Descargar la lista de palabras vacías (stop words) si no lo has hecho antes
nltk.download('stopwords')

similarity_matrix = calculate_similarity(documents)

# Visualizar la matriz de similitud como un heatmap con valores y nombres de documentos
fig, ax = plt.subplots()
heatmap = ax.matshow(similarity_matrix, cmap='YlGnBu', interpolation='nearest')

# Agregar los valores en cada celda del heatmap
for i in range(similarity_matrix.shape[0]):
    for j in range(similarity_matrix.shape[1]):
        text = ax.text(j, i, round(similarity_matrix[i, j], 2),
                       ha="center", va="center", color="black")

# Configurar los nombres de los programas en los ejes x e y
ax.set_xticks(np.arange(len(document_names)))
ax.set_yticks(np.arange(len(document_names)))
ax.set_xticklabels(document_names, rotation=90)
ax.set_yticklabels(document_names)

# Mostrar una barra de color para indicar la escala de similitud
plt.colorbar(heatmap)

plt.title('Matriz de Similitud')

plt.show()