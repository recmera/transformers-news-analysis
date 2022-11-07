
def sentiment_emotion_analysis(df, sentiment_analyzer, emotion_analyzer):
    
    # todo: define inputs and outputs
    

    df['title_sentiment_roBERTuito'] = ""
    df['title_emotion_roBERTuito'] = ""
    df['title_sentiment_BETO'] = ""
    df['text_sentiment_BETO'] = ""

    for index, row in tqdm(sub.iterrows(), desc='sub rows - sentiment', total=sub.shape[0]):
        # análisis del título de la noticia
        sub.at[index, "title_sentiment_roBERTuito"] = sentiment_analyzer.predict(row['title'])
        sub.at[index, "title_emotion_roBERTuito"] = emotion_analyzer.predict(row['title'])
        sub.at[index, 'title_sentiment_BETO'] = nlp(row['title'])

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

        sub.at[index, "text_sentiment_BETO"] = {"NEU": count_neutral, "NEG": count_negative, "POS": count_positive}