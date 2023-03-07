from tqdm import tqdm
from tqdm.notebook import tqdm_notebook
tqdm.pandas()
import pandas as pd

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from pysentimiento import create_analyzer


def sentiment_analysis(df, sentiment_analyzer, nlp):
    
    
    df["title_sentiment_roBERTuito"]=""
    df["title_sentiment_BETO"]=""
    df["text_sentiment_BETO"]=""

    for index, row in tqdm(df.iterrows(), desc='df rows - sentiment', total=df.shape[0]):
        # análisis del título de la noticia
        df.at[index, "title_sentiment_roBERTuito"] = list(sentiment_analyzer.predict(row['title']).probas.keys())[0]
        df.at[index, 'title_sentiment_BETO'] = nlp(row['title'])[0].get('label')

        # análisis del cuerpo de la noticia
        count_neutral = 0
        count_negative = 0
        count_positive = 0
        partition = row['text'].split(".")
        for text in partition:
            # Analizamos su sentimiento
            sentiment_value = nlp(text)
            if sentiment_value[0].get('label') == "NEU": count_neutral=count_neutral+1
            if sentiment_value[0].get('label') == "NEG": count_negative=count_negative+1
            if sentiment_value[0].get('label') == "POS": count_positive=count_positive+1
            d = {"NEU": count_neutral, "NEG": count_negative, "POS": count_positive}

            df.at[index, "text_sentiment_BETO"] = max(d, key=d.get)
    
    return df