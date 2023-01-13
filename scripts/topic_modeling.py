from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP
from hdbscan import HDBSCAN



# this script needs to become a class if we want to use different hyperparameters to test coherence in multiple models


def model_definition(nlp):

    vectorizer_model = CountVectorizer(ngram_range=(1, 3), stop_words=None)
    
    umap_model = UMAP(n_neighbors=15, 
                      n_components=5, 
                      min_dist=0.0, 
                      metric='cosine', 
                      random_state=42)
    
    hdbscan_model = HDBSCAN(min_cluster_size=10, 
                            metric='euclidean', 
                            cluster_selection_method='eom', 
                            prediction_data=True, 
                            min_samples=5)

    topic_model = BERTopic(n_gram_range=(1,3),
                           top_n_words=15,
                           diversity=0.2, 
                           embedding_model=nlp,
                           language="multilingual", 
                           vectorizer_model=vectorizer_model,
                           umap_model=umap_model,
                           hdbscan_model=hdbscan_model,
                           calculate_probabilities=True,
                           verbose=True)

    return topic_model