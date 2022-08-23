import nltk
from nltk.corpus import stopwords
import string
import re
import pandas as pd
from tqdm import tqdm
from tqdm.notebook import tqdm_notebook
import unidecode

def content_preprocessing(text):
    text = ' '.join(remove_stopwords(text))
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(' +', ' ', text)
    return text.lower()

def remove_stopwords(sentence):
    return [ token for token in nltk.word_tokenize(sentence) if token.lower() not in stopwords.words('spanish') ]

def import_data(url):
    comunas = ["ancud", "castro", "chonchi", "curaco de velez", "dalcahue", 
           "puqueldon", "queilen", "quemchi", "quellon", "quinchao"
           "calbuco", "cochamo", "fresia", "frutillar", "llanquihue"
           "los muermos", "maullin", "puerto montt", "puerto varas", "osorno"
           "puerto octay", "purranque", "puyehue", "rio negro", "san juan de la costa",
           "san pablo", "chaiten", "futaleufu", "hualaihue", "palena"]
    df = pd.read_csv(url, sep=';', engine='python')
    df.columns = ["date", "media_outlet", "url", "title", "text"]
    df["content"] = ""
    df["content"] =  df.title + ". " + df.text
    df.content =  df.content.progress_apply(lambda x: content_preprocessing(str(x)))
    df['comuna'] = ""
    for index, row in tqdm_notebook(df.iterrows(), desc="buscando comunas en content"):
        unaccented = unidecode.unidecode(str(row["content"]).lower()) 
        # a veces tira que es float, probablemente esto se deba a un problema en el formato del dataset
        found = [comuna for comuna in comunas if(comuna in unaccented)]
        if(len(found)!= 0): df.at[index, 'comuna'] = found
    print("Largo del dataset: ", len(df))
    return df

def clean_dataset_basedOn_media(df):
    medios = ["laestrelladechiloe", "elaustral", "elllanquihue" ,"radiosago","elcalbucano",
              "elheraldoaustral","elinsular","elrepuertero","elvacanudo","seminariolocal",
              "radioacogida","elhuemul","radiopudeto","enlanoticia","fresiaahora","elquellonino",
              "segundos33","radioestrelladelmar","soypuertomontt","soyosorno", "soychiloe"]
    df = df[df['media_outlet'].isin(medios)]
    return df

def date_clustering(df):
    df['date_clustering'] = ""
    df['date_clustering']= df.apply(lambda row:  row['date'][:7], axis=1).to_list()
    return df