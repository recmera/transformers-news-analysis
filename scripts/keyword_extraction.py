from keybert import KeyBERT

def extract_ngram_keywords(ngram_size, word_doc_embedder, docs):

    kw_model = KeyBERT(model=word_doc_embedder)
    doc_embeddings, word_embeddings = kw_model.extract_embeddings(docs,
                                                                  keyphrase_ngram_range=ngram_size)
    column =  kw_model.extract_keywords(docs,
                                          doc_embeddings=doc_embeddings,
                                          word_embeddings=word_embeddings,
                                          keyphrase_ngram_range=ngram_size,
                                          use_mmr=True)
    return column 