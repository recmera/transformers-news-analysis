import pandas as pd
import gensim.corpora as corpora
from gensim.models.coherencemodel import CoherenceModel

def cv_umass_npmi(docs, topics, topic_model):

    # Preprocess Documents
    documents = pd.DataFrame({"Document": docs,
                              "ID": range(len(docs)),
                              "Topic": topics})
    documents_per_topic = documents.groupby(['Topic'], as_index=False).agg({'Document': ' '.join})
    cleaned_docs = topic_model._preprocess_text(documents_per_topic.Document.values)

    # Extract vectorizer and analyzer from BERTopic
    vectorizer = topic_model.vectorizer_model
    analyzer = vectorizer.build_analyzer()

    # Extract features for Topic Coherence evaluation
    words = vectorizer.get_feature_names()
    tokens = [analyzer(doc) for doc in cleaned_docs]
    dictionary = corpora.Dictionary(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    topic_words = [[words for words, _ in topic_model.get_topic(topic)] 
                   for topic in range(len(set(topics))-1)]
    # Evaluate
    cv_coherence_model = CoherenceModel(topics=topic_words, 
                                        texts=tokens, 
                                        corpus=corpus,
                                        dictionary=dictionary, 
                                        coherence='c_v')

    umass_coherence_model = CoherenceModel(topics=topic_words, 
                                           texts=tokens, 
                                           corpus=corpus,
                                           dictionary=dictionary, 
                                           coherence='u_mass')
    
    c_npmi_coherence_model = CoherenceModel(topics=topic_words, 
                                            texts=tokens, 
                                            corpus=corpus,
                                            dictionary=dictionary, 
                                            coherence='c_npmi')

    cv_coherence = cv_coherence_model.get_coherence()
    umass_coherence = umass_coherence_model.get_coherence()
    c_npmi_coherence = c_npmi_coherence_model.get_coherence()

    return cv_coherence, umass_coherence, c_npmi_coherence