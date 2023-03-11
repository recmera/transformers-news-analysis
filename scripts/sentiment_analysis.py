from tqdm import tqdm
from tqdm.notebook import tqdm_notebook
tqdm.pandas()
import pandas as pd

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from pysentimiento import create_analyzer


def sentiment_analysis(df, sentiment_analyzer, nlp):
    
    
    df["topic_sentiment_roBERTuito"]= ""
    df["reasons_sentiment_roBERTuito"]= ""
    df["topic_sentiment_BETO"]= ""
    df["reasons_sentiment_BETO"]= ""

    for index, row in tqdm(df.iterrows(), desc='df rows - sentiment', total=df.shape[0]):
        # análisis del título de la noticia
        df.at[index, "topic_sentiment_roBERTuito"] = sentiment_analyzer.predict(row['topic']).output
        df.at[index, 'topic_sentiment_BETO'] = nlp(row['topic'])[0].get('label')
        df.at[index, "reasons_sentiment_roBERTuito"] = sentiment_analyzer.predict(row['reasons']).output
        df.at[index, 'reasons_sentiment_BETO'] = nlp(row['reasons'])[0].get('label')
        
    
    return df