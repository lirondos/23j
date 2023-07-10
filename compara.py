from itertools import combinations
import pandas as pd
import scattertext as st
import spacy
from spacy.lang.es.stop_words import STOP_WORDS

STOP_WORDS.update(["»","—", "«", "cuyas", "cuyos", "–", "000", "etc", "etcétera", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "as"])
STOP_WORDS.update({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'})

for number in range(0, 100):
    STOP_WORDS.add(str(number))
    STOP_WORDS.add(number)
    
print(STOP_WORDS)

nlp = spacy.load('es_core_news_sm', disable=['parser', 'ner', 'textcat'])
nlp.add_pipe('sentencizer')
nlp.max_length = 1500000


PARTIDOS = ["PP", "PSOE", "SUMAR", "VOX"]


if __name__ == '__main__':

    for partido, otro_partido in combinations(PARTIDOS,2):
            with open("programastxt/" + partido + ".txt", "r", encoding="utf-8") as f1, open("programastxt/" + otro_partido + ".txt", "r", encoding="utf-8")  as f2:
                programa = f1.read()
                otro_programa = f2.read()
                data = {"partido": [partido, otro_partido], "programa": [programa, otro_programa]}
                df = pd.DataFrame(data)
                corpus = st.CorpusFromPandas(df, category_col="partido", text_col='programa', nlp=st.whitespace_nlp_with_sentences).build().remove_terms(STOP_WORDS, ignore_absences=True)
                html = st.produce_scattertext_explorer(corpus, category=partido, category_name=partido, not_category_name=otro_partido, width_in_pixels=1000)
                open("comparaciones/" + partido+"vs" + otro_partido + ".html", 'wb').write(html.encode('utf-8'))

                
         

