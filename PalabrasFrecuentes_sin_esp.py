import pypdf
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import SnowballStemmer
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import math

# Lista de los nombres de los archivos PDF
pdf_files = ['psoe.pdf', 'pp.pdf', 'sumar.pdf', 'vox.pdf']

# Lista de etiquetas para los gráficos de barras
labels = ['PSOE', 'PP', 'SUMAR', 'VOX']

# Lista de colores para los gráficos de barras
colors = ['r', 'b', 'pink', 'darkgreen']

# Crea un DataFrame para guardar los resultados del análisis
df = pd.DataFrame(columns=['PDF', 'Palabra', 'Frecuencia'])

# Procesa cada PDF y guarda los resultados en el DataFrame
for i, pdf_file in enumerate(pdf_files):
    # Abre el archivo PDF
    pdf_file_obj = open(pdf_file, 'rb')

    # Lee el contenido del PDF y conviértelo en un objeto PyPDF2
    read_pdf = pypdf.PdfReader(pdf_file_obj)

    # Extrae el texto de cada página del PDF
    text = ""
    for page in range(len(read_pdf.pages)):
        text += read_pdf.pages[page].extract_text()

    with open('programa '+labels[i]+'.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    # Tokeniza el texto en palabras
    tokens = word_tokenize(text)

    # Elimina las palabras vacías y las stopwords
    exclude_words = ['programa', 'así']
    stop_words = set(stopwords.words('spanish'))
    stop_words.update(exclude_words)
    words = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]

    # Crea un stemmer para español
    stemmer = SnowballStemmer('spanish')

    # Obtiene los sinónimos y palabras relacionadas de cada palabra
    related_words = []
    for word in words:
        synsets = wn.synsets(stemmer.stem(word), lang='spa')
        synonyms = set()
        for synset in synsets:
            for lemma in synset.lemma_names('spa'):
                synonyms.add(lemma.lower())
        related_words += list(synonyms)

    # Cuenta la frecuencia de las palabras y sus sinónimos/relacionadas
    word_freq = Counter(words + related_words)
    ################## DESCOMENTAR SIGUIENTE LINEA PARA NO INCLUIR LOS SINONIMOS ##################
    #word_freq = Counter(words)
    ###############################################################################################

    # Agrega los resultados al DataFrame
    for word, freq in word_freq.items():
        df = pd.concat([df, pd.DataFrame({'PDF': labels[i], 'Palabra': word, 'Frecuencia': freq}, index=[0])],
                       ignore_index=True)

df.to_csv('resultados_programas_sinon.csv')

# Crea un subplot con los gráficos de barras
nrows=2
fig, axs = plt.subplots(nrows=nrows, ncols=math.ceil(len(pdf_files)/nrows), figsize=(16, 5))

# Dibuja un gráfico de barras para cada PDF
for i, pdf_file in enumerate(pdf_files):
    # Filtra los datos del DataFrame para el PDF actual
    data = df[df['PDF'] == labels[i]]

    # Selecciona las n palabras más frecuentes para el gráfico de barras
    n = 20
    top_words = dict(data.groupby('Palabra')['Frecuencia'].sum().sort_values(ascending=False)[:n].sort_values(ascending=True))

    print(top_words)

    # Dibuja el gráfico de barras
    col = i // 2
    row = i % 2
    print(col)
    print(row)
    ax = axs[row, col]
    ax.barh(list(top_words.keys()), list(top_words.values()), color=colors[i])
    ax.set_title(labels[i])

plt.show()
