import pandas as pd
import spacy
from collections import Counter

def edit_year(df):
    """ Modifies year value from float to datetime."""
    
    df_output = df.copy()  # Create a copy
    df_output['Year'] = df['Year'].astype(int)
    
    return df_output

def get_most_common_words(df, year, n=25):
    """
    Processes the SOTU speech for a given year and returns
    the most common non-stopword/punctuation lemmas.
    """
    # subsetting df
    df = edit_year(df)
    df = df[df['Year'] == year]

    # text processing
    nlp = spacy.load("en_core_web_sm")
    df_text = df["Text"].apply(nlp)
    
    speeches = [token for token in df_text]
    token_list = [token for s in speeches for token in s]
    
    list_lemmas = [
    token.lemma_.lower()
    for token in token_list
    if is_token_allowed(token)
    ]

    # get lemmas
    count_n = Counter(list_lemmas).most_common(n)
    
    return count_n

def is_token_allowed(token):
    allowed = bool(token
                   and not token.is_stop
                       and not token.is_punct
                           and not token.is_space)
    return allowed