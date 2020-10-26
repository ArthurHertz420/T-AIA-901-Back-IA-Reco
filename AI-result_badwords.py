import csv
import numpy as np
import pandas as pd
import re
import nltk
from nltk.stem.snowball import FrenchStemmer
import string


# Lire les données depuis le fichier CSV
rawData = pd.read_csv("bad_wordFinal.csv", sep=';')

def remove_punct(text):
    text_nopunct = "".join([char for char in str(text) if char not in string.punctuation])  # retire toute les ponctuations
    return text_nopunct


rawData['body_text_clean'] = rawData['Data'].apply(lambda x: remove_punct(x))


def tokenize(text):
    tokens = re.split('\W+', str(text))  # W+ veux dire sois un caratère A-Za-z0-9 ou un tiret
    return tokens


rawData['body_text_tokenized'] = rawData['body_text_clean'].apply(lambda x: tokenize(x.lower()))

stopword = nltk.corpus.stopwords.words('french')


# Function pour retirer les stopwords
def remove_stopwords(tokenized_list):
    text = [word for word in tokenized_list if word not in stopword]  # suppression des stopwords
    return text


rawData['body_text_nostop'] = rawData['body_text_tokenized'].apply(lambda x: remove_stopwords(x))

# rawData['body_text_stemmed'] = rawData['body_text_nostop'].apply(lambda x: stemming(x))
print(rawData['body_text_nostop'])

a = rawData['body_text_nostop']

a.to_csv('resultat2.csv')