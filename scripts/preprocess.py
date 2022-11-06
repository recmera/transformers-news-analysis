import nltk
import string
import re
import unidecode

import pandas as pd
from tqdm import tqdm
from tqdm.notebook import tqdm_notebook

from nltk.corpus import stopwords
#from nltk.stem import SnowballStemmer
#stemmer = SnowballStemmer('spanish')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from nltk.tokenize import word_tokenize


# Funciones útiles
def remove_stopwords(sentence):
    return " ".join([token for token in nltk.word_tokenize(sentence) 
                     if token.lower() not in stopwords.words('spanish') and  
                     len(token) > 2])

def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])

def lemmatize_words(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])
    
def preprocess(text):
    text = clean_text(text)
    # borrar espacios multiples
    text = re.sub(' +', ' ', text)
    # borrar stopwords
    text = remove_stopwords(text)
    # obtener las raices de palabras -- no me gusta el resultado --
        #text = stem_words(text)
    # obtenemos la forma canonica de la palabra
    text = lemmatize_words(text)
    # obtenemos los tokens
    text = word_tokenize(text)
    return text

def find_cities(text):
    cities = [
        "ancud", "castro", "chonchi", "curaco de velez", "dalcahue", 
        "puqueldon", "queilen", "quemchi", "quellon", "quinchao"
        "calbuco", "cochamo", "fresia", "frutillar", "llanquihue"
        "los muermos", "maullin", "puerto montt", "puerto varas", "osorno",
        "puerto octay", "purranque", "puyehue", "rio negro", "san juan de la costa",
        "san pablo", "chaiten", "futaleufu", "hualaihue", "palena"]
    text = clean_text(text)
    #found = [city for city in cities if(city in text)]
    
    found = []
    for city in cities:
        if city in text: found.append(city)
            
    return found

def clean_text(text):
    # transformar caracteres acentuados a no acentuados
    text = unidecode.unidecode(text)
    # borrar caracteres distintos a los alfabeticos
    text = re.sub(r'[^A-Za-z ]+', "", text) #^A-Za-z0-9 alfanumericos
    # borrar puntuaciones
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    # borrar palabras comprometidas con numeros
    text = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text)
    
    return text

def filter_by_media(df):
    medios = [
        "laestrelladechiloe", "elaustral", "elllanquihue" ,"radiosago","elcalbucano",
        "elheraldoaustral","elinsular","elrepuertero","elvacanudo","seminariolocal",
        "radioacogida","elhuemul","radiopudeto","enlanoticia","fresiaahora","elquellonino",
        "segundos33","radioestrelladelmar","soypuertomontt","soyosorno", "soychiloe"]
    df = df[df['media_outlet'].isin(medios)]
    df = df[df['content'].notna()]
    return df

def cluster_by_month(df):
    df['date_clustering'] = ""
    df['date_clustering']= df.apply(lambda row:  row['date'][:7], axis=1).to_list()
    return df








# OLD
# Esta es una función para limpiar el dataset --sin embargo, creo que ya no es útil--
def import_data(url):
    comunas = [
        "ancud", "castro", "chonchi", "curaco de velez", "dalcahue", 
        "puqueldon", "queilen", "quemchi", "quellon", "quinchao"
        "calbuco", "cochamo", "fresia", "frutillar", "llanquihue"
        "los muermos", "maullin", "puerto montt", "puerto varas", "osorno"
        "puerto octay", "purranque", "puyehue", "rio negro", "san juan de la costa",
        "san pablo", "chaiten", "futaleufu", "hualaihue", "palena"
    ]
    
    df = pd.read_csv(url, sep=';', engine='python')
    df.columns = ["date", "media_outlet", "url", "title", "text"]
    df["content"] = ""
    df["content"] =  df.title + ". " + df.text
    df['comuna'] = ""
    df.content =  df.content.progress_apply(lambda x: preprocess(str(x)))
    
    for index, row in tqdm_notebook(df.iterrows(), desc="buscando comunas en content"):
        unaccented = unidecode.unidecode(str(row["content"]).lower()) 
        # a veces tira que es float, probablemente esto se deba a un problema en el formato del dataset
        found = [comuna for comuna in comunas if(comuna in unaccented)]
        if(len(found)!= 0): df.at[index, 'comuna'] = found
 
    return df