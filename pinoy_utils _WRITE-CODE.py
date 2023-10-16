import re
import string
import numpy as np
import pandas as pd
from nltk.tokenize import TweetTokenizer
import TglStemmer as TglStemmer

# Replace with your actual list of Filipino stopwords (2 points)
stop_words = [] 
def process_article (article):
    """Process article function.
    Input:
        article: a string containing an article
    Output:
        article_clean: a list of words containing the processed article

    """
    """
    Preprocess  article.
    Input:
        raw article: a string containing the raw    article
        stemmer: a stemmer function for Filipino words
        stop_words: a list of Filipino stopwords
    Output:
        preprocessed    article: a list of preprocessed words
    """
    # Convert to lowercase
    article =  article.lower()
    
    # Remove punctuation and special characters
    # 2 points
    article = re.sub(f"[{re.escape(string.punctuation)}]", "", article)

    # Remove single characters
    # 2 points 
    article = ' '.join([word for word in article.split() if len(word) > 1])


    # Substitute multiple spaces with single space
    # 2 points
     article = re.sub(r'\s+', ' ', article)

    # tokenize articles
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    article_token = tokenizer.tokenize(article)
    
    article_clean = []
    
for salita in article_token:
    if salita not in stop_words and salita not in string.punctuation:
       stem word = Tgl stemmer.stemmer("2" , salita, "1") #stem the word
       clean_article.append(stem_word)               
return article_clean


def build_freqs(articles, ys):
    """Build frequencies.
    Input:
        articles: a list of articles
        ys: an m x 1 array with the real/fake label of each article
            (either 0 or 1)
    Output:
        freqs: a dictionary mapping each (salita, real/fake) pair to its
        frequency
    """
    # Convert np array to list since zip needs an iterable.
    # The squeeze is necessary or the list ends up with one element.
    # Also note that this is just a NOP if ys is already a list.
    yslist = np.squeeze(ys).tolist()

     # Start with an empty dictionary and populate it by looping over all articles
    # and over all processed words in each article.
    freqs = {}
    for y, article in zip(yslist, articles):
        for salita in process_article(article):
            pair = (salita, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1

    return freqs